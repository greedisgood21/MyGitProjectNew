Name:           chocolate-doom
Version:        3.0.1
Release:        1%{?dist}
Summary:        Historically accurate DOOM/Heretic/Hexen/Strife port
Group:		Games
License:        GPLv2+
URL:            https://github.com/chocolate-doom/chocolate-doom
Source0:        chocolate-doom-%{version}.tar.gz

BuildRequires:  autoconf automake libtool libSDL2-devel libSDL2_mixer-devel libSDL2_net-devel python3
Requires:       libSDL2 libSDL2_mixer libSDL2_net

%description
Chocolate Doom is a minimalist, historically accurate DOOM engine with support for Heretic, Hexen and Strife.

%package heretic
Summary:        Heretic support for Chocolate-Doom
Requires:       %{name} = %{version}-%{release}
Group:		Games
%description heretic
Heretic game support for Chocolate-Doom.

%package hexen
Summary:        Hexen support for Chocolate-Doom
Requires:       %{name} = %{version}-%{release}
Group:		Games
%description hexen
Hexen game support for Chocolate-Doom.

%package strife
Summary:        Strife support for Chocolate-Doom
Requires:       %{name} = %{version}-%{release}
Group:		Games
%description strife
Strife game support for Chocolate-Doom.

%prep
%setup -q -n chocolate-doom

%build
# Генерация скриптов сборки
./autogen.sh

# Сборка всех компонентов
./configure --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --enable-doom \
    --enable-heretic \
    --enable-hexen \
    --enable-strife

make %{?_smp_mflags}

%install
# Установка всех компонентов
make install DESTDIR=%{buildroot}

%files
%{_bindir}/chocolate-doom
%{_mandir}/man6/chocolate-doom.6*

%files heretic
%{_bindir}/chocolate-heretic
%{_mandir}/man6/chocolate-heretic.6*

%files hexen
%{_bindir}/chocolate-hexen
%{_mandir}/man6/chocolate-hexen.6*

%files strife
%{_bindir}/chocolate-strife
%{_mandir}/man6/chocolate-strife.6*

%changelog
* Wed Nov 01 2023 Your Name <your.email@example.com> - 3.0.1-1
- Fixed multi-binary packaging
