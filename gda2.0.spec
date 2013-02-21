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
%define	major 2
%define xsltmajor 0
%define libname	%mklibname %{oname}%{api}_ %major 
%define libnamexslt %mklibname gda-xslt %{api} %xsltmajor 
%define libnamedev	%mklibname -d %{oname}%{api}
%define basiclibname	%mklibname %{oname}%{api}

%define old_package	%mklibname gda3.0_ 3 
Summary:	GNU Data Access
Name: 		%{name}
Version: 3.1.5
Release: 15
License: 	GPLv2+ and LGPLv2+
Group: 		Databases
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
Patch0: libgda-3.1.5-format-strings.patch
Patch1: libgda-3.1.5-fix-install.patch
Patch2: libgda-3.1.5-xbase64.patch
Patch3: libgda-3.1.5-lib64.patch
Patch4: libgda-3.1.5-glib-includes.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	flex
BuildRequires:	gdbm-devel
BuildRequires:	glib2-devel
BuildRequires:	libxslt-devel >= 1.0.9
BuildRequires:	ncurses-devel
BuildRequires:  openldap-devel
BuildRequires:	intltool
BuildRequires:	popt-devel
BuildRequires:	postgresql-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:	readline-devel
BuildRequires:	scrollkeeper
BuildRequires:  sqlite3-devel
BuildRequires:  unixODBC-devel
BuildRequires: automake1.8
BuildRequires: libcheck-devel
%if %build_mysql
BuildRequires:	mysql-devel
%endif
%if %build_freetds
BuildRequires:	freetds-devel
%endif
%if %build_mdb
BuildRequires:	libmdbtools-devel
%endif
BuildRequires:	gtk-doc
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
Conflicts:	%old_package
Requires:	%name-sqlite >= %version

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

%package -n	%{libnamexslt}
Summary:	GNU Data Access Development
Group: 		System/Libraries
Requires:	%name >= %version
Conflicts:	%old_package
Conflicts: %libname < 3.1.5-3mdv

%description -n	%{libnamexslt}
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
Requires:	%{libnamexslt} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d %{oname}%{api}_ %major

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

%if %build_mdb
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
%endif

%package	xbase
Summary:	GDA xbase Provider
Group:		Databases
Requires:	%{name} = %{version}
BuildRequires:	xbase-devel

%description	xbase
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.


%package	sqlite
Summary:	GDA sqlite Provider
Group:		Databases
Requires:	%{name} = %{version}
Obsoletes:      gda3.0-sqlite
Conflicts:	%libname < 3.1.5-3mdv
Conflicts:	%old_package

%description	sqlite
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA sqlite provider

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p1

%build
autoreconf -fi
export LIBS=-ldl
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
	--without-firebird \
	--disable-static

make

%install
rm -rf %{buildroot}

%{makeinstall_std}

# remove unneeded files
rm -f %{buildroot}%{_libdir}/libgda-%dirver/providers/*.{a,la}

%{find_lang} %{pkgname}-%{api} --with-gnome

%check
#make check

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%post -n %{libnamexslt} -p /sbin/ldconfig
%postun -n %{libnamexslt} -p /sbin/ldconfig
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

%files -n %{libnamexslt}
%defattr(-, root, root)
%_libdir/libgda-xslt-%{api}.so.%{xsltmajor}*

%files -n %{libnamedev}
%defattr(-, root, root)
%doc %_datadir/gtk-doc/html/libgda-3.0/
%{_libdir}/libgda-%{api}.so
%{_libdir}/libgda-report-%{api}.so
%{_libdir}/libgdasql-%{api}.so
%_libdir/libgda-xslt-%{api}.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files sqlite
%defattr(-, root, root)
%{_libdir}/libgda-%dirver/providers/libgda-sqlite.so

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


%changelog
* Thu May 10 2012 Crispin Boylan <crisb@mandriva.org> 3.1.5-14
+ Revision: 797932
- Rebuild

  + Götz Waschk <waschk@mandriva.org>
    - update patch 0
    - patch for glib includes

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for new unixODBC (second try)
    - rebuilt for new unixODBC

* Mon Apr 11 2011 Funda Wang <fwang@mandriva.org> 3.1.5-11
+ Revision: 652511
- fix build under lib64 arch

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 3.1.5-10
+ Revision: 645746
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 3.1.5-9mdv2011.0
+ Revision: 626997
- rebuilt against mysql-5.5.8 libs, again

* Mon Dec 27 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1.5-8mdv2011.0
+ Revision: 625418
- rebuilt against mysql-5.5.8 libs

* Sun Nov 14 2010 Funda Wang <fwang@mandriva.org> 3.1.5-7mdv2011.0
+ Revision: 597457
- build with xbase664

* Wed Feb 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1.5-7mdv2010.1
+ Revision: 507028
- rebuild

* Thu Dec 31 2009 Funda Wang <fwang@mandriva.org> 3.1.5-6mdv2010.1
+ Revision: 484333
- rebuild for db4.8

* Mon Oct 05 2009 Funda Wang <fwang@mandriva.org> 3.1.5-5mdv2010.0
+ Revision: 453790
- fix installation

* Wed Feb 25 2009 Götz Waschk <waschk@mandriva.org> 3.1.5-5mdv2009.1
+ Revision: 344824
- fix format strings
- disable static libs

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild for new libreadline

  + Oden Eriksson <oeriksson@mandriva.com>
    - use lowercase mysql-devel

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.1.5-4mdv2009.1
+ Revision: 311199
- rebuilt against mysql-5.1.30 libs

* Tue Aug 12 2008 Götz Waschk <waschk@mandriva.org> 3.1.5-3mdv2009.0
+ Revision: 271114
- split library package in a sane way
- update build deps

* Wed Aug 06 2008 Götz Waschk <waschk@mandriva.org> 3.1.5-2mdv2009.0
+ Revision: 264228
- add conflict with old library package

* Wed Aug 06 2008 Götz Waschk <waschk@mandriva.org> 3.1.5-1mdv2009.0
+ Revision: 264182
- new version
- new major
- drop patch
- fix build
- update license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.1.2-3mdv2009.0
+ Revision: 222542
- fix build when %%build_freetds is not set (missing %%files for subpackage)
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 22 2007 Götz Waschk <waschk@mandriva.org> 3.1.2-2mdv2008.1
+ Revision: 136827
- rebuild for libdb 4.6

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - do not package big ChangeLog

* Thu Oct 25 2007 Götz Waschk <waschk@mandriva.org> 3.1.2-1mdv2008.1
+ Revision: 102208
- new version
- update file list

* Sun Sep 02 2007 Götz Waschk <waschk@mandriva.org> 3.1.1-2mdv2008.0
+ Revision: 78284
- move sqlite provider to the lib package
- move libs to the library package
- filter out wrong deps from the devel package

* Sun Sep 02 2007 Götz Waschk <waschk@mandriva.org> 3.1.1-1mdv2008.0
+ Revision: 78213
- new version
- new devel name

* Thu May 10 2007 Götz Waschk <waschk@mandriva.org> 3.0.1-1mdv2008.0
+ Revision: 25874
- new version

* Tue Apr 24 2007 Götz Waschk <waschk@mandriva.org> 3.0.0-1mdv2008.0
+ Revision: 17749
- new version
- patch to add missing man pages

* Wed Apr 18 2007 Götz Waschk <waschk@mandriva.org> 2.99.6-1mdv2008.0
+ Revision: 14425
- disable the checks again, they fail in the iurt chroot
- new version
- drop sharp bindings
- drop patches
- enable checks


* Tue Feb 13 2007 Götz Waschk <waschk@mandriva.org> 2.99.5-1mdv2007.1
+ Revision: 120313
- new version
- fix build of gda-sharp
- update file list

* Sat Jan 27 2007 Götz Waschk <waschk@mandriva.org> 2.99.3-2mdv2007.1
+ Revision: 114386
- fix devel deps

* Tue Jan 23 2007 Götz Waschk <waschk@mandriva.org> 2.99.3-1mdv2007.1
+ Revision: 112598
- new version
- update file list
- drop obsolete library packages now all libs share one major version

* Tue Jan 02 2007 Götz Waschk <waschk@mandriva.org> 2.99.2-1mdv2007.1
+ Revision: 103091
- new version
- new API version
- add sqltransaction package

* Tue Nov 21 2006 Götz Waschk <waschk@mandriva.org> 1.99.1-1mdv2007.1
+ Revision: 85946
- Import gda2.0

* Tue Nov 21 2006 G�tz Waschk <waschk@mandriva.org> 1.99.1-1mdv2007.1
- New version 1.99.1
- fix file list

* Tue Sep 05 2006 Oden Eriksson <oeriksson@mandriva.com> 1.9.102-1mdv2007.0
- rebuilt against MySQL-5.0.24a-1mdv2007.0 due to ABI changes

* Thu Aug 03 2006 G�tz Waschk <waschk@mandriva.org> 1.9.102-2mdv2007.0
- enable mono

* Fri Mar 24 2006 G�tz Waschk <waschk@mandriva.org> 1.9.102-1mdk
- update file list
- New release 1.9.102

* Wed Feb 15 2006 G�tz Waschk <waschk@mandriva.org> 1.9.100-1mdk
- new libname
- add sharp subpackage
- drop patches
- new version

* Thu Feb 02 2006 G�tz Waschk <waschk@mandriva.org> 1.2.3-6mdk
- fix buildrequires

* Wed Feb 01 2006 G�tz Waschk <waschk@mandriva.org> 1.2.3-5mdk
- fix post scripts

* Wed Feb 01 2006 G�tz Waschk <waschk@mandriva.org> 1.2.3-4mdk
- split out libgdasql

* Thu Nov 17 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-3mdk
- rebuilt against openssl-0.9.8a

* Wed Nov 09 2005 G�tz Waschk <waschk@mandriva.org> 1.2.3-2mdk
- replace prereq
- fix buildrequires

* Tue Nov 01 2005 Götz Waschk <waschk@mandriva.org> 1.2.3-1mdk
- New release 1.2.3

* Sun Oct 30 2005 G�tz Waschk <waschk@mandriva.org> 1.2.2-4mdk
- fix deps and description

* Tue Oct 11 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.2.2-3mdk
- ppc64 is a lib64 arch too

* Wed Aug 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2mdk
- rebuilt against new openldap-2.3.6 libs

* Wed Jun 15 2005 G�tz Waschk <waschk@mandriva.org> 1.2.2-1mdk
- New release 1.2.2

* Thu May 12 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.2.1-2mdk
- Rebuild for postgresql-devel 8.0.2

* Thu Mar 03 2005 G�tz Waschk <waschk@linux-mandrake.com> 1.2.1-1mdk
- fix sqlite deps
- drop patch 0
- New release 1.2.1

* Fri Feb 04 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.2.0-5mdk
- rebuild for ldap2.2_7

* Thu Jan 20 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.0-4mdk
- rebuild for new readline

* Wed Dec 29 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.0-3mdk 
- Fix conflicts

* Tue Dec 28 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.0-2mdk
- add conflict to ease upgrade

* Tue Dec 28 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.0-1mdk
- major 3
- add xbase package
- New release 1.2.0

* Wed Nov 10 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1.99-1mdk
- disable parallel build
- New release 1.1.99

* Thu Sep 30 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.1.6-2mdk
- lib64 & 64-bit fixes

* Mon Aug 16 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.1.6-1mdk
- New release 1.1.6

* Fri Jul 23 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.1.5-1mdk
- New release 1.1.5

* Thu Jun 10 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1.4-1mdk
- reenable mysql
- New release 1.1.4

* Sat Jun 05 2004 <lmontel@n2.mandrakesoft.com> 1.1.3-3mdk
- Rebuild

* Sat Jun 05 2004 Abel Cheung <deaddog@deaddog.org> 1.1.3-2mdk
- gda-config-tool is not devel stuff
- Fix provides

* Sat Jun 05 2004 Abel Cheung <deaddog@deaddog.org> 1.1.3-1mdk
- New version
- Allows building freetds and mdb backend via build switch
- Parallel make works again

* Fri May 14 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.1.2-2mdk
- sync with AMD64 branch
- Disable freetds support

* Wed Apr 28 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1.2-1mdk
- fix buildrequires
- new version

