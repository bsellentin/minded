# MindEd
Editor for programming LEGO Mindstorms NXT and EV3 bricks with NXC/C4EV3

MindEd is a GTK+ Editor for programming LEGO Mindstorms bricks.
Not eXactly C ([NXC](http://bricxcc.sourceforge.net)) and Next Byte Codes(NBC) is used for NXT-bricks,
EVC aka [C4EV3](https://github.com/c4ev3) and armgcc-cross-compiler is used for EV3-bricks. It
offers Syntaxhighlightning, Autocompletion, API help ...  
MindEd also compiles and uploads your programs to your brick over USB.

## Requirements

For Debian-based systems MindEd requires the following packages to run:

1. python3
1. gir1.2-gtk-3.0 (>=3.18)
1. gir1.2-gudev-1.0
1. python3-usb
1. nbc
1. gcc-arm-linux-gnueabi

## Don't Install

Not completed!

```$ git clone --recursive https://github.com/bsellentin/minded.git```

MindEd looks for the NBC compiler in ```/usr/bin``` and in ```/usr/local/bin```. GCC cross-compiler is searched
in ```/usr/bin``` as ```arm-linux-gnueabi-gcc-6``` (Debian) or ```arm-linux-gnueabi-gcc``` (Ubuntu). Other
names and paths can be set using dconf-editor -> org -> gge-em -> minded.

EV3 brick needs firmware > 1.01.

## Documentation

A first draft of an [EVC-tutorial](docs/evc_tutorial.md) in german language is in the docs folder.
