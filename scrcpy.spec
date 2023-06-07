Name: scrcpy
Version: 2.0
Release: alt1

Summary: Display and control your Android device

License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/Genymobile/scrcpy

Source: https://github.com/Genymobile/scrcpy/archive/v%version/%name-%version.tar.gz
# Source0-md5:	7aaf3494112e8127cbafddcacf04d53d
Source1: https://github.com/Genymobile/scrcpy/releases/download/v%version/%name-server-v%version
# Source1-md5:	5ea87ea427c3fd63965db46a18342794

BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: libSDL2-devel
BuildRequires: ffmpeg
BuildRequires: libusb-devel
BuildRequires: meson >= 1.1.1
BuildRequires: pkg-config
BuildRequires: rpm-build
BuildRequires: libavformat-devel
BuildRequires: libswresample-devel
BuildRequires: libavdevice-devel

Requires: libSDL2 >= 2.0.5
Requires: android-tools

%description
Display and control your Android device.

%package -n bash-completion-scrcpy
Summary: bash-completion for scrcpy
Group: Shells
Requires: %name = %version-%release
Requires: bash-completion
BuildArch: noarch

%description -n bash-completion-scrcpy
bash-completion for scrcpy.

%package -n zsh-completion-scrcpy
Summary: zsh-completion for scrcpy
Group: Shells
Requires: %name = %version-%release
Requires: zsh
BuildArch: noarch

%description -n zsh-completion-scrcpy
zsh-completion for scrcpy.

%prep
%setup

%build
%meson \
	-Dprebuilt_server=%SOURCE1

%meson_build

%install
%meson_install

%files
%attr(755,root,root) %_bindir/scrcpy
%dir %_datadir/scrcpy
%attr(755,root,root) %_datadir/scrcpy/scrcpy-server
%_desktopdir/scrcpy.desktop
%_desktopdir/scrcpy-console.desktop
%_iconsdir/hicolor/256x256/apps/scrcpy.png
%_man1dir/scrcpy.1*


%files -n bash-completion-scrcpy
%_datadir/bash-completion/completions/scrcpy

%files -n zsh-completion-scrcpy
%_datadir/zsh/site-functions/_scrcpy

%changelog
* Wed Jun 07 2023 Mikhail Tergoev <fidel@altlinux.org> 2.0-alt1
- initial build for ALT Sisyphus

* Tue Apr 11 2023 PLD Linux Team <feedback@pld-linux.org>
- For complete changelog see: http://git.pld-linux.org/?p=packages/scrcpy.git;a=log;h=master

* Sun Apr 09 2023 Jan Palus <atler@pld-linux.org> 4bba3df
- up to 2.0

* Fri Dec 30 2022 Jan Palus <atler@pld-linux.org> 35184ef
- new

