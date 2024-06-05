%define debug_package %{nil}

Name: shotcut
Version: 24.06.02
Release: 1
Source0: https://github.com/mltframework/shotcut/archive/v%{version}/%{name}-%{version}.tar.gz

Summary: A video editor
URL: https://shotcut.org/
License: GPLv3
Group: Graphical desktop/KDE

BuildRequires: cmake
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: qt6-qttools-linguist
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: qt6-qtmultimedia-gstreamer
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6OpenGLWidgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Charts)
BuildRequires: qt6-qtbase-sql-firebird
BuildRequires: qt6-qtbase-sql-mariadb
BuildRequires: qt6-qtbase-sql-odbc
BuildRequires: qt6-qtbase-sql-postgresql
BuildRequires: qt6-qtbase-sql-sqlite
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6WebSockets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: pkgconfig(mlt++-7)
BuildRequires: pkgconfig(mlt-framework-7)
BuildRequires: ffmpeg-devel
BuildRequires: ladspa-devel
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(frei0r)
BuildRequires: pkgconfig(Qt6Concurrent)
BuildRequires: pkgconfig(Qt6PrintSupport)
BuildRequires: pkgconfig(vpx)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:	cmake(VulkanHeaders)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(xkbcommon)

Requires:	frei0r-plugins
Requires:	ladspa
Requires: lame
Requires:	mlt >= 6.10.0
#Requires:	qt6-qtquickcontrols2
#Requires: qt5-qtgraphicaleffects
Requires: qml(QtMultimedia)
Recommends: gstreamer1.0-plugins-bad
Recommends: gstreamer1.0-plugins-good
Recommends: gstreamer1.0-plugins-ugly

%description
A video editor

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build


%files
%doc COPYING README.md
%{_bindir}/%{name}
%{_libdir}/libCuteLogger.so
%{_datadir}/%{name}
%{_datadir}/applications/org.%{name}.Shotcut.desktop
%{_datadir}/metainfo/org.%{name}.Shotcut.metainfo.xml
%{_datadir}/mime/packages/org.%{name}.Shotcut.xml
%{_iconsdir}/hicolor/*/apps/org.%{name}.Shotcut.png
%{_mandir}/man1/%{name}.1*
