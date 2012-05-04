Name:    smokeqt
Summary: Qt Bindings for SMOKE
Version: 4.8.3
Release: 1
Epoch:   1
Group:   Development/KDE and Qt
License: GPL
URL:     http://www.kde.org
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.xz

BuildRequires: smokegen-devel >= 1:%version
BuildRequires: qimageblitz-devel
BuildRequires: qscintilla-qt4-devel 

%description
Qt Bindings for SMOKE (Scripting Meta Object Kompiler Engine)

#-----------------------------------------------------------------------------

%define smokeqtcore_major 3
%define libsmokeqtcore %mklibname smokeqtcore %{smokeqtcore_major}

%package -n   %{libsmokeqtcore}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtcore}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtcore}
%_kde_libdir/libsmokeqtcore.so.%{smokeqtcore_major}*

#-----------------------------------------------------------------------------

%define smokeqtdeclarative_major 3
%define libsmokeqtdeclarative %mklibname smokeqtdeclarative %{smokeqtdeclarative_major}

%package -n   %{libsmokeqtdeclarative}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtdeclarative}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtdeclarative}
%_kde_libdir/libsmokeqtdeclarative.so.%{smokeqtdeclarative_major}*

#-----------------------------------------------------------------------------

%define smokeqtdbus_major 3
%define libsmokeqtdbus %mklibname smokeqtdbus %{smokeqtdbus_major}

%package -n   %{libsmokeqtdbus}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtdbus}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtdbus}

%_kde_libdir/libsmokeqtdbus.so.%{smokeqtdbus_major}*

#------------------------------------------------------------

%define smokeqthelp_major 3
%define libsmokeqthelp %mklibname smokeqthelp %{smokeqthelp_major}

%package -n %{libsmokeqthelp}
Summary: Qt binding library for SMOKE
Group: Development/KDE and Qt

%description -n %{libsmokeqthelp}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqthelp}

%_kde_libdir/libsmokeqthelp.so.%{smokeqthelp_major}*

#-----------------------------------------------------------------------------

%define smokeqtgui_major 3
%define libsmokeqtgui %mklibname smokeqtgui %{smokeqtgui_major}

%package -n   %{libsmokeqtgui}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtgui}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtgui}

%_kde_libdir/libsmokeqtgui.so.%{smokeqtgui_major}*

#-----------------------------------------------------------------------------

%define smokeqtmultimedia_major 3
%define libsmokeqtmultimedia %mklibname smokeqtmultimedia %{smokeqtmultimedia_major}

%package -n   %{libsmokeqtmultimedia}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtmultimedia}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtmultimedia}

%_kde_libdir/libsmokeqtmultimedia.so.%{smokeqtmultimedia_major}*

#-----------------------------------------------------------------------------

%define smokeqtnetwork_major 3
%define libsmokeqtnetwork %mklibname smokeqtnetwork %{smokeqtnetwork_major}

%package -n   %{libsmokeqtnetwork}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtnetwork}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtnetwork}

%_kde_libdir/libsmokeqtnetwork.so.%{smokeqtnetwork_major}*

#-----------------------------------------------------------------------------

%define smokeqtopengl_major 3
%define libsmokeqtopengl %mklibname smokeqtopengl %{smokeqtopengl_major}

%package -n   %{libsmokeqtopengl}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtopengl}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtopengl}

%_kde_libdir/libsmokeqtopengl.so.%{smokeqtopengl_major}*

#-----------------------------------------------------------------------------

%define smokeqtsql_major 3
%define libsmokeqtsql %mklibname smokeqtsql %{smokeqtsql_major}

%package -n   %{libsmokeqtsql}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtsql}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtsql}

%_kde_libdir/libsmokeqtsql.so.%{smokeqtsql_major}*

#-----------------------------------------------------------------------------

%define smokeqtsvg_major 3
%define libsmokeqtsvg %mklibname smokeqtsvg %{smokeqtsvg_major}

%package -n   %{libsmokeqtsvg}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtsvg}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtsvg}

%_kde_libdir/libsmokeqtsvg.so.%{smokeqtsvg_major}*

#-----------------------------------------------------------------------------

%define smokeqtxml_major 3
%define libsmokeqtxml %mklibname smokeqtxml %{smokeqtxml_major}

%package -n   %{libsmokeqtxml}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtxml}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtxml}

%_kde_libdir/libsmokeqtxml.so.%{smokeqtxml_major}*

#-----------------------------------------------------------------------------

%define smokeqtxmlpatterns_major 3
%define libsmokeqtxmlpatterns %mklibname smokeqtxmlpatterns %{smokeqtxmlpatterns_major}

%package -n   %{libsmokeqtxmlpatterns}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtxmlpatterns}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtxmlpatterns}

%_kde_libdir/libsmokeqtxmlpatterns.so.%{smokeqtxmlpatterns_major}*

#-----------------------------------------------------------------------------

%define smokephonon_major 3
%define libsmokephonon %mklibname smokephonon %{smokephonon_major}

%package -n   %{libsmokephonon}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokephonon}
Phonon binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokephonon}

%_kde_libdir/libsmokephonon.so.%{smokephonon_major}*

#-----------------------------------------------------------------------------

%define smokeqtuitools_major 3
%define libsmokeqtuitools %mklibname smokeqtuitools %{smokeqtuitools_major}

%package -n   %{libsmokeqtuitools}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtuitools}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtuitools}

%_kde_libdir/libsmokeqtuitools.so.%{smokeqtuitools_major}*

#-----------------------------------------------------------------------------

%define smokeqtwebkit_major 3
%define libsmokeqtwebkit %mklibname smokeqtwebkit %{smokeqtwebkit_major}

%package -n   %{libsmokeqtwebkit}
Summary:      Qt webkit binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqtwebkit}
Qt webkit binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtwebkit}

%_kde_libdir/libsmokeqtwebkit.so.%{smokeqtwebkit_major}*

#-----------------------------------------------------------------------------

%define smokeqimageblitz_major 3
%define libsmokeqimageblitz %mklibname smokeqimageblitz %{smokeqimageblitz_major}

%package -n   %{libsmokeqimageblitz}
Summary:      Qimageblitz binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqimageblitz}
Qimageblitz binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqimageblitz}

%_kde_libdir/libsmokeqimageblitz.so.%{smokeqimageblitz_major}*

#-----------------------------------------------------------------------------

%define smokeqsci_major 3
%define libsmokeqsci %mklibname smokeqsci %{smokeqsci_major}

%package -n   %{libsmokeqsci}
Summary:      Qt binding library for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeqsci}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqsci}

%_kde_libdir/libsmokeqsci.so.%{smokeqsci_major}*

#------------------------------------------------------------

%define libsmokeqtscript_major 3
%define libsmokeqtscript %mklibname smokeqtscript %{libsmokeqtscript_major}

%package -n %{libsmokeqtscript}
Summary: Qt binding library for SMOKE
Group: Development/KDE and Qt

%description -n %{libsmokeqtscript}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqtscript}

%_kde_libdir/libsmokeqtscript.so.%{libsmokeqtscript_major}*

#------------------------------------------------------------

%define libsmokeqttest_major 3
%define libsmokeqttest %mklibname smokeqttest %{libsmokeqttest_major}

%package -n %{libsmokeqttest}
Summary: Qt binding library for SMOKE
Group: Development/KDE and Qt

%description -n %{libsmokeqttest}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqttest}

%_kde_libdir/libsmokeqttest.so.%{libsmokeqttest_major}*

#------------------------------------------------------------

%define libsmokeqt3support_major 3
%define libsmokeqt3support %mklibname smokeqt3support %{libsmokeqt3support_major}

%package -n %{libsmokeqt3support}
Summary: Qt binding library for SMOKE
Group: Development/KDE and Qt

%description -n %{libsmokeqt3support}
Qt binding library for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeqt3support}

%_kde_libdir/libsmokeqt3support.so.%{libsmokeqt3support_major}*

#------------------------------------------------------------

%package devel
Summary: Header files for %{name}
Group: Development/KDE and Qt
Conflicts: smoke4-devel < 1:4.6.90
Requires: kdelibs4-devel >= 2:%version
Requires: smokegen-devel >= 1:%version
Requires: pkgconfig(qimageblitz)
Requires: qscintilla-qt4-devel 
Requires: %{libsmokeqimageblitz} = %epoch:%version-%release
Requires: %{libsmokeqsci} = %epoch:%version-%release
Requires: %{libsmokeqt3support} = %epoch:%version-%release
Requires: %{libsmokeqtcore} = %epoch:%version-%release
Requires: %{libsmokeqtdbus} = %epoch:%version-%release
Requires: %{libsmokeqtdeclarative} = %epoch:%version-%release
Requires: %{libsmokeqtgui} = %epoch:%version-%release
Requires: %{libsmokeqthelp} = %epoch:%version-%release
Requires: %{libsmokeqtmultimedia} = %epoch:%version-%release
Requires: %{libsmokeqtnetwork} = %epoch:%version-%release
Requires: %{libsmokeqtopengl} = %epoch:%version-%release
Requires: %{libsmokeqtscript} = %epoch:%version-%release
Requires: %{libsmokeqtsql} = %epoch:%version-%release
Requires: %{libsmokeqtsvg} = %epoch:%version-%release
Requires: %{libsmokeqttest} = %epoch:%version-%release
Requires: %{libsmokeqtuitools} = %epoch:%version-%release
Requires: %{libsmokeqtwebkit} = %epoch:%version-%release
Requires: %{libsmokeqtxmlpatterns} = %epoch:%version-%release
Requires: %{libsmokeqtxml} = %epoch:%version-%release
Requires: %{libsmokephonon} = %epoch:%version-%release

%description devel
Devel headers for %{name}

%files devel

%_kde_includedir/smoke/phonon_smoke.h
%_kde_includedir/smoke/qimageblitz_smoke.h
%_kde_includedir/smoke/qsci_smoke.h
%_kde_includedir/smoke/qt3support_smoke.h
%_kde_includedir/smoke/qtcore_smoke.h
%_kde_includedir/smoke/qtdbus_smoke.h
%_kde_includedir/smoke/qtdeclarative_smoke.h
%_kde_includedir/smoke/qtgui_smoke.h
%_kde_includedir/smoke/qthelp_smoke.h
%_kde_includedir/smoke/qtmultimedia_smoke.h
%_kde_includedir/smoke/qtnetwork_smoke.h
%_kde_includedir/smoke/qtopengl_smoke.h
%_kde_includedir/smoke/qtscript_smoke.h
%_kde_includedir/smoke/qtsql_smoke.h
%_kde_includedir/smoke/qtsvg_smoke.h
%_kde_includedir/smoke/qttest_smoke.h
%_kde_includedir/smoke/qtuitools_smoke.h
%_kde_includedir/smoke/qtwebkit_smoke.h
%_kde_includedir/smoke/qtxml_smoke.h
%_kde_includedir/smoke/qtxmlpatterns_smoke.h
%_kde_libdir/libsmokephonon.so
%_kde_libdir/libsmokeqimageblitz.so
%_kde_libdir/libsmokeqsci.so
%_kde_libdir/libsmokeqt3support.so
%_kde_libdir/libsmokeqtcore.so
%_kde_libdir/libsmokeqtdbus.so
%_kde_libdir/libsmokeqtdeclarative.so
%_kde_libdir/libsmokeqtgui.so
%_kde_libdir/libsmokeqthelp.so
%_kde_libdir/libsmokeqtmultimedia.so
%_kde_libdir/libsmokeqtnetwork.so
%_kde_libdir/libsmokeqtopengl.so
%_kde_libdir/libsmokeqtscript.so
%_kde_libdir/libsmokeqtsql.so
%_kde_libdir/libsmokeqtsvg.so
%_kde_libdir/libsmokeqttest.so
%_kde_libdir/libsmokeqtuitools.so
%_kde_libdir/libsmokeqtwebkit.so
%_kde_libdir/libsmokeqtxml.so
%_kde_libdir/libsmokeqtxmlpatterns.so
%_kde_datadir/smokegen/qt-config.xml
%_kde_datadir/smokegen/qtdefines

#------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build

