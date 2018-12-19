# MindEd
Editor for programming LEGO Mindstorms NXT and EV3 bricks with NXC/C4EV3

MindEd is a GTK+ Editor for programming LEGO:registered: Mindstorms bricks.
Not eXactly C ([NXC](http://bricxcc.sourceforge.net)) and Next Byte Codes(NBC)
is used for NXT-bricks, EVC aka [C4EV3](https://github.com/c4ev3) and
armgcc-cross-compiler is used for EV3-bricks. Both work with unmodified bricks,
no need to install foreign firmware or alternative operating systems.  
MindEd offers Syntaxhighlightning, Autocompletion, API help ...  
MindEd also compiles and uploads your programs to your brick over USB.

## Requirements

For Debian-based systems MindEd requires the following packages to run:

1. python3.5
1. gir1.2-gtk-3.0 (>=3.18)
1. gir1.2-gudev-1.0
1. python3-usb
1. nbc, if you want to program NXT-brick
1. gcc-arm-linux-gnueabi, if you want to program EV3-brick

## Installation

For systemwide installation click [releases](https://github.com/bsellentin/minded/releases)
and download the latest version as deb-package. In the download-folder execute as *root*:

    $ dpkg -i minded-*X.Y.Z*_amd64.deb

Advantage: you get mime-support - clicking on a brick-file in the filemanager opens
MindEd. If something goes wrong, open a terminal and start by typing

    $ minded --debug

For local installation clone the repository:

    $ git clone --recursive https://github.com/bsellentin/minded.git
    $ cd minded

As *root* copy the nxc- and evc.language-specs to gtksourceview-3.0/language-specs-folder
and the minded-style-file to the gtksourceview-3.0/styles-folder.

    minded$ cp *.lang /usr/share/gtksourceview-3.0/language-specs/
    minded$ cp minded.xml /usr/share/gtksourceview-3.0/styles/

Now run Minded as normal user.

    minded$ python3 minded.py --debug


MindEd looks for the NBC compiler in `/usr/bin` and in `/usr/local/bin`.
GCC cross-compiler is searched in `/usr/bin` as `arm-linux-gnueabi-gcc-?`.
Other names and paths can be set in settings-menu or dconf-editor -> org -> gge-em -> minded.

EV3-brick needs firmware >= 1.03.

## Documentation

A first draft of an [EVC-tutorial](docs/evc_tutorial.md) in german language is in the docs folder.
