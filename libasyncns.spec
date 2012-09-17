%define shortname asyncns

%define major 0
%define libname %mklibname %{shortname} %{major}
%define libname_devel %mklibname -d %{shortname}

Summary:	A library for executing name service queries asynchronously
Name:		libasyncns
Version:	0.8
Release:	4
License:	LGPL
Group:		System/Libraries
URL:		http://0pointer.de/lennart/projects/libasyncns/
Source0:	http://0pointer.de/lennart/projects/libasyncns/%{name}-%{version}.tar.gz
Patch0:		libasyncns-0.8-libdir.patch
BuildRequires:	doxygen

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

%package -n %{libname_devel}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libname_devel}
Development files for %{name}

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
find %{buildroot} \( -name *.a -o -name *.la \) -exec rm -f {} \;

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{libname_devel}
%doc %{_docdir}/%{name}
%{_includedir}/%{shortname}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
