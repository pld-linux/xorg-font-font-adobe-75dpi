# $Rev: 3189 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	font-adobe-75dpi
Summary(pl):	font-adobe-75dpi
Name:		xorg-font-font-adobe-75dpi
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-adobe-75dpi-%{version}.tar.bz2
# Source0-md5:	46c7a56e2085c087ca84f6836d91fd9c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/font-adobe-75dpi-%{version}-root-%(id -u -n)

%description
font-adobe-75dpi

%description -l pl
font-adobe-75dpi


%prep
%setup -q -n font-adobe-75dpi-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/75dpi/*
