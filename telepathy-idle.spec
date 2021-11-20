Summary:	A Telepathy connection manager for IRC
Summary(pl.UTF-8):	Zarządca połączeń Telepathy dla IRC-a
Name:		telepathy-idle
Version:	0.2.2
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://telepathy.freedesktop.org/releases/telepathy-idle/%{name}-%{version}.tar.gz
# Source0-md5:	a2ecfaa76f5180359bcbc3caa66c5e55
Patch0:		%{name}-am.patch
URL:		https://telepathy.freedesktop.org/components/telepathy-idle
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-devel >= 0.51
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	sed >= 4.0
BuildRequires:	telepathy-glib-devel >= 0.21
Requires:	dbus >= 0.51
Requires:	dbus-glib >= 0.61
Requires:	glib2 >= 1:2.32.0
Requires:	telepathy-glib >= 0.21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A connection manager to connect Telepathy to IRC.

%description -l pl.UTF-8
Zarządca połączeń pozwalający połączyć się Telepathy z IRC-em.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/python$,%{__python3},' tools/*.py

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON="%{__python3}" \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libexecdir}/telepathy-idle
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.idle.service
%{_datadir}/telepathy/managers/idle.manager
%{_mandir}/man8/telepathy-idle.8*
