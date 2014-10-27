Summary:	Qt Bindings for SMOKE
Name:		smokeqt
Version:	4.14.2
Release:	2
Epoch:		1
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		http://www.kde.org
%define is_beta %(if test `echo %version |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	qscintilla-qt4-devel
BuildRequires:	smokegen-devel >= 1:%{version}
BuildRequires:	pkgconfig(qimageblitz) < 5.0.0

%description
Qt Bindings for SMOKE (Scripting Meta Object Kompiler Engine)

#-----------------------------------------------------------------------------

%define smokeqtcore_major 3
%define libsmokeqtcore %mklibname smokeqtcore %{smokeqtcore_major}

%package -n %{libsmokeqtcore}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtcore}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtcore}
%{_kde_libdir}/libsmokeqtcore.so.%{smokeqtcore_major}*

#-----------------------------------------------------------------------------

%define smokeqtdeclarative_major 3
%define libsmokeqtdeclarative %mklibname smokeqtdeclarative %{smokeqtdeclarative_major}

%package -n %{libsmokeqtdeclarative}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtdeclarative}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtdeclarative}
%{_kde_libdir}/libsmokeqtdeclarative.so.%{smokeqtdeclarative_major}*

#-----------------------------------------------------------------------------

%define smokeqtdbus_major 3
%define libsmokeqtdbus %mklibname smokeqtdbus %{smokeqtdbus_major}

%package -n   %{libsmokeqtdbus}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtdbus}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtdbus}
%{_kde_libdir}/libsmokeqtdbus.so.%{smokeqtdbus_major}*

#------------------------------------------------------------

%define smokeqthelp_major 3
%define libsmokeqthelp %mklibname smokeqthelp %{smokeqthelp_major}

%package -n %{libsmokeqthelp}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqthelp}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqthelp}
%{_kde_libdir}/libsmokeqthelp.so.%{smokeqthelp_major}*

#-----------------------------------------------------------------------------

%define smokeqtgui_major 3
%define libsmokeqtgui %mklibname smokeqtgui %{smokeqtgui_major}

%package -n %{libsmokeqtgui}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtgui}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtgui}
%{_kde_libdir}/libsmokeqtgui.so.%{smokeqtgui_major}*

#-----------------------------------------------------------------------------

%define smokeqtmultimedia_major 3
%define libsmokeqtmultimedia %mklibname smokeqtmultimedia %{smokeqtmultimedia_major}

%package -n %{libsmokeqtmultimedia}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtmultimedia}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtmultimedia}
%{_kde_libdir}/libsmokeqtmultimedia.so.%{smokeqtmultimedia_major}*

#-----------------------------------------------------------------------------

%define smokeqtnetwork_major 3
%define libsmokeqtnetwork %mklibname smokeqtnetwork %{smokeqtnetwork_major}

%package -n %{libsmokeqtnetwork}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtnetwork}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtnetwork}
%{_kde_libdir}/libsmokeqtnetwork.so.%{smokeqtnetwork_major}*

#-----------------------------------------------------------------------------

%define smokeqtopengl_major 3
%define libsmokeqtopengl %mklibname smokeqtopengl %{smokeqtopengl_major}

%package -n %{libsmokeqtopengl}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtopengl}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtopengl}
%{_kde_libdir}/libsmokeqtopengl.so.%{smokeqtopengl_major}*

#-----------------------------------------------------------------------------

%define smokeqtsql_major 3
%define libsmokeqtsql %mklibname smokeqtsql %{smokeqtsql_major}

%package -n %{libsmokeqtsql}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtsql}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtsql}
%{_kde_libdir}/libsmokeqtsql.so.%{smokeqtsql_major}*

#-----------------------------------------------------------------------------

%define smokeqtsvg_major 3
%define libsmokeqtsvg %mklibname smokeqtsvg %{smokeqtsvg_major}

%package -n %{libsmokeqtsvg}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtsvg}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtsvg}
%{_kde_libdir}/libsmokeqtsvg.so.%{smokeqtsvg_major}*

#-----------------------------------------------------------------------------

%define smokeqtxml_major 3
%define libsmokeqtxml %mklibname smokeqtxml %{smokeqtxml_major}

%package -n %{libsmokeqtxml}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtxml}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtxml}
%{_kde_libdir}/libsmokeqtxml.so.%{smokeqtxml_major}*

#-----------------------------------------------------------------------------

%define smokeqtxmlpatterns_major 3
%define libsmokeqtxmlpatterns %mklibname smokeqtxmlpatterns %{smokeqtxmlpatterns_major}

%package -n %{libsmokeqtxmlpatterns}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtxmlpatterns}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtxmlpatterns}
%{_kde_libdir}/libsmokeqtxmlpatterns.so.%{smokeqtxmlpatterns_major}*

#-----------------------------------------------------------------------------

%define smokephonon_major 3
%define libsmokephonon %mklibname smokephonon %{smokephonon_major}

%package -n %{libsmokephonon}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokephonon}
Phonon binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokephonon}
%{_kde_libdir}/libsmokephonon.so.%{smokephonon_major}*

#-----------------------------------------------------------------------------

%define smokeqtuitools_major 3
%define libsmokeqtuitools %mklibname smokeqtuitools %{smokeqtuitools_major}

%package -n %{libsmokeqtuitools}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtuitools}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtuitools}
%{_kde_libdir}/libsmokeqtuitools.so.%{smokeqtuitools_major}*

#-----------------------------------------------------------------------------

%define smokeqtwebkit_major 3
%define libsmokeqtwebkit %mklibname smokeqtwebkit %{smokeqtwebkit_major}

%package -n %{libsmokeqtwebkit}
Summary:	Qt webkit binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtwebkit}
Qt webkit binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtwebkit}
%{_kde_libdir}/libsmokeqtwebkit.so.%{smokeqtwebkit_major}*

#-----------------------------------------------------------------------------

%define smokeqimageblitz_major 3
%define libsmokeqimageblitz %mklibname smokeqimageblitz %{smokeqimageblitz_major}

%package -n %{libsmokeqimageblitz}
Summary:	Qimageblitz binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqimageblitz}
Qimageblitz binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqimageblitz}
%{_kde_libdir}/libsmokeqimageblitz.so.%{smokeqimageblitz_major}*

#-----------------------------------------------------------------------------

%define smokeqsci_major 3
%define libsmokeqsci %mklibname smokeqsci %{smokeqsci_major}

%package -n %{libsmokeqsci}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqsci}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqsci}
%{_kde_libdir}/libsmokeqsci.so.%{smokeqsci_major}*

#------------------------------------------------------------

%define libsmokeqtscript_major 3
%define libsmokeqtscript %mklibname smokeqtscript %{libsmokeqtscript_major}

%package -n %{libsmokeqtscript}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqtscript}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtscript}
%{_kde_libdir}/libsmokeqtscript.so.%{libsmokeqtscript_major}*

#------------------------------------------------------------

%define libsmokeqttest_major 3
%define libsmokeqttest %mklibname smokeqttest %{libsmokeqttest_major}

%package -n %{libsmokeqttest}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqttest}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqttest}
%{_kde_libdir}/libsmokeqttest.so.%{libsmokeqttest_major}*

#------------------------------------------------------------

%define libsmokeqt3support_major 3
%define libsmokeqt3support %mklibname smokeqt3support %{libsmokeqt3support_major}

%package -n %{libsmokeqt3support}
Summary:	Qt binding library for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeqt3support}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqt3support}
%{_kde_libdir}/libsmokeqt3support.so.%{libsmokeqt3support_major}*

#------------------------------------------------------------

%package devel
Summary:	Header files for %{name}
Group:		Development/KDE and Qt
Conflicts:	smoke4-devel < 1:4.6.90
Requires:	kdelibs4-devel >= 2:%{version}
Requires:	smokegen-devel >= 1:%{version}
Requires:	pkgconfig(qimageblitz)
Requires:	qscintilla-qt4-devel
Requires:	%{libsmokeqimageblitz} = %{EVRD}
Requires:	%{libsmokeqsci} = %{EVRD}
Requires:	%{libsmokeqt3support} = %{EVRD}
Requires:	%{libsmokeqtcore} = %{EVRD}
Requires:	%{libsmokeqtdbus} = %{EVRD}
Requires:	%{libsmokeqtdeclarative} = %{EVRD}
Requires:	%{libsmokeqtgui} = %{EVRD}
Requires:	%{libsmokeqthelp} = %{EVRD}
Requires:	%{libsmokeqtmultimedia} = %{EVRD}
Requires:	%{libsmokeqtnetwork} = %{EVRD}
Requires:	%{libsmokeqtopengl} = %{EVRD}
Requires:	%{libsmokeqtscript} = %{EVRD}
Requires:	%{libsmokeqtsql} = %{EVRD}
Requires:	%{libsmokeqtsvg} = %{EVRD}
Requires:	%{libsmokeqttest} = %{EVRD}
Requires:	%{libsmokeqtuitools} = %{EVRD}
Requires:	%{libsmokeqtwebkit} = %{EVRD}
Requires:	%{libsmokeqtxmlpatterns} = %{EVRD}
Requires:	%{libsmokeqtxml} = %{EVRD}
Requires:	%{libsmokephonon} = %{EVRD}

%description devel
Devel headers for %{name}

%files devel
%{_kde_includedir}/smoke/phonon_smoke.h
%{_kde_includedir}/smoke/qimageblitz_smoke.h
%{_kde_includedir}/smoke/qsci_smoke.h
%{_kde_includedir}/smoke/qt3support_smoke.h
%{_kde_includedir}/smoke/qtcore_smoke.h
%{_kde_includedir}/smoke/qtdbus_smoke.h
%{_kde_includedir}/smoke/qtdeclarative_smoke.h
%{_kde_includedir}/smoke/qtgui_smoke.h
%{_kde_includedir}/smoke/qthelp_smoke.h
%{_kde_includedir}/smoke/qtmultimedia_smoke.h
%{_kde_includedir}/smoke/qtnetwork_smoke.h
%{_kde_includedir}/smoke/qtopengl_smoke.h
%{_kde_includedir}/smoke/qtscript_smoke.h
%{_kde_includedir}/smoke/qtsql_smoke.h
%{_kde_includedir}/smoke/qtsvg_smoke.h
%{_kde_includedir}/smoke/qttest_smoke.h
%{_kde_includedir}/smoke/qtuitools_smoke.h
%{_kde_includedir}/smoke/qtwebkit_smoke.h
%{_kde_includedir}/smoke/qtxml_smoke.h
%{_kde_includedir}/smoke/qtxmlpatterns_smoke.h
%{_kde_libdir}/libsmokephonon.so
%{_kde_libdir}/libsmokeqimageblitz.so
%{_kde_libdir}/libsmokeqsci.so
%{_kde_libdir}/libsmokeqt3support.so
%{_kde_libdir}/libsmokeqtcore.so
%{_kde_libdir}/libsmokeqtdbus.so
%{_kde_libdir}/libsmokeqtdeclarative.so
%{_kde_libdir}/libsmokeqtgui.so
%{_kde_libdir}/libsmokeqthelp.so
%{_kde_libdir}/libsmokeqtmultimedia.so
%{_kde_libdir}/libsmokeqtnetwork.so
%{_kde_libdir}/libsmokeqtopengl.so
%{_kde_libdir}/libsmokeqtscript.so
%{_kde_libdir}/libsmokeqtsql.so
%{_kde_libdir}/libsmokeqtsvg.so
%{_kde_libdir}/libsmokeqttest.so
%{_kde_libdir}/libsmokeqtuitools.so
%{_kde_libdir}/libsmokeqtwebkit.so
%{_kde_libdir}/libsmokeqtxml.so
%{_kde_libdir}/libsmokeqtxmlpatterns.so
%{_kde_datadir}/smokegen/qt-config.xml
%{_kde_datadir}/smokegen/qtdefines
%{_kde_datadir}/smoke/*.txt

#------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Mon Oct 27 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-2
- Use pkgconfig(qimageblitz) < 5.0.0 to force Qt4 version

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Sun Jul 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95
- Update files

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.1mib2010.2
+ Revision: 762507
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762507
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758092
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 744571
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 739326
- New upstream tarball $NEW_VERSION

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 731844
- New upstream tarball 4.7.80

* Wed Sep 07 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 698650
- Fix BR
- imported package smokeqt

