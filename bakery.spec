Summary:	C++ Framework for creating GNOME applications
Summary(pl.UTF-8):	Struktura C++ do tworzenia programów dla GNOME
Name:		bakery
Version:	2.6.3
Release:	4
License:	LGPL v2+
Group:		X11/Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/bakery/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	49d28fecf13252f4f2899461505e56e5
# http://bugzilla.gnome.org/show_bug.cgi?id=564168
Patch0:		%{name}-release-version.patch
URL:		http://bakery.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gconfmm-devel >= 2.16.0
BuildRequires:	gettext-tools
BuildRequires:	glibmm-devel >= 2.16.0
BuildRequires:	gtkmm-devel >= 2.10.5
BuildRequires:	intltool
BuildRequires:	libglademm-devel >= 2.6.3
BuildRequires:	libstdc++-devel >= 6:4.3
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml++2-devel >= 2.24.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gconfmm >= 2.16.0
Requires:	gtkmm >= 2.10.5
Requires:	libglademm >= 2.6.3
Requires:	libxml++2 >= 2.24.0
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

%description -l pl.UTF-8
Bakery jest strukturą C++ do tworzenia opartych na dokumentach
programów dla GNOME przy użyciu gtkmm i/lub gnomemm.

- dostarcza architektury Dokument/Widok
- może używać XML jako formatu zapisu Dokumentu,
- dostarcza domyślnej, łatwo modyfikowalnej funkcjonalności,
- pozwala na łatwy start w tworzeniu aplikacji GNOME,
- nadaje aplikacji format,
- zawiera kilka klas użytkowych

%package devel
Summary:	Bakery header files
Summary(pl.UTF-8):	Pliki nagłówkowe Bakery
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gconfmm-devel >= 2.16.0
Requires:	glibmm-devel >= 2.16.0
Requires:	gtkmm-devel >= 2.10.5
Requires:	libglademm-devel >= 2.6.3
Requires:	libxml++2-devel >= 2.24.0

%description devel
Header files for Bakery framework.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla struktury Bakery.

%package static
Summary:	Static Bakery library
Summary(pl.UTF-8):	Statyczna biblioteka Bakery
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Bakery library.

%description static -l pl.UTF-8
Statyczna biblioteka Bakery.

%prep
%setup -q
%patch -P0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# for glibmm 2.46+/libxml++ 2.40+
CXXFLAGS="%{rpmcxxflags} -std=c++0x"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libbakery-*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libbakery-2.6-2.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbakery-2.6-2.6.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbakery-2.6.so
%dir %{_libdir}/bakery-2.6
%{_libdir}/bakery-2.6/include
%{_includedir}/bakery-2.6
%{_pkgconfigdir}/bakery-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libbakery-2.6.a
