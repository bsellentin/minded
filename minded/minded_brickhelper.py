#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2017 Bernd Sellentin <sel@gge-em.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path
import os
import subprocess
import shlex
import struct
import hashlib
import re
import mmap
import contextlib

from minded.minded_widgets import CancellationWin

import logging
LOGGER = logging.getLogger(__name__)

class BrickHelper():
    '''
    Helper to put programms on brick
    '''

    def __init__(self, application):

        self.application = application
        self.procid = -1

    def nbc_proc(self, document, upload: bool = False):
        '''
        compile and upload file to NXT brick
        returns (error, msg)
        '''
        nbc_exec = self.application.settings.get_string('nbcpath')
        if not nbc_exec:
            return ('Error: 127', 'nbc-compiler not found')

        enhancedfw = self.application.settings.get_boolean('enhancedfw')
        if enhancedfw:
            nbc_exec = nbc_exec + ' -EF'
        LOGGER.debug('use enhancedfw: {}'.format(enhancedfw))

        if upload:
            # compile and upload
            nbc_opts = (' -d %s' % (shlex.quote(document.get_path())))
            LOGGER.debug('upload: {}'.format(nbc_opts))
        else:
            # compile only
            nbcout = str(Path(document.get_path()).with_suffix('.rxe'))
            LOGGER.debug('File to compile: {}'.format(document.get_path()))
            nbc_opts = (' -O=%s %s' % (shlex.quote(nbcout),
                                       shlex.quote(document.get_path())))

        # TODO: nbc dies silently if not enough free memory on brick
        # 1. compile
        # 2. check filesize
        # 3. check free memory
        #    name, host, signal_strength, user_flash = self.application.nxt_brick.get_device_info()
        # 4. nbc -b: treat input file as a binary file (don't compile it)
        #    nbc_opts = (' -b %s' % (shlex.quote(document.get_path())))
        #    Error: unexpected filetype specified (.rxe)

        # do it
        nbc_proc = subprocess.Popen(('%s %s' % (nbc_exec, nbc_opts)),
                                    shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, preexec_fn=os.setsid)

        self.procid = nbc_proc.pid
        LOGGER.debug('nbc_proc ID %s' % self.procid)

        cancel_win = CancellationWin(self, nbc_proc.pid)

        try:
            nbc_data = nbc_proc.communicate(timeout=30)
            # nbc_data[0]: stdout, nbc_data[1]: stderr
        except TimeoutExpired:
            nbc_proc.kill()
            nbc_data = nbc_proc.communicate()

        cancel_win.destroy()
        return (nbc_proc.returncode, nbc_data)


    def evc_proc(self, document, upload: bool = False):
        '''
        compile and upload file to EV3 brick
        param upload false = compile only
        returns (error, msg)
        '''

        prjname = Path(document.get_basename()).stem
        msg = ''

        gcc_err, msg = self.cross_compile(document)
        if gcc_err:
            # compilation failed
            return (gcc_err, msg)
        if upload:
            # make starter
            starter_err, starter_msg = self.mkstarter(document)
            msg += starter_msg
            if not starter_err:
                # upload starter
                filename = Path(document.get_parent(), prjname + '.rbf')
                errora, err_msg = self.ev3_upload(filename)
                msg += err_msg
                # upload executable
                filename = Path(document.get_parent(), prjname)
                errorb, err_msg = self.ev3_upload(filename)
                msg += err_msg

                if not errora and not errorb:
                    self.application.ev3_brick.play_sound('./ui/DownloadSucces')

        return (0, msg)

    def mkstarter(self, document):
        '''
        build rbf-starter-file, store local, upload later
        '''
        LOGGER.debug('building starter for: {}'.format(document.get_path()))

        prjname = Path(document.get_basename()).stem
        prjsstore = self.application.settings.get_string('prjsstore')
        prjpath = str(Path(prjsstore, prjname, prjname))
        LOGGER.debug('EV3-path: {}'.format(prjpath))

        magic = b'LEGO'
        before = b'\x68\x00\x01\x00\x00\x00\x00\x00\x1C\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x60\x80'
        after = b'\x44\x85\x82\xE8\x03\x40\x86\x40\x0A'

        size = len(magic) + 4 + len(before) + len(prjpath)+1 + len(after)

        cmd = b''.join([
            magic,
            struct.pack('I', size),
            before,
            str.encode(prjpath)+b'\x00',
            after
            ])

        starter = Path(document.get_path()).with_suffix('.rbf')
        try:
            starter.write_bytes(cmd)
            return (0, 'Build starter successfull\n')
        except OSError as err:
            return (1, 'OS error:{0}'.format(err))

    def cross_compile(self, document):
        '''
        cross-compile evc-file for EV3-brick, store local, upload later
        returns ()gcc_proc.returncode, msg)
        '''
        infile = document.get_path()

        # look for own headers
        headers = []
        pattern = re.compile(b'".*.h"')
        with open(infile, 'rb', 0) as file:
            with contextlib.closing(mmap.mmap(file.fileno(), 0, \
                access=mmap.ACCESS_READ)) as m:
                for match in pattern.findall(m):
                    myheader = match.decode()
                    if not 'ev3.h' in myheader:
                       # 1   :   -3
                       # "myheader.h"
                       myheader = str(Path(document.get_parent(),
                                      Path(myheader[1:-3] + '.evc')))
                       headers.append(myheader)

        LOGGER.debug('file to compile: {}'.format(infile))

        outfile = str(Path(document.get_parent(), Path(document.get_basename()).stem))
        LOGGER.debug('executable to write: {}'.format(outfile))

        cplusplus = self.application.settings.get_boolean('cplusplus')
        if cplusplus:
            arm_exec = self.application.settings.get_string('armgplusplus')
            if not arm_exec:
                return ('Error', 'C++-compiler not found')
            language = 'c++'
            arm_exec += ' -static-libstdc++'
        else:
            arm_exec = self.application.settings.get_string('armgcc')
            if not arm_exec:
                return ('Error', 'C-compiler not found')
            language = 'c'

        ldflags = ' -L' + self.application.settings.get_string('ldflags')
        incs = ' -I' + self.application.settings.get_string('incs')

        gcc_exec = arm_exec + ldflags + incs + ' -Os'
        gcc_opts = (' -o %s -x %s %s' % (shlex.quote(outfile), language, shlex.quote(infile)))
        for header in headers:
            gcc_opts += (' %s' % (shlex.quote(header)))
        gcc_opts += ' -lev3api'

        # is multithreading?
        with open(infile, 'rb', 0) as file, \
            mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as string:
            if string.find(b'pthread.h') != -1:
                gcc_opts += ' -lpthread'
            string.close()
        LOGGER.debug('command: {}'.format(gcc_exec + gcc_opts))

        gcc_proc = subprocess.Popen(('%s %s' % (gcc_exec, gcc_opts)),
                                    shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

        gcc_data = gcc_proc.communicate()
        if gcc_proc.returncode:  # Error
            return (gcc_proc.returncode, gcc_data[1].decode())
        else:  # OK
            msg = '{}: compile successfull\n'.format(document.get_basename())
            return (gcc_proc.returncode, msg)

    def ev3_upload(self, infile):
        '''
        upload file to EV3 brick
        '''
        brick = self.application.ev3_brick
        if brick:
            if brick.usb_ready():

                prjname = infile.stem
                prjsstore = self.application.settings.get_string('prjsstore')
                outfile = str(Path(prjsstore, prjname, infile.name))

                data = infile.read_bytes()
                # TODO: GetErrorCode from brick
                brick.write_file(outfile, data)

                content = brick.list_dir(str(Path(prjsstore, prjname)))

                for afile in content['files']:
                    if afile['name'] == infile.name:
                        error = 1
                        msg = '# Error: Failed to upload {}, try again\n'.format(infile.name)
                        if afile['md5'] == hashlib.md5(data).hexdigest().upper():
                            error = 0
                            msg = 'Upload of {} successfull\n'.format(infile.name)
                return (error, msg)
            else:
                return (2, 'brick not ready\n')
