%define sname	asyncns
%define major	0
%define libname	%mklibname %{sname} %{major}
%define devname %mklibname -d %{sname}

%bcond_with	crosscompile

Summary:	A library for executing name service queries asynchronously
Name:		libasyncns
Version:	0.8
Release:	23
License:	LGPLv2
Group:		System/Libraries
Url:		https://0pointer.de/lennart/projects/libasyncns/
Source0:	http://0pointer.de/lennart/projects/libasyncns/%{name}-%{version}.tar.gz
Patch0:		libasyncns-no-Lusrlib.patch
BuildRequires :	doxygen

%description
A small and lightweight library that implements easy to use asynchronous
wrappers around the libc NSS functions getaddrinfo(), res_query() and related.

%package -n %{libname}
Summary:	A library for executing name service queries asynchronously
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
A small and lightweight library that implements easy to use asynchronous
wrappers around the libc NSS functions getaddrinfo(), res_query() and related.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%prep
%autosetup -p1
autoreconf -fi
%if %{with crosscompile}
export ac_cv_func_malloc_0_nonnull=yes
%endif

%build
%configure --disable-static
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%doc %{_docdir}/%{name}
%{_includedir}/%{sname}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
