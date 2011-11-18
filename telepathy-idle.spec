Summary:	A Telepathy connection manager for IRC
Summary(pl.UTF-8):	Zarządca połączeń Telepathy dla IRC-a
Name:		telepathy-idle
Version:	0.1.11
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-idle/%{name}-%{version}.tar.gz
# Source0-md5:	be277e8f0bd32ae56af799f0ff4ec72e
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 2.28.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
BuildRequires:	telepathy-glib-devel >= 0.15.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A connection manager to connect Telepathy to IRC.

%description -l pl.UTF-8
Zarządca połączeń pozwalający połączyć się Telepathy z IRC-em.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libexecdir}/telepathy-idle
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.idle.service
%{_datadir}/telepathy/managers/idle.manager
%{_mandir}/man8/telepathy-idle.8*
