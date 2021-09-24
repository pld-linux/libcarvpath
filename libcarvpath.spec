Summary:	Zero storage carving library
Summary(pl.UTF-8):	Biblioteka do sekcji bez zapisu danych
Name:		libcarvpath
Version:	2.3.0
%define	subver	rc8
Release:	5
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/DNPA/libcarvpath/releases
Source0:	https://github.com/DNPA/libcarvpath/archive/R%{version}%{subver}/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	0deb0d1533c5eba85d0edb9d2bcc3ed6
Patch0:		openssl.patch
URL:		http://ocfa.sourceforge.net/libcarvpath/
BuildRequires:	cmake >= 2.6
BuildRequires:	openssl-devel
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple translation library to map multi level fragment lists to
virtual paths and back. It is meant to be used by forensic carving
tools and by pseudo filesystems that give access to data in disk
imaging file formats (raw, ewf, aff), like CarvFS filesystem.

%description -l pl.UTF-8
Prosta biblioteka transakcyjna, odwzorowująca wielopoziomowe listy
fragmentów na wirtualne ściezki i z powrotem. Jest przeznaczona dla
narzędzi do sekcji śledczej oraz pseudosystemy plików udostępniające
dane w formatach plików obrazów dysków (raw, ewf, aff), jak np.
system plików CarvFS.

%package devel
Summary:	Header file for libcarvpath library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libcarvpath
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for libcarvpath library, needed to develop programs using
the library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki libcarvpath, potrzebny do tworzenia
programów z użyciem tej biblioteki.

%prep
%setup -q -n %{name}-R%{version}%{subver}
%patch0 -p1

sed -e 's|/lib\b|/%{_lib}|g' -i src/CMakeLists.txt

%build
install -d build
cd build
%cmake ../src

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libcarvpath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcarvpath.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcarvpath.so
%{_includedir}/libcarvpath.h
