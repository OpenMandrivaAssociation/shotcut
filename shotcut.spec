%define debug_package %{nil}

Name: shotcut
Version: 22.09.23
Release: 1
Source0: https://github.com/mltframework/shotcut/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix for building with OpenGL ES. OMV ARM64 use QT compiled with GLES instead desktop OpenGL. So we need force GLES on Shotcut too.
%ifarch %{arm} %{armx}
Patch0:   shotcut-allow-building-with-opengles.patch
%endif
#Patch1:   shotcut-libdir.patch
Summary: A video editor
URL: http://shotcut.org/
License: GPLv3
Group: Graphical desktop/KDE

BuildRequires: cmake
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5OpenGL)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickWidgets)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5WebKit)
BuildRequires: cmake(Qt5WebKitWidgets)
BuildRequires: cmake(Qt5WebSockets)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5XkbCommonSupport)
BuildRequires: pkgconfig(mlt++-7)
BuildRequires: pkgconfig(mlt-framework-7)
BuildRequires: qt5-linguist-tools
BuildRequires: ffmpeg-devel
BuildRequires: ladspa-devel
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(frei0r)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(vpx)
BuildRequires: qt5-qtquick-private-devel
BuildRequires: qt5-qtqmlmodels-private-devel
BuildRequires: qt5-qtqml-private-devel
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: qt5-qttools
BuildRequires: qt5-qtbase-devel
BuildRequires:  pkgconfig(sdl2)

Requires:	frei0r-plugins
Requires:	ladspa
Requires: lame
Requires:	mlt >= 6.10.0
Requires:	qt5-qtquickcontrols
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtmultimedia
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
