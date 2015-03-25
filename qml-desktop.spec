%define debug_package %nil
%define snap	20150325

Summary:	QML Desktop
Name:		qml-desktop
Version:	0.0.0
Release:	0.%{snap}.1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/qml-desktop
# git clone https://github.com/papyros/qml-desktop.git
# git archive --format=tar --prefix qml-desktop-0.0.0-$(date +%Y%m%d)/ HEAD | xz -vf > qml-desktop-0.0.0-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}-%{snap}.tar.xz
Patch0:		alsa-lib-linkage-fix.patch
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gio-2.0)

%description
A C++ plugin for QML to access desktop features

%prep
%setup -qn %{name}-%{version}-%{snap}
%apply_patches

%build
%qmake_qt5
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_qt5_libdir}/qt5/qml/Material/*
