%global debug_package %{nil}

Name:           gnome-network-displays
Version:        0.99.0
Release:        1%{?dist}
Summary:        Screencasting for GNOME

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-network-displays
Source0:        https://gitlab.gnome.org/GNOME/gnome-network-displays/-/archive/%{version}/gnome-network-displays-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  gstreamer1-rtsp-server-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  avahi-client-devel
BuildRequires:  avahi-gobject-devel
BuildRequires:  gtk3-devel
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  libpulseaudio-devel
BuildRequires:  protobuf-c-devel
BuildRequires:  json-glib-devel
BuildRequires:  libsoup3-devel
BuildRequires:  libportal-gtk4-devel
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  appstream

Requires:       gstreamer1-plugins-bad-free
Requires:       gstreamer1-plugins-good
Requires:       NetworkManager

%description
Screencasting for GNOME. Supports the Miracast and Chromecast protocols
for casting your desktop to a remote display.

%prep
%autosetup

%build
meson setup builddir --prefix=/usr
ninja -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%{_bindir}/gnome-network-displays
%{_bindir}/gnome-network-displays-daemon
%{_libexecdir}/gnome-network-displays-stream
%{_datadir}/applications/org.gnome.NetworkDisplays.desktop
%{_datadir}/metainfo/org.gnome.NetworkDisplays.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.NetworkDisplays.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.NetworkDisplays-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/gnome-network-displays.mo
%{_prefix}/lib/firewalld/zones/P2P-WiFi-Display.xml

%changelog
* Wed Jul 30 2026 Fame <fame@famelinuxpc> - 0.99.0-1
- Initial RPM package release
