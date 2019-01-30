%define debug_package %{nil}

Name: shotcut
Version: 19.01.24
Release: 1
Source0: https://github.com/mltframework/shotcut/archive/v%{version}/%{name}-%{version}.tar.gz
Summary: A video editor
URL: http://shotcut.org/
License: GPLv3
Group: Graphical desktop/KDE
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5OpenGL)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickWidgets)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5WebKit)
BuildRequires: cmake(Qt5WebKitWidgets)
BuildRequires: cmake(Qt5WebSockets)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: pkgconfig(mlt++)
BuildRequires: pkgconfig(mlt-framework)
BuildRequires: qt5-linguist-tools
BuildRequires: ffmpeg-devel
BuildRequires: ladspa-devel
BuildRequires: pkgconfig(frei0r)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(vpx)
BuildRequires: qt5-qtquick-private-devel
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: qt5-qttools
BuildRequires: qt5-qtbase-devel


Requires:	frei0r-plugins
Requires:	ladspa
Requires:	mlt >= 6.10.0
Requires:	qt5-qtquickcontrols-qml


%description
A video editor


%prep
%setup -q
qmake-qt5 PREFIX=%{_prefix}

%build
%make

lrelease-qt5 translations/*.ts

%install
%makeinstall INSTALL_ROOT=%{buildroot}


%files
%doc COPYING README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/org.%{name}.Shotcut.desktop
%{_datadir}/metainfo/org.%{name}.Shotcut.appdata.xml
%{_datadir}/mime/packages/org.%{name}.Shotcut.xml
%{_iconsdir}/hicolor/*/apps/org.%{name}.Shotcut.png
%{_mandir}/man1/%{name}.1*
