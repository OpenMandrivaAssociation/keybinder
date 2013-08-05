%define major 0
%define gmajor 0.0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define girname %mklibname %{name}-gir %{gmajor}
%define _disable_ld_no_undefined 1

Summary:	A library for registering global keyboard shortcuts
Name:		keybinder
Version:	0.3.0
Release:	1
Url:		http://kaizer.se/wiki/keybinder/
Source0:	http://kaizer.se/publicfiles/keybinder/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python

BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	python-devel
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
Keybinder is a library for registering global keyboard shortcuts. 
Keybinder works with GTK-based applications 
using the X Window System.

The library contains:
- A C library, libkeybinder
- Lua bindings, lua-keybinder
- Python bindings, python-keybinder
- An examples directory with programs in C, Lua, 
Python and Vala.

%package -n %{libname}
Group:		Development/Python
Summary:	Library package

%description -n %{libname}
%summary.

%package -n %{develname}
Group:		Development/Python
Summary:	Development files
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
This package contains header files needed when building 
applications based on %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n python-%{name}
Group:		Development/Python
Summary:	Python bindings
Requires:	%{libname} = %{EVRD}
Requires:	pygtk2.0
Requires:	python-gobject

%description -n python-%{name}
This package contains python bindings for keybinder.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-python \
	--enable-introspection=yes

%make

%install
%makeinstall_std

# don't ship .la
find %{buildroot} -name '*.la' | xargs rm -f

%files
%doc NEWS AUTHORS README

%files -n %libname
%{_libdir}/libkeybinder.so.%{major}*

%files -n %{develname}
%doc NEWS AUTHORS README
%{_includedir}/keybinder.h
%{_libdir}/lua/*/keybinder.so
%{_libdir}/libkeybinder.so
%{_libdir}/pkgconfig/keybinder.pc

%files -n %{girname}
%{_libdir}/girepository-1.0/Keybinder-%{gmajor}.typelib

%files -n python-%{name}
%{python_sitearch}/%{name}
