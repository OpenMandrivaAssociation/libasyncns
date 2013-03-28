%define shortname asyncns
%define name libasyncns
%define version 0.8
%define release %mkrel 4

%define major 0
%define libname %mklibname %shortname %major
%define libname_devel %mklibname -d %shortname

%bcond_with	crosscompile

Summary: A library for executing name service queries asynchronously
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://0pointer.de/lennart/projects/libasyncns/%{name}-%{version}.tar.gz
License: LGPL
Group: System/Libraries
URL: http://0pointer.de/lennart/projects/libasyncns/
BuildRequires : doxygen

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
autoreconf -fi
%if %{with crosscompile}
export ac_cv_func_malloc_0_nonnull=yes
%endif
%configure2_5x --disable-static
%make

%install
%makeinstall_std
find %{buildroot} \( -name *.a -o -name *.la \) -exec rm -f {} \;

#----------------------------------------------------------------------------

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{libname_devel}
%doc %{_docdir}/%{name}
%{_includedir}/%{shortname}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc



%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8-3mdv2011.0
+ Revision: 660216
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-2mdv2011.0
+ Revision: 602522
- rebuild

* Thu Nov 05 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8-1mdv2010.1
+ Revision: 460435
- New version: 0.8

* Mon Jul 27 2009 Emmanuel Andry <eandry@mandriva.org> 0.7-1mdv2010.0
+ Revision: 400829
- New version 0.7
- update files list

* Sat Oct 25 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6-1mdv2009.1
+ Revision: 297202
- New version: 0.6

* Mon Jul 28 2008 Colin Guthrie <cguthrie@mandriva.org> 0.4-1mdv2009.0
+ Revision: 251242
- Fix group
- Minor file list change to inlcude library major number in filespec
- import libasyncns


