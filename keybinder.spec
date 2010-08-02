%define srcname keybinder

%define major 0
%define libname %mklibname %srcname %major
%define develname %mklibname -d %srcname

Summary:	A library for registering global keyboard shortcuts
Name:		keybinder
Version:	0.2.2
Release:	%mkrel 1
Url:		http://kaizer.se/wiki/keybinder/
Source0:	http://kaizer.se/publicfiles/keybinder/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgtk+2-devel
BuildRequires:	python-devel pygtk2.0-devel python-gobject-devel
BuildRequires:	lua-devel

%description
keybinder is a library for registering global keyboard shortcuts. Keybinder works
with GTK-based applications using the X Window System.

The library contains:
- A C library, libkeybinder
- Lua bindings, lua-keybinder
- Python bindings, python-keybinder
- An examples directory with programs in C, Lua, Python and Vala.

%package -n %libname
Group:		Development/Python
Summary:	%{name} library package

%description -n %libname
%summary.

%package -n %develname
Group:		Development/Python
Summary:	%{name} developement files
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %develname
This package contains header files needed when building applications based on
%{name}.

%package -n python-%{srcname}
Group:		Development/Python
Summary:	%{name} python bindings
Requires:	%{libname} = %{version}
Requires:	pygtk2.0 python-gobject

%description -n python-%{srcname}
This package contains python bindings for keybinder.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --disable-static --enable-python
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# don't ship .la
find %{buildroot} -name '*.la' | xargs rm -f

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog NEWS AUTHORS README

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libkeybinder.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_includedir}/keybinder.h
%{_libdir}/lua/*/keybinder.so
%{_libdir}/libkeybinder.so
%{_libdir}/pkgconfig/keybinder.pc

%files -n python-%{name}
%defattr(-,root,root)
%{python_sitearch}/%{name}
