%define	build_mysql 1
%{?_with_mysql:	%global build_mysql 1}
%define	build_freetds 0
%{?_with_freetds:	%global build_freetds 1}
%define	build_mdb 0
%{?_with_mdb:	%global build_mdb 1}

%define	url_ver %(echo %{version}|cut -d. -f1,2)

%define	pkgname libgda
%define	oname	gda
%define	api	3.0
%define	major	2
%define	xsltmaj	0
%define	libname	%mklibname %{oname} %{api} %{major} 
%define	libreport %mklibname gda-report %{api} %{major}
%define	libsql %mklibname gdasql %{api} %{major}
%define	libxslt %mklibname gda-xslt %{api} %{xsltmaj} 
%define	devname	%mklibname -d %{oname}%{api}
#### TODO: this package should be called libgda3.0 ####

Summary:	GNU Data Access
Name:		gda2.0
Version:	3.1.5
Release:	19
License:	GPLv2+ and LGPLv2+
Group:		Databases
Url:		http://www.gnome-db.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{url_ver}/%{pkgname}-%{version}.tar.bz2
Patch0:		libgda-3.1.5-format-strings.patch
Patch1:		libgda-3.1.5-fix-install.patch
Patch2:		libgda-3.1.5-xbase64.patch
Patch3:		libgda-3.1.5-lib64.patch
Patch4:		libgda-3.1.5-glib-includes.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	rarian
BuildRequires:	db-devel
BuildRequires:	gdbm-devel
BuildRequires:	openldap-devel
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
BuildRequires:	unixODBC-devel
BuildRequires:	xbase-devel
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(sqlite3)
%if %{build_mysql}
BuildRequires:	mysql-devel
%endif
%if %{build_freetds}
BuildRequires:	freetds-devel
%endif
%if %{build_mdb}
BuildRequires:	libmdbtools-devel
%endif

%description
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

Drivers for the supported databases are included in the gda2.0-* packages.

%package -n	%{libname}
Summary:	GNU Data Access Development
Group:		System/Libraries

%description -n	%{libname}
This package contains a shared library for %{name}.

%package -n	%{libreport}
Summary:	GNU Data Access Development
Group:		System/Libraries
Conflicts:	%{_lib}gda2.0_2 < 3.1.5-16

%description -n	%{libreport}
This package contains a shared library for %{name}.

%package -n	%{libsql}
Summary:	GNU Data Access Development
Group:		System/Libraries
Conflicts:	%{_lib}gda2.0_2 < 3.1.5-16

%description -n	%{libsql}
This package contains a shared library for %{name}.

%package -n	%{libxslt}
Summary:	GNU Data Access Development
Group:		System/Libraries

%description -n	%{libxslt}
This package contains a shared library for %{name}.

%package -n	%{devname}
Summary:	GNU Data Access Development
Group:		Development/Databases
Requires:	%{libname} = %{version}
Requires:	%{libreport} = %{version}-%{release}
Requires:	%{libsql} = %{version}-%{release}
Requires:	%{libxslt} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the development files for %{name}.

%package	postgres
Summary:	GDA PostgreSQL Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	postgres
This package includes the GDA PostgreSQL provider

%package	mysql
Summary:	GDA MySQL Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	mysql
This package includes the GDA MySQL provider

%package	odbc
Summary:	GDA ODBC Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	odbc
This package includes the GDA ODBC provider.

%package	ldap
Summary:	GDA LDAP Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	ldap
This package includes the GDA LDAP provider.

%package	bdb
Summary:	GDA Berkeley Database Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	bdb
This package includes the GDA Berkeley Database provider.

%if %{build_freetds}
%package	freetds
Summary:	GDA FreeTDS Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	freetds
This package includes the GDA FreeTDS provider.
%endif

%if %{build_mdb}
%package	mdb
Summary:	GDA MDB Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	mdb
This package includes the GDA MDB provider, which can access
Microsoft Access databases.
%endif

%package	xbase
Summary:	GDA xbase Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	xbase
This package includes the GDA Xbase provider.

%package	sqlite
Summary:	GDA sqlite Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	sqlite
This package includes the GDA sqlite provider

%prep
%setup -qn %{pkgname}-%{version}
%apply_patches
autoreconf -fi

%build
export LIBS=-ldl
%configure2_5x \
%if %{build_mysql}
	--with-mysql=yes \
%endif
%if !%{build_freetds}
	--with-tds=no \
%endif
%if !%{build_mdb}
	--with-mdb=no \
%endif
	--without-firebird \
	--disable-static

make

%install
%makeinstall_std

%find_lang %{pkgname}-%{api} --with-gnome

%check
#make check

%files -f %{pkgname}-%{api}.lang
%doc AUTHORS COPYING README
%dir %{_sysconfdir}/libgda-%{api}
%config(noreplace) %{_sysconfdir}/libgda-%{api}/sales_test.db
%config(noreplace) %{_sysconfdir}/libgda-%{api}/config
%{_bindir}/*
%dir %{_libdir}/libgda-%{api}
%dir %{_libdir}/libgda-%{api}/providers
%{_datadir}/libgda-%{api}
%{_mandir}/man?/*

%files -n %{libname}
%{_libdir}/libgda-%{api}.so.%{major}*

%files -n %{libreport}
%{_libdir}/libgda-report-%{api}.so.%{major}*

%files -n %{libsql}
%{_libdir}/libgdasql-%{api}.so.%{major}*

%files -n %{libxslt}
%{_libdir}/libgda-xslt-%{api}.so.%{xsltmaj}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/libgda-%{api}/
%{_libdir}/libgda-%{api}.so
%{_libdir}/libgda-report-%{api}.so
%{_libdir}/libgdasql-%{api}.so
%{_libdir}/libgda-xslt-%{api}.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files sqlite
%{_libdir}/libgda-%{api}/providers/libgda-sqlite.so

%files postgres
%{_libdir}/libgda-%{api}/providers/libgda-postgres.so

%files odbc
%{_libdir}/libgda-%{api}/providers/libgda-odbc.so

%files ldap
%{_libdir}/libgda-%{api}/providers/libgda-ldap.so

%files bdb
%{_libdir}/libgda-%{api}/providers/libgda-bdb.so

%if %{build_mysql}
%files mysql
%{_libdir}/libgda-%{api}/providers/libgda-mysql.so
%endif

%if %{build_freetds}
%files freetds
%{_libdir}/libgda-%{api}/providers/libgda-freetds.so
%endif

%if %{build_mdb}
%files mdb
%{_libdir}/libgda-%{api}/providers/libgda-mdb.so
%endif

%files xbase
%{_libdir}/libgda-%{api}/providers/libgda-xbase.so

