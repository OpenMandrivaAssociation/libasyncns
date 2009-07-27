%define shortname asyncns
%define name libasyncns
%define version 0.7
%define release %mkrel 1

%define major 0
%define libname %mklibname %shortname %major
%define libname_devel %mklibname -d %shortname

Summary: A library for executing name service queries asynchronously
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://0pointer.de/lennart/projects/libasyncns/%{name}-%{version}.tar.gz
License: LGPL
Group: System/Libraries
URL: http://0pointer.de/lennart/projects/libasyncns/
BuildRequires : doxygen
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A small and lightweight library that implements easy to use asynchronous
wrappers around the libc NSS functions getaddrinfo(), res_query() and related.


#----------------------------------------------------------------------------

%package -n %{libname}
Summary: A library for executing name service queries asynchronously
Group: System/Libraries
Provides: %name = %{version}-%{release}

%description -n %{libname}
A small and lightweight library that implements easy to use asynchronous
wrappers around the libc NSS functions getaddrinfo(), res_query() and related.


#----------------------------------------------------------------------------

%package -n %{libname_devel}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}


%description -n %{libname_devel}
Development files for %{name}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} \( -name *.a -o -name *.la \) -exec rm -f {} \;

%clean
rm -rf %{buildroot}

#----------------------------------------------------------------------------

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/%{name}.so.%{major}*

%files -n %{libname_devel}
%defattr(-,root,root)
%doc %{_docdir}/%{name}
%{_includedir}/%{shortname}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

