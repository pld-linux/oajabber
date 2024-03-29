%define _snap 20040913

Summary:	Portable, flexible C++ Jabber/XMPP library
Summary(pl.UTF-8):	Przenośna, elastyczna biblioteka Jabbera/XMPP dla C++
Name:		oajabber
Version:	%{_snap}
Release:	0.1
Epoch:		0
License:	LGPL
Group:		Libraries
Source0:	oa-core-%{version}.tar.bz2
# Source0-md5:	ef352ff310d3cb091fafeae879f034a4
Patch0:		%{name}-apr_includes.patch
URL:		http://gen.openaether.org/oajabber.html
BuildRequires:	apr-util-devel >= 1:1.0.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	boost-python-devel
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	oapr-devel
BuildRequires:	which
BuildRequires:	xerces-c-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ library for the XMPP/Jabber protocol. It is designed to be
portable and flexible. It aims to be the most complete C++ XMPP/Jabber
implementation.

%description -l pl.UTF-8
Biblioteka C++ obsługującą protokół XMPP/Jabber, przenośna i
elastyczna. Celem jest zapewnienie najbardziej kompletnej
implementacji XMPP/Jabber dla C++.

%package devel
Summary:	Header files for oajabber library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki oajabber
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	apr-devel >= 1:1.0.0
Requires:	boost-utility-devel

%description devel
Header files for oajabber libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki oajabber.

%package static
Summary:	Static oajabber libraries
Summary(pl.UTF-8):	Statyczne biblioteki oajabber
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static oajabber libraries.

%description static -l pl.UTF-8
Statyczne biblioteki oajabber.

%prep
%setup -q -n oa-core-%{_snap}
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-apr=%{_bindir}/apr-1-config \
	--with-apr-util=%{_bindir}/apu-1-config \
 	--with-oapu=%{_bindir}

%{__make} \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/oa-core

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
