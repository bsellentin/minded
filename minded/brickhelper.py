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
        returns (error, msg)
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

    def evc_proc(self, document, upload: bool=False):
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
                    self.application.ev3brick.play_sound('./ui/DownloadSucces')

        return (0, msg)

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

        starter = Path(document.get_path()).with_suffix('.rbf')
        try:
            starter.write_bytes(cmd)
            return (0, 'Build starter successfull\n')
        except OSError as err:
            return (1, 'OS error:{0}'.format(err))

    def cross_compile(self, document):
        '''
        cross-compile evc-file for EV3-brick, store local, upload later
        '''
        infile = document.get_path()
        logger.debug('file to compile: {}'.format(infile))

        outfile = str(Path(document.get_parent(), Path(document.get_basename()).stem))
        logger.debug('executable to write: {}'.format(outfile))

        cplusplus =self.application.settings.get_boolean('cplusplus')
        if cplusplus:
            arm_exec = self.application.settings.get_string('armgplusplus')
            language = 'c++'
        else:
            arm_exec = self.application.settings.get_string('armgcc')
            language = 'c'

        ldflags = self.application.settings.get_string('ldflags')
        incs = self.application.settings.get_string('incs')

        gcc_exec = arm_exec + ldflags + incs + ' -Os'
        gcc_opts = (' -o %s -x %s %s -lev3api' % (shlex.quote(outfile), language, shlex.quote(infile)))

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
            return (gcc_proc.returncode, gcc_data[1].decode())
        else:  # OK
            msg = 'Compile successfull\n'
            return (gcc_proc.returncode, msg)

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

