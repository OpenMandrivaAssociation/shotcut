%define debug_package %{nil}

Name: shotcut
Version: 23.07.18
Release: 1
Source0: https://github.com/mltframework/shotcut/archive/v%{version}/%{name}-%{version}.tar.gz

Summary: A video editor
URL: http://shotcut.org/
License: GPLv3
Group: Graphical desktop/KDE

BuildRequires: cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Test)
#BuildRequires: cmake(Qt5WebKit)
#BuildRequires: cmake(Qt5WebKitWidgets)
BuildRequires: cmake(Qt6WebSockets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6XkbCommonSupport)
BuildRequires: pkgconfig(mlt++-7)
BuildRequires: pkgconfig(mlt-framework-7)
#BuildRequires: qt5-linguist-tools
BuildRequires: ffmpeg-devel
BuildRequires: ladspa-devel
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(frei0r)
BuildRequires: pkgconfig(Qt6Concurrent)
BuildRequires: pkgconfig(Qt6PrintSupport)
#BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(vpx)
#BuildRequires: qt5-qtquick-private-devel
#BuildRequires: qt5-qtqmlmodels-private-devel
#BuildRequires: qt5-qtqml-private-devel
#BuildRequires: pkgconfig(Qt5WebKitWidgets)
#BuildRequires: qt5-qttools
#BuildRequires: qt5-qtbase-devel
BuildRequires:  pkgconfig(sdl2)

Requires:	frei0r-plugins
Requires:	ladspa
Requires: lame
Requires:	mlt >= 6.10.0
#Requires:	qt5-qtquickcontrols
#Requires: qt5-qtgraphicaleffects
#Requires: qt5-qtmultimedia
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
