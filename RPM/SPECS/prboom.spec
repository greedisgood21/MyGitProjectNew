Name:           prboom
Version:        2.6.2
Release:        1%{?dist}
Summary:        PrBoom is a DOOM game engine that focuses on accuracy and performance
Group:          Games

License:        GPLv2
URL:            http://prboom.sourceforge.net/
Source0:        prboom-%{version}.tar.gz

BuildRequires:  gcc, make, automake, autoconf, SDL-devel, SDL_mixer-devel, SDL_net-devel
Requires:       SDL, SDL_mixer, SDL_net

%description
PrBoom is a DOOM game engine that focuses on accuracy and performance. It is based on
the original DOOM source code and supports modern systems.

%prep
%setup -q

%build
./autogen.sh
./configure --prefix=/usr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
/usr/bin/prboom
/usr/share/games/prboom/*
/usr/share/doc/prboom/*
/usr/share/man/man6/prboom.6.gz

%changelog
* Tue Oct 10 2023 Your Name <your.email@example.com> - 2.6.2-1
- Initial package for PrBoom 2.6.2
