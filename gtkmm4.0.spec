%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1
%define _disable_lto 1

%define pkgname	gtkmm
%define api	4.0
%define major	0
%define libname %mklibname %{pkgname} %{api} %{major}
%define libgdkmm %mklibname gdkmm %{api} %{major}
%define devname %mklibname -d %{pkgname} %{api}

Summary:	C++ interface for popular GUI library gtk+
Name:		%{pkgname}%{api}
Version:	4.10.0
Release:	1
#gw lib is LGPL, tool is GPL
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
Url:		http://gtkmm.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/%{url_ver}/%{pkgname}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:  cmake
BuildRequires:	doxygen
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(atkmm-2.36)
BuildRequires:	pkgconfig(cairomm-1.16)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glibmm-2.68)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(pangomm-2.48)
BuildRequires:  pkgconfig(epoxy)


%description
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package	-n %{libname}
Summary:	C++ interface for popular GUI library gtk+
Group:		System/Libraries
Provides:	%{pkgname}%{api} = %{version}-%{release}

%description	-n %{libname}
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains the library needed to run programs dynamically
linked with %{pkgname}.

%package	-n %{devname}
Summary:	Headers and development files of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-doc < 3.4.2-2

%description	-n %{devname}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{pkgname}.

%prep
%setup -qn %{pkgname}-%{version}

%build
%meson

%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libgtkmm-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING NEWS README* ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/gtkmm-%{api}
%{_libdir}/pkgconfig/*.pc
