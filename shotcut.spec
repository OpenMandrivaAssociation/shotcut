%define debug_package %{nil}

Name: shotcut
Version: 17.03
Release: 2
Source0: https://github.com/mltframework/shotcut/archive/v%{version}.tar.gz
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
BuildRequires: cmake(Qt5WebKitWidgets)
BuildRequires: cmake(Qt5WebSockets)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: pkgconfig(mlt++)
BuildRequires: pkgconfig(mlt-framework)

%description
A video editor

%prep
%setup -q
qmake-qt5 PREFIX=%{_prefix}

%build
%make

%install
%makeinstall INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/shotcut
%{_datadir}/shotcut
