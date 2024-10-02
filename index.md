---
layout: base
permalink: /

# ===================================================================
# openrazer.github.io uses a single page design.
# Content is specified as YAML (or Markdown) below.
# ===================================================================

# Navigation to quick jump to sections
navigation:
    - label: Features
      icon: fa fa-star
      href: '#features'

    - label: Devices
      icon: fa fa-keyboard
      href: '#devices'

    - label: Download
      icon: fa fa-download
      href: '#download'

    - label: Apps
      icon: fa fa-puzzle-piece
      href: '#apps'

    - label: Links
      icon: fa-brands fa-github
      href: '#project'

about:
    - title: What is OpenRazer?
      description: 'A community-led effort to support Razer peripherals on Linux. It consists of:'
      items:
        - title: Linux Kernel Module
          icon: fa-brands fa-linux
          description: Written in C and configured to rebuild on kernel updates using DKMS
        - title: Daemon
          icon: fa fa-gears
          description: Adding persistence support, battery notifications and turning off brightness on screensaver
        - title: Python Library
          icon: fa-brands fa-python
          description: >-
            For integration with scripts and [applications ↓](#apps)

    - title: Features
      description: 'OpenRazer enables Razer-specific capabilities of the hardware, such as:'
      items:
        - title: Hardware Effects
          icon: fa-brands fa-usb
          description: Exposing what's supported on the firmware. Devices retain settings across power cycles*
        - title: Device Functions
          icon: fa fa-computer-mouse
          description: Such as brightness, DPI** and polling rate
        - title: Addressable RGB
          icon: fa-regular fa-lightbulb
          description: Enable custom lighting via software
      footnotes:
        - '* Not supported by all hardware. Using the device on a computer running Razer Synapse will reset this state.'
        - '** Most mice DPI hardware buttons are not intercepted and continue to use default behaviour/range.'

devices:
    intro: Originally written for the BlackWidow Chroma, the driver is now compatible with 123 Razer peripherals.
    keyboard:
    mice:
    mousemat:
    keypads: A third party application is required for key rebinding, such as [input-remapper](https://github.com/sezanzeb/input-remapper/).
    headset: Only lighting features are supported. OpenRazer doesn't provide additional audio features.
    other: Webcams with no lighting features are not supported. Try [cameractrls](https://github.com/soyersoyer/cameractrls) to enable HDR and related functionality.

download: >-
    Before installing the driver, you'll need to install a kernel headers package that matches your kernel version.
    This is because the driver is "out-of-tree" and needs to be compiled for the kernel (using DKMS).


    For example, Arch has `linux-headers` and `linux-lts-headers`.
    Other distros like Ubuntu/Debian may install them automatically, as the packaging system "recommends" the necessary package.


    Before using OpenRazer, you'll need to add your user to the `plugdev` group. In most distributions, this is:

        sudo gpasswd -a $USER plugdev


    After following the instructions for your distribution below, a **system reboot** is essential
    so the driver and user group permissions take effect. **Secure boot** may
    need to be disabled due to the nature of the driver being unsigned.


    After successful installation, reboot the computer and [pick an application](#apps) to interact with the driver.

# ===================================================================
# For new lines, use double newlines.
# For code indents, use 4 spaces. Backticks (`) are not supported.
# ===================================================================

instructions:
    - title: Officially Supported
      summary: We provide packages for these distros.
      distros:
        - name: Debian
          id: debian
          logo: /img/distros/debian.svg
          instructions: >-
            Starting with Debian 10, OpenRazer is available from the [official repositories](https://packages.debian.org/search?keywords=openrazer).
            However, you may need to install our package if your device was added in a newer version.


            Instructions and downloadable builds for Debian are
            [available from the openSUSE Build Service.](https://software.opensuse.org/download.html?project=hardware%3Arazer&package=openrazer-meta)

        - name: Fedora
          id: fedora
          logo: /img/distros/fedora.svg
          instructions: >-

            Due to a bug in Fedora, the wrong kernel headers (`kernel-debug-devel`) may be installed and cause OpenRazer to fail installation.
            To fix this, you must install `kernel-devel` explictly before installing OpenRazer:

                sudo dnf install kernel-devel


            For Fedora run the following:

                sudo dnf config-manager --add-repo https://download.opensuse.org/repositories/hardware:/razer/Fedora_$(rpm -E %fedora)/hardware:razer.repo

                sudo dnf install openrazer-meta


            For Fedora Rawhide run the following:

                sudo dnf config-manager --add-repo https://download.opensuse.org/repositories/hardware:/razer/Fedora_Rawhide/hardware:razer.repo

                sudo dnf install openrazer-meta

        - name: Mageia
          id: mageia
          logo: /img/distros/mageia.svg
          instructions: >-
            Instructions and downloadable builds for Mageia are
            [available on openSUSE Build Service.](https://software.opensuse.org/download.html?project=hardware%3Arazer&package=openrazer-meta)

        - name: openSUSE
          id: opensuse
          logo: /img/distros/opensuse.svg
          instructions: >-
            Instructions and downloadable builds for openSUSE are
            [available on openSUSE Build Service.](https://software.opensuse.org/download.html?project=hardware%3Arazer&package=openrazer-meta)

        - name: Ubuntu / Linux Mint / elementaryOS / Pop!_OS / Zorin OS
          id: ubuntu
          logo: /img/distros/ubuntu.svg
          instructions: >-
            Starting with 20.04, OpenRazer is available from the [official repositories](https://packages.ubuntu.com/search?keywords=openrazer).
            However, you may need to install our package if your device was added in a newer version.


            elementaryOS users need to install a prerequisite first:

                sudo apt install software-properties-gtk

            To install the latest release, add this PPA:

                sudo add-apt-repository ppa:openrazer/stable

            Or for latest development builds:

                sudo add-apt-repository ppa:openrazer/daily

            After adding the PPA, install the packages:

                sudo apt update
                sudo apt install openrazer-meta

            If you get dependency errors when trying to install the driver packages, please make sure that you have enabled the "universe" repository in **Software & Updates**.

    - title: Community Supported
      summary: Packaged and supported by the wider community.
      distros:
        - name: Alpine Linux
          id: alpine
          logo: /img/distros/alpine.svg
          instructions: >-
            Packages are available from the [community repositories](https://pkgs.alpinelinux.org/packages?name=openrazer).


                doas apk add openrazer openrazer-src


            The kernel modules are built via [akms](https://github.com/jirutka/akms).

        - name: Arch Linux / Manjaro
          id: arch
          logo: /img/distros/arch.svg
          instructions: >-
            Packages are available from the [official repos](https://archlinux.org/packages/?q=openrazer).


                sudo pacman -S openrazer-daemon


            If you need the latest development builds, install [openrazer-meta-git](https://aur.archlinux.org/packages/openrazer-meta-git/) package from the AUR.

        - name: Gentoo
          id: gentoo
          logo: /img/distros/gentoo.svg
          instructions: >-
            An ebuild is available, to install:

                emerge -av --autounmask sys-apps/openrazer

        - name: NixOS
          id: nixos
          logo: /img/distros/nixos.svg
          instructions: >-
            To enable the OpenRazer module in NixOS, add this snippet to your `configuration.nix`:

                hardware.openrazer.enable = true;

            In order to run the openrazer-daemon service, your user needs to be part of the `openrazer` group.

                hardware.openrazer.users = ["<name>?"];

            Rebuild your NixOS configuration:

                sudo nixos-rebuild switch

            Alternately, use `nix-shell`:

                nix-shell -p openrazer-daemon

        - name: Solus
          id: solus
          logo: /img/distros/solus.svg
          instructions: >-
            An eopkg is available, to install:

                sudo eopkg install openrazer

        - name: Slackware
          id: slackware
          logo: /img/distros/slackware.svg
          instructions: >-
            Packages are available at the following URLs:

            * <https://www.slackbuilds.org/repository/15.0/system/openrazer-kernel/>

            * <https://www.slackbuilds.org/repository/15.0/system/openrazer-daemon/>


            For details on how to install, see the [SlackBuilds.org FAQ](https://www.slackbuilds.org/howto/).

        - name: Void Linux
          id: voidlinux
          logo: /img/distros/voidlinux.svg
          instructions: >-
            Void Linux provides these packages:

            * [openrazer-meta](https://github.com/void-linux/void-packages/blob/master/srcpkgs/openrazer-meta/template)

            * [openrazer-daemon](https://github.com/void-linux/void-packages/blob/master/srcpkgs/openrazer-daemon)

            * [openrazer-driver-dkms](https://github.com/void-linux/void-packages/blob/master/srcpkgs/openrazer-driver-dkms)

            * [python3-openrazer](https://github.com/void-linux/void-packages/blob/master/srcpkgs/python3-openrazer)


            To install:

                xbps-install -S openrazer-meta

apps:
    intro: 'These projects integrate with OpenRazer:'
    featured:
        - name: Polychromatic
          url: https://polychromatic.app/
          logo: /img/apps/polychromatic.svg
          technologies:
            - Python, Qt 6
            - Tray Applet

        - name: RazerGenie
          url: https://github.com/z3ntu/RazerGenie
          logo: /img/logo.svg
          technologies:
            - Qt 5

        - name: Snake
          url: http://bithatch.co.uk/snake.html
          logo: /img/apps/snake.png
          technologies:
            - Java

        - name: razerCommander
          url: https://gitlab.com/gabmus/razerCommander
          logo: /img/apps/razerCommander.png
          technologies:
            - GTK

        - name: razer-cli
          url: https://github.com/lolei/razer-cli
          logo: fa fa-terminal
          technologies:
            - Python

links:
    - label: View Source
      icon: fa-brands fa-github
      url: https://github.com/openrazer/openrazer

    - label: Troubleshoot
      icon: fa-regular fa-question-circle
      url: https://github.com/openrazer/openrazer/wiki/Troubleshooting

    - label: Issues
      icon: fa fa-exclamation-circle
      url: https://github.com/openrazer/openrazer/issues

    - label: Wiki
      icon: fa fa-book-open
      url: https://github.com/openrazer/openrazer/wiki

    - label: Contributors
      icon: fa fa-users
      url: https://github.com/openrazer/openrazer/graphs/contributors

footer:
    legal:
        This project is licensed under the [GPLv2](https://github.com/openrazer/openrazer/blob/master/LICENSES/GPL-2.0-or-later.txt).
        It is <em>not affiliated</em> with [Razer Inc](https://www.razerzone.com/).

    credits:
        Brought to you by [Luca Weiss](https://github.com/z3ntu), plus the help of many
        [contributors](https://github.com/openrazer/openrazer/graphs/contributors) and testers.

    social:
        - tooltip: '@OpenRazer on GitHub'
          icon: github
          url: https://github.com/openrazer/openrazer

        - tooltip: OpenRazer Telegram Group
          icon: telegram
          url: https://t.me/joinchat/AMhHjj9Txhkhn8JM5_LeMg

        - tooltip: '@OpenRazer on Mastodon'
          icon: mastodon
          url: https://fosstodon.org/@openrazer

        - tooltip: '#openrazer:matrix.org'
          icon: /img/social/matrix.svg
          url: https://matrix.to/#/#openrazer:matrix.org
---
