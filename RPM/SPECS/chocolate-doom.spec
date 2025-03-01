Name:           chocolate-doom
Version:        3.0.1
Release:        1%{?dist}
Summary:        Chocolate Doom is a port of the classic DOOM game
Group:		Games
License:        GPLv2
URL:            https://www.chocolate-doom.org/
Source0:        chocolate-doom-%{version}.tar.gz

BuildRequires:  gcc, make, automake, autoconf, libSDL2-devel, libSDL2_mixer-devel, libSDL2_net-devel
Requires:       libSDL2, libsSDL2_mixer, SDL2_net

%description
Chocolate Doom is a port of the classic DOOM game that aims to reproduce the
original experience as closely as possible.

%prep
%setup -q -n chocolate-doom

%build
./autogen.sh
./configure --prefix=/usr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
/usr/bin/chocolate-doom
/usr/bin/chocolate-doom-setup
/usr/bin/chocolate-heretic
/usr/bin/chocolate-heretic-setup
/usr/bin/chocolate-hexen
/usr/bin/chocolate-hexen-setup
/usr/bin/chocolate-server
/usr/bin/chocolate-strife
/usr/bin/chocolate-strife-setup

%changelog
* Tue Oct 10 2023 Your Name <your.email@example.com> - 3.0.1-1
- Initial package for Chocolate Doom 3.0.1

