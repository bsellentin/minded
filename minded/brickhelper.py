#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pathlib import Path
import subprocess
import shlex
import struct
import hashlib
import mmap


import logging
logger = logging.getLogger(__name__)

class BrickHelper():
    '''
    Helper to put programms on brick
    '''

    def __init__(self, application, *args, **kwargs):

        self.application = application

    def nbc_proc(self, document, upload: bool=False):
        '''
        compile and upload file to NXT brick
        '''
        nbc_exec = self.application.settings.get_string('nbcpath')
        if not nbc_exec:
            return (2, 'no NBC-executable found')
        else:
            enhancedfw = self.application.settings.get_boolean('enhancedfw')
            if enhancedfw:
                nbc_exec = nbc_exec + ' -EF'
            logger.debug('use enhancedfw: {}'.format(enhancedfw))

            if upload:
                # compile and upload
                nbc_opts = (' -d %s' % (shlex.quote(document.get_path())))
                logger.debug('upload: {}'.format(nbc_opts))
            else:
                # compile only
                #nbcout = str(Path(document.get_filepath(),
                #             Path(document.get_shortname()).stem + '.rxe'))
                nbcout = str(Path(document.get_path()).with_suffix('.rxe'))
                logger.debug('File to compile: {}'.format(document.get_path()))
                nbc_opts = (' -O=%s %s' % (shlex.quote(nbcout),
                                           shlex.quote(document.get_path())))

            # do it
            nbc_proc = subprocess.Popen(('%s %s' % (nbc_exec, nbc_opts)),
                                        shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)

            nbc_data = nbc_proc.communicate()
            if nbc_proc.returncode:  # Error
                return (nbc_proc.returncode, nbc_data[1].decode())
            else:  # OK
                # nur die letzten 5 Zeilen ausgeben
                msg = '\n'.join([str(i) for i in nbc_data[0].decode().split('\n')[-5:]])
                return (nbc_proc.returncode, msg)

    def mkstarter(self, document):
        '''
        build rbf-starter-file, store local, upload later
        '''
        logger.debug('building starter for: {}'.format(document.get_path()))

        prjname = Path(document.get_basename()).stem
        prjsstore = self.application.settings.get_string('prjsstore')
        prjpath = str(Path(prjsstore, prjname, prjname))
        logger.debug('EV3-path: {}'.format(prjpath))

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

        #starter = Path(document.get_filepath(), prjname + '.rbf')
        starter = Path(document.get_path()).with_suffix('.rbf')
        starter.write_bytes(cmd)

        return 1

    def cross_compile(self, document):
        '''
        cross-compile evc-file for EV3-brick, store local, upload later
        '''
        infile = document.get_path()
        logger.debug('file to compile: {}'.format(infile))

        outfile = str(Path(document.get_parent(), Path(document.get_basename()).stem))
        logger.debug('executable to write: {}'.format(outfile))

        arm_exec = self.application.settings.get_string('armgcc')

        ldflags = self.application.settings.get_string('ldflags')
        incs = self.application.settings.get_string('incs')

        gcc_exec = arm_exec + ldflags + incs + ' -Os'
        gcc_opts = (' -o %s -x c %s -lev3api' % (shlex.quote(outfile), shlex.quote(infile)))

        # is multithreading?
        with open(infile,  'rb', 0) as file, \
            mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            if s.find(b'pthread.h') != -1:
                gcc_opts += ' -lpthread'
        logger.debug('command: {}'.format(gcc_exec + gcc_opts))

        gcc_proc = subprocess.Popen(('%s %s' % (gcc_exec, gcc_opts)),
                                        shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)

        gcc_data = gcc_proc.communicate()
        if gcc_proc.returncode:  # Error
            return gcc_data[1].decode()
        else:  # OK
            return 0


    def ev3_upload(self, infile):
        '''
        upload file to EV3 brick
        '''
        brick = self.application.ev3brick
        if brick:
            if brick.usb_ready():

                prjname = infile.stem
                prjsstore = self.application.settings.get_string('prjsstore')
                outfile = str(Path(prjsstore, prjname, infile.name))

                data = infile.read_bytes()
                brick.write_file(outfile, data)

                content = brick.list_dir(str(Path(prjsstore, prjname)))

                for afile in content['files']:
                    if afile['name'] == infile.name:
                        error = 1
                        if afile['md5'] == hashlib.md5(data).hexdigest().upper():
                            error = 0
                return error
            else:
                return 2

