Summary:	C++ Framework for creating GNOME applications
Summary(pl):	Struktura C++ do tworzenia programów dla GNOME
Name:		bakery
Version:	2.3.15
Release:	1
License:	GPL v.2
Group:		X11/Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/bakery/2.3/%{name}-%{version}.tar.gz
# Source0-md5:	735d83cb4a93630706edef5120e1a2f8
URL:		http://bakery.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gconfmm-devel >= 2.6.0
BuildRequires:	gnome-vfsmm-devel >= 2.6.0
BuildRequires:	gtkmm-devel >= 2.6.0
BuildRequires:	intltool
BuildRequires:	libglademm-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml++-devel >= 2.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bakery is a C++ Framework for creating document-based GNOME
applications using gtkmm and/or gnomemm.

- provides a Document/View architecture,
- can use XML as a Document storage format,
- provides default functionality, which can be easily customized,
- makes it easy to start developing GNOME applications,
- gives your application structure,
- contains a few utility classes.

%description -l pl
Bakery jest struktur± C++ do tworzenia opartych na dokumentach
programów dla GNOME przy u¿yciu gtkmm i/lub gnomemm.

- dostarcza architektury Dokument/Widok
- mo¿e u¿ywaæ XML jako formatu zapisu Dokumentu,
- dostarcza domy¶lnej, ³atwo modyfikowalnej funkcjonalno¶ci,
- pozwala na ³atwy start w tworzeniu aplikacji GNOME,
- nadaje aplikacji format,
- zawiera kilka klas u¿ytkowych

%package devel
Summary:	Bakery header files
Summary(pl):	Pliki nag³ówkowe Bakery
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gconfmm-devel >= 2.6.0
Requires:	gnome-vfsmm-devel >= 2.6.0
Requires:	gtkmm-devel >= 2.6.0
Requires:	libglademm-devel >= 2.4.0
Requires:	libxml++-devel >= 2.8.0

%description devel
Header files for Bakery framework.

%description devel -l pl
Pliki nag³ówkowe dla struktury Bakery.

%package static
Summary:	Static Bakery library
Summary(pl):	Statyczna biblioteka Bakery
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Bakery library.

%description static -l pl
Statyczna biblioteka Bakery.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# bogus (well, author is German guy ;)
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/de

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/bakery-2.4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
