Summary:	Zero storage carving library
Name:		libcarvpath
Version:	2.3.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/carvpath/%{name}%{version}.tgz
# Source0-md5:	dac237151a2fed70f86024abe55f9d5b
URL:		http://ocfa.sourceforge.net/libcarvpath/
BuildRequires:	cmake
BuildRequires:	sqlite3-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple translation library to map multi level fragment lists to
virtual paths and back. It is meant to be used by forensic carving
tools and by pseudo filesystems that give access to data in disk
imaging file formats (raw,ewf,aff).

%package devel
Summary:	Development libraries for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name}.

%prep
%setup -q -n %{name}%{version}

%build
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcflags}"
%{__cmake} src \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.?

%files devel
%attr(755,root,root) %{_libdir}/%{name}.so
%{_includedir}/%{name}.h
