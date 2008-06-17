%define 	name gda2.0
%define		pkgname libgda
%define dirver 3.0

%define 	build_mysql 1
%{?_with_mysql: %global build_mysql 1}
%define		build_freetds 0
%{?_with_freetds: %global build_freetds 1}
%define		build_mdb 0
%{?_with_mdb: %global build_mdb 1}

%define api 3.0
%define oname gda
%define	major 3
%define libname	%mklibname %{oname}%{api}_ %major 
%define libnamedev	%mklibname -d %{oname}%{api}
%define basiclibname	%mklibname %{oname}%{api}

%define old_package	%mklibname gda2.0_ 3 
Summary:	GNU Data Access
Name: 		%{name}
Version: 3.1.2
Release: %mkrel 3
License: 	GPL/LGPL
Group: 		Databases
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
#gw add missing man pages
Patch: libgda-3.0.0-man.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	bison
BuildRequires:	db4-devel
BuildRequires:	flex
BuildRequires:	gdbm-devel
BuildRequires:	glib2-devel
BuildRequires:	libxslt-devel >= 1.0.9
BuildRequires:	ncurses-devel
BuildRequires:  openldap2-devel
#gw for the intltool scripts:
BuildRequires:	perl-XML-Parser
BuildRequires:	popt-devel
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
BuildRequires:	scrollkeeper
BuildRequires:  sqlite3-devel
BuildRequires:  unixODBC-devel
BuildRequires: automake1.8 intltool
BuildRequires: libcheck-devel
%if %build_mysql
BuildRequires:	MySQL-devel
%endif
%if %build_freetds
BuildRequires:	freetds-devel
%endif
%if %build_mdb
BuildRequires:	libmdbtools-devel
%endif
BuildRequires:	gtk-doc
#Requires(post):		scrollkeeper
#Requires(postun):	scrollkeeper
Conflicts:	gda < 0.3
URL: 		http://www.gnome-db.org/

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
Group: 		System/Libraries
Provides:	%basiclibname = %{version}-%{release}
Requires:	%name >= %version
Provides: %name-sqlite = %version
Obsoletes: gda3.0-sqlite

%description -n	%{libname}
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.


%package -n	%{libnamedev}
Summary:	GNU Data Access Development
Group: 		Development/Databases
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	libxslt-devel >= 1.0.9
Obsoletes: %mklibname -d %{oname}%{api}_ %major
%define _requires_exceptions ^devel.libgda-

%description -n	%{libnamedev}
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

%package	postgres
Summary:	GDA PostgreSQL Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	postgres
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA PostgreSQL provider

%package	mysql
Summary:	GDA MySQL Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	mysql
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA MySQL provider

%package	odbc
Summary:	GDA ODBC Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	odbc
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA ODBC provider.

%package	ldap
Summary:	GDA LDAP Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	ldap
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA LDAP provider.

%package	bdb
Summary:	GDA Berkeley Database Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	bdb
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA Berkeley Database provider.

%if %build_freetds
%package	freetds
Summary:	GDA FreeTDS Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	freetds
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA FreeTDS provider.
%endif

%package	mdb
Summary:	GDA MDB Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	mdb
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA MDB provider, which can access
Microsoft Access databases.


%package	xbase
Summary:	GDA xbase Provider
Group:		Databases
Requires:	%{name} = %{version}
BuildRequires:	libxbase-devel

%description	xbase
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

%prep
%setup -q -n %{pkgname}-%{version}
%patch -p1 -b .man

# (Abel) mkinstalldirs is not distributed, this is temp hack
cat > mkinstalldirs << _EOF_
#!/bin/sh
exec mkdir -p "\$@"
_EOF_
chmod +x mkinstalldirs

autoconf

%build
%configure2_5x \
%if %build_mysql
	--with-mysql=yes \
%endif
%if !%build_freetds
	--with-tds=no \
%endif
%if !%build_mdb
	--with-mdb=no \
%endif
	--with-sqlite=%_prefix \
	--without-firebird

make

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std}

# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_libdir}/libgda-%dirver/providers/*.{a,la}

%{find_lang} %{pkgname}-%{api} --with-gnome

%check
#make check

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif
		  
%files -f %{pkgname}-%{api}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_bindir}/*
%dir %{_sysconfdir}/libgda-%dirver
%config(noreplace) %_sysconfdir/libgda-%dirver/sales_test.db
%config(noreplace) %{_sysconfdir}/libgda-%dirver/config
%{_datadir}/libgda-%dirver
%{_mandir}/man?/*
%dir %{_libdir}/libgda-%dirver
%dir %{_libdir}/libgda-%dirver/providers

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/libgda-%{api}.so.%{major}*
%{_libdir}/libgda-report-%{api}.so.%{major}*
%{_libdir}/libgdasql-%{api}.so.%{major}*
%_libdir/libgda-xslt-%{api}.so.0*
%{_libdir}/libgda-%dirver/providers/libgda-sqlite.so


%files -n %{libnamedev}
%defattr(-, root, root)
%doc %_datadir/gtk-doc/html/libgda-3.0/
%{_libdir}/libgda-%{api}.so
%{_libdir}/libgda-report-%{api}.so
%{_libdir}/libgdasql-%{api}.so
%_libdir/libgda-xslt-%{api}.so
%{_libdir}/lib*.a
%attr(644,root,root) %{_libdir}/lib*.la
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files postgres
%defattr(-, root, root)
%{_libdir}/libgda-%dirver/providers/libgda-postgres.so

%files odbc
%defattr(-, root, root)
%{_libdir}/libgda-%dirver/providers/libgda-odbc.so

%files ldap
%defattr(-, root, root)
%{_libdir}/libgda-%dirver/providers/libgda-ldap.so

%files bdb
%defattr(-, root, root)
%{_libdir}/libgda-%dirver/providers/libgda-bdb.so

%if %build_mysql
%files mysql
%defattr(-, root, root)
%{_libdir}/libgda-%dirver/providers/libgda-mysql.so
%endif

%if %build_freetds
%files freetds
%defattr(-, root, root)
%{_libdir}/libgda-%dirver/providers/libgda-freetds.so
%endif

%if %build_mdb
%files mdb
%defattr(-, root, root)
%{_libdir}/libgda-%dirver/providers/libgda-mdb.so
%endif

%files xbase
%defattr(-, root, root)
%{_libdir}/libgda-%dirver/providers/libgda-xbase.so
