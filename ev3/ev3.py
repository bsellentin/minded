#!/usr/bin/env python3


import struct
import threading
import time
import logging
import usb.core

logger = logging.getLogger(__name__)

class DirCmdError(Exception):
    """
    Direct command replies error
    """
    pass

class SysCmdError(Exception):
    """
    System command replies error
    """
    pass

class EV3():

    _msg_cnt = 41
    _lock = threading.Lock()

    def __init__(self):
        self.device = usb.core.find(idVendor=ID_VENDOR_LEGO, idProduct=ID_PRODUCT_EV3)
        if self.device is None:
            raise RuntimeError("No Lego EV3 found")
        if self.device.is_kernel_driver_active(0) is True:
            self.device.detach_kernel_driver(0)
        self.device.set_configuration()
        # gives USBError.timeout
        #self.device.read(EP_IN, 1024, EV3_USB_TIMEOUT)

    def __del__(self): pass

    def close(self):

        self.device = None
        logger.debug('USB connection closed.')

    def do_nothing(self):
        cmd = opNop
        self.send_direct_cmd(cmd)

    def usb_set_ready(self):
        '''opCOM_READY
        READY blocks the calling object at user level until the specific
        resource function is completed/failed and then it sets the dispatch
        status to "NOBREAK" or "FAILBREAK" '''
        cmd = b''.join([
            opCom_Ready,
            LCX(1),         # USB
            LCS('0')        # own adapter
        ])
        self.send_direct_cmd(cmd)

    def usb_ready(self):
        '''opCOM_TEST
        TEST can be used to test a resource: if it is busy it will block
        the calling object by setting the dispatch status to "BUSYBREAK"
        until not busy.
        Waits until USB busy-flag is 0 = Ready, then returns True'''

        self._lock.acquire()
        if self._msg_cnt < 65535:
            self._msg_cnt += 1
        else:
            self._msg_cnt = 1
        msg_cnt = self._msg_cnt
        self._lock.release()

        ops = b''.join([
            opCom_Test,
            LCX(1),         # USB
            LCS('0'),       # own adapter
            GVX(0)
        ])
        cmd = b''.join([
            struct.pack('<h', len(ops) + 5),
            struct.pack('<h', msg_cnt),
            DIRECT_COMMAND_REPLY,
            struct.pack('<h', 1),
            ops
        ])

        self.device.write(EP_OUT, cmd, EV3_USB_TIMEOUT)

        success = 0
        rpl_cnt = 0
        for i in range(0,3):
            if rpl_cnt == 0 or rpl_cnt > msg_cnt:
                logger.debug('usb_ready attempt %d' % int(i+1))
                try:
                    reply = bytes(self.device.read(EP_IN, 1024, EV3_USB_TIMEOUT))
                    reply_counter = reply[2:4]
                    rpl_cnt = struct.unpack('<H', reply_counter)[0]
                    logger.warning('USB ready: want %s, got %s' %(msg_cnt, rpl_cnt))
                    if msg_cnt == rpl_cnt:
                        success = 1
                        break
                except usb.core.USBError as e:
                    if e.args == ('Operation timed out',):
                        logger.info(e)
                        continue

        if success:
            len_data = struct.unpack('<H', reply[:2])[0] + 2
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(print_hex('Recv', reply[:len_data]))
            (busy,) = struct.unpack('b', reply[5:len_data])
            if not busy:   # 0 = Ready, 1 = Busy
                return True
        else:
            return False

    def set_brickname(self, name):
        cmd = b''.join([
            opCom_Set,
            SET_BRICKNAME,
            LCS(name)
        ])
        self.send_direct_cmd(cmd)

    def get_brickname(self):
        cmd = b''.join([
            opCom_Get,
            GET_BRICKNAME,
            LCX(16),
            GVX(0)
        ])
        reply = self.send_direct_cmd(cmd, global_mem=16)  # global_mem: needed
        (brickname,) = struct.unpack('16s', reply[5:])    # size in bytes for
        brickname = brickname.split(b'\x00')[0]           # return values
        brickname = brickname.decode('utf-8')
        return brickname

    def get_hw_version(self):
        '''read the hardware version on the given hardware'''
        cmd = b''.join([
            opUI_Read,
            GET_HW_VERS,
            LCX(16),
            GVX(0)
        ])
        reply = self.send_direct_cmd(cmd, global_mem=16)
        (hw_version,) = struct.unpack('16s', reply[5:])
        hw_version = hw_version.split(b'\x00')[0]
        hw_version = hw_version.decode('utf-8')
        return hw_version

    def get_fw_version(self):
        '''read the firmware version currently on the EV3 brick'''
        cmd = b''.join([
            opUI_Read,
            GET_FW_VERS,
            LCX(16),
            GVX(0)
        ])
        reply = self.send_direct_cmd(cmd, global_mem=16)
        (fw_version,) = struct.unpack('16s', reply[5:])
        fw_version = fw_version.split(b'\x00')[0]
        fw_version = fw_version.decode('utf-8')
        return fw_version

    def get_vbatt(self):
        '''(DataF) Value – Battery voltage [V]'''
        cmd = b''.join([
            opUI_Read,
            GET_VBATT,
            GVX(0),
        ])
        reply = self.send_direct_cmd(cmd, global_mem=4)
        (vbatt,) = struct.unpack('<f', reply[5:])
        return str(vbatt)[:4]

    def get_lbatt(self):
        '''(Data8) PCT – Battery level in percentage [0 - 100]'''
        cmd = b''.join([
            opUI_Read,
            GET_LBATT,
            GVX(0)
        ])
        reply = self.send_direct_cmd(cmd, global_mem=2)
        (lbatt,) = struct.unpack('<H', reply[5:])
        return lbatt

    def get_os_version(self):
        '''get OS version string'''
        cmd = b''.join([
            opUI_Read,
            GET_OS_VERS,
            LCX(18),
            GVX(0)
        ])
        reply = self.send_direct_cmd(cmd, global_mem=18)
        (os_version,) = struct.unpack('18s', reply[5:])
        os_version = os_version.split(b'\x00')[0]
        os_version = os_version.decode('utf-8')
        return os_version

    def get_os_build(self):
        '''read the OS build info currently on the EV3 brick'''
        cmd = b''.join([
            opUI_Read,
            GET_OS_BUILD,
            LCX(18),
            GVX(0)
        ])
        reply = self.send_direct_cmd(cmd, global_mem=18)
        (os_build,) = struct.unpack('18s', reply[5:])
        os_build = os_build.split(b'\x00')[0]
        os_build = os_build.decode('utf-8')
        return os_build

    def get_free_mem(self):
        '''get the free internal memory on the brick'''
        # (Data32) TOTAL – Total amount of internal memory [KB]
        # (Data32) FREE – Free memory [KB]
        cmd = b''.join([
            opMemory_Usage,     # returns 4 bytes, rest is garbage
            LCX(0),
            GVX(0),
        ])
        reply = self.send_direct_cmd(cmd, global_mem=4)
        (total,) = struct.unpack('<I', reply[5:])
        return total

    def get_sdcard(self):
        # GET_SDCARD= 0x1D
        # Return
        # (Data8) STATE – SD Card present, [0: No, 1: Present]
        # (Data32) TOTAL – SD Card memory size [KB]
        # (Data32) FREE – Amount of free memory [KB]
        pass

    def get_type_mode(self):
        cmd = b''.join([
            opInput_Device,
            GET_TYPEMODE,
            LCX(0),
            LCX(0),    # port A
            GVX(0),
            GVX(1)
        ])
        reply = self.send_direct_cmd(cmd, global_mem=2)
        typemode = struct.unpack('BB', reply[5:])
        return typemode

    def get_folders(self, directory):
        '''
        reads the number of sub folders within a folder
        '''
        cmd = b''.join([
            opFile,
            GET_FOLDERS,
            LCS(directory),
            GVX(0)
            ])
        reply = self.send_direct_cmd(cmd, global_mem=1)
        num = struct.unpack('<B', reply[5:])[0]
        return num

    def get_subfolder_name(self, directory, index):
        cmd = b''.join([
            opFile,
            GET_SUBFOLDER_NAME,
            LCS(directory),
            LCX(index + 1),     # ITEM
            LCX(64),            # LENGTH
            GVX(0)              # NAME
        ])
        reply = self.send_direct_cmd(cmd, global_mem=64)
        subdir = struct.unpack('64s', reply[5:])[0]
        subdir = subdir.split(b'\x00')[0]
        subdir = subdir.decode()
        return subdir

    def play_sound(self, name):
        cmd = b''.join([
            opSound,
            PLAY,
            LCX(100),
            LCS(name)
            ])
        self.send_direct_cmd(cmd)

    def list_dir(self, path: str) -> dict:
        cmd = b''.join([
            LIST_FILES,
            struct.pack('<H', 1012),    # SIZE
            str.encode(path) + b'\x00'  # NAME
            ])
        reply = self.send_system_cmd(cmd)
        (size, handle) = struct.unpack('<IB', reply[7:12])
        part_size = min(1012, size)
        if part_size > 0:
            fmt = str(part_size) + 's'
            data = struct.unpack(fmt, reply[12:])[0]
        else:
            data = b''
        rest = size - part_size
        while rest > 0:
            part_size = min(1016, rest)
            cmd = b''.join([
                CONTINUE_LIST_FILES,
                struct.pack('<BH', handle, part_size)
            ])
            reply = self.send_system_cmd(cmd)
            fmt = 'B' + str(part_size) + 's'
            (handle, part) = struct.unpack(fmt, reply[7:])
            data += part_size
            rest -= part_size
            if rest <= 0 and reply[6:7] != SYSTEM_END_OF_FILE:
                raise SysCmdError("end of file not reached")
        folders = []
        files = []
        for line in data.split(sep=b'\x0A'):
            if line == b'':
                pass
            elif line.endswith(b'\x2F'):
                folders.append(line.rstrip(b'\x2F').decode("utf8"))
            else:
                (md5, size_hex, name) = line.split(None, 2)
                size = int(size_hex, 16)
                files.append({
                    'md5': md5.decode("utf8"),
                    'size': size,
                    'name': name.decode("utf8")
                })
        return {'files': files, 'folders': folders}

    def write_file(self, path:str, data: bytes) -> None:
        size = len(data)
        cmd = b''.join([
            BEGIN_DOWNLOAD,
            struct.pack('<I', size),    # SIZE
            str.encode(path) + b'\x00'  # NAME
            ])
        reply = self.send_system_cmd(cmd)
        handle = struct.unpack('B', reply[7:8])[0]
        rest = size
        while rest > 0:
            part_size = min(1017, rest)
            pos = size - rest
            fmt = 'B' + str(part_size) + 's'
            cmd = b''.join([
                CONTINUE_DOWNLOAD,
                struct.pack(fmt, handle, data[pos:pos+part_size])   # HANDLE, DATA
            ])
            self.send_system_cmd(cmd)
            rest -= part_size

    def read_file(self, path:str) -> bytes:
        cmd = b''.join([
            BEGIN_UPLOAD,
            struct.pack('<H', 1012),    # SIZE
            str.encode(path) + b'\x00'  # NAME
        ])
        reply = self.send_system_cmd(cmd)
        (size, handle) = struct.unpack('<IB', reply[7:12])
        part_size = min(1012, size)
        if part_size > 0:
            fmt = str(part_size) + 's'
            data = struct.unpack(fmt, reply[12:])[0]
        else:
            data = b''
        rest = size - part_size
        while rest > 0:
            part_size = min(1016, rest)
            cmd = b''.join([
                CONTINUE_UPLOAD,
                struct.pack('<BH', handle, part_size)   # HANDLE, SIZE
            ])
            reply = self.send_system_cmd(cmd)
            fmt = 'B' + str(part_size) + 's'
            (handle, part) = struct.unpack(fmt, reply[7:])
            data += part
            rest -= part_size
            if rest <= 0 and reply[6:7] != SYSTEM_END_OF_FILE:
                raise SysCmdError("end of file not reached")
        return data

    def del_file(self, path: str) -> None:
        '''
        deletes a file and empty directories
        '''
        cmd = b''.join([
            DELETE_FILE,
            str.encode(path) + b'\x00'  # Name
        ])
        self.send_system_cmd(cmd)

    def send_direct_cmd(self, ops: bytes, local_mem: int=0, global_mem: int=0) -> bytes:

        if global_mem > 0:
            cmd_type = DIRECT_COMMAND_REPLY
        else:
            cmd_type = DIRECT_COMMAND_NO_REPLY

        self._lock.acquire()
        if self._msg_cnt < 65535:
            self._msg_cnt += 1
        else:
            self._msg_cnt = 1
        msg_cnt = self._msg_cnt
        self._lock.release()

        cmd = b''.join([
            struct.pack('<h', len(ops) + 5),
            struct.pack('<h', msg_cnt),
            cmd_type,
            struct.pack('<h', local_mem*1024 + global_mem),
            ops
        ])
        self.device.write(EP_OUT, cmd, EV3_USB_TIMEOUT)
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(print_hex('Sent', cmd))

        if cmd[4:5] == DIRECT_COMMAND_NO_REPLY:
            return msg_cnt
        else:
            while True:
                reply = bytes(self.device.read(EP_IN, 1024, EV3_USB_TIMEOUT))
                reply_counter = reply[2:4]
                rpl_cnt = struct.unpack('<H', reply_counter)[0]
                len_data = struct.unpack('<H', reply[:2])[0] + 2
                if msg_cnt != struct.unpack('<H', reply_counter)[0]:
                    logger.warning('not for me, want %s, got %s' % (msg_cnt, rpl_cnt))
                else:
                    if logger.isEnabledFor(logging.DEBUG):
                        logger.debug(print_hex('Recv', reply[:len_data]))
                    if reply[4:5] != DIRECT_REPLY:
                        raise DirCmdError(
                            "direct command {:02X}:{:02X} replied error".format(
                                reply[2],
                                reply[3]
                            )
                        )
                    return reply[:len_data]

    def send_system_cmd(self, ops: bytes, reply: bool=True) -> bytes:
        if reply:
            cmd_type = SYSTEM_COMMAND_REPLY
        else:
            cmd_type = SYSTEM_COMMAND_NO_REPLY

        self._lock.acquire()
        if self._msg_cnt < 65535:
            self._msg_cnt += 1
        else:
            self._msg_cnt = 1
        msg_cnt = self._msg_cnt
        self._lock.release()

        cmd = b''.join([
            struct.pack('<hh', len(ops) + 3, msg_cnt),
            cmd_type,
            ops
        ])

        self.device.write(EP_OUT, cmd, EV3_USB_TIMEOUT)

        counter = struct.unpack('<H', cmd[2:4])[0]
        logger.debug('msg_cnt: %s, counter: %s' % (msg_cnt, counter))
        if not reply:
            return counter
        else:
            #reply = self.wait_for_system_reply(counter)
            reply = bytes(self.device.read(EP_IN, 1024, EV3_USB_TIMEOUT))
            len_data = struct.unpack('<H', reply[:2])[0] + 2
            reply_counter = reply[2:4]
            rpl_cnt = struct.unpack('<H', reply_counter)[0]
            if msg_cnt != struct.unpack('<H', reply_counter)[0]:
                logger.debug('not for me, want %s, got %s' % (msg_cnt, rpl_cnt))
            else:
                #print("sysreply: ", reply[4:5], "SYSTEM_REPLY", SYSTEM_REPLY)
                if reply[4:5] != SYSTEM_REPLY:  # ! reply = bytes(read)
                    raise SysCmdError("SysCmdError: {:02X}".format(reply[6]))
                logger.debug('reply: %s' % reply[:len_data])
                return reply[:len_data]

    def wait_for_system_reply(self, counter: bytes) -> bytes:
        pass


def LCX(value: int) -> bytes:
    """
    create a LC0, LC1, LC2, LC4, dependent from the value
    """
    if   value >=    -32 and value <      0:
        return struct.pack('b', 0x3F & (value + 64))
    elif value >=      0 and value <     32:
        return struct.pack('b', value)
    elif value >=   -127 and value <=   127:
        return b'\x81' + struct.pack('<b', value)
    elif value >= -32767 and value <= 32767:
        return b'\x82' + struct.pack('<h', value)
    else:
        return b'\x83' + struct.pack('<i', value)

def LCS(value: str) -> bytes:
    """
    pack a string into a LCS
    """
    return b'\x84' + str.encode(value) + b'\x00'

def LVX(value: int) -> bytes:
    """
    create a LV0, LV1, LV2, LV4, dependent from the value
    """
    if value   <     0:
        raise RuntimeError('No negative values allowed')
    elif value <    32:
        return struct.pack('b', 0x40 | value)
    elif value <   256:
        return b'\xc1' + struct.pack('<b', value)
    elif value < 65536:
        return b'\xc2' + struct.pack('<h', value)
    else:
        return b'\xc3' + struct.pack('<i', value)

def GVX(value: int) -> bytes:
    """
    create a GV0, GV1, GV2, GV4, dependent from the value
    """
    if value   <     0:
        raise RuntimeError('No negative values allowed')
    elif value <    32:
        return struct.pack('<b', 0x60 | value)
    elif value <   256:
        return b'\xe1' + struct.pack('<b', value)
    elif value < 65536:
        return b'\xe2' + struct.pack('<h', value)
    else:
        return b'\xe3' + struct.pack('<i', value)

def print_hex(desc: str, data: bytes) -> None:
    print(desc + ' 0x|' + ':'.join('{:02X}'.format(byte) for byte in data) + '|')

ID_VENDOR_LEGO              = 0x0694
ID_PRODUCT_EV3              = 0x0005
EP_IN                       = 0x81
EP_OUT                      = 0x01

EV3_USB_TIMEOUT             = 2000

SYSTEM_COMMAND_REPLY        = b'\x01'   # System command, reply required
SYSTEM_COMMAND_NO_REPLY     = b'\x81'   # System command, reply not require

BEGIN_DOWNLOAD              = b'\x92'
CONTINUE_DOWNLOAD           = b'\x93'
BEGIN_UPLOAD                = b'\x94'
CONTINUE_UPLOAD             = b'\x95'
BEGIN_GETFILE               = b'\x96'
CONTINUE_GETFILE            = b'\x97'
CLOSE_FILEHANDLE            = b'\x98'
LIST_FILES                  = b'\x99'
CONTINUE_LIST_FILES         = b'\x9A'
CREATE_DIR                  = b'\x9B'
DELETE_FILE                 = b'\x9C'
LIST_OPEN_HANDLES           = b'\x9D'
WRITEMAILBOX                = b'\x9E'
BLUETOOTHPIN                = b'\x9F'   # Transfer trusted pin code to brick
ENTERFWUPDATE               = b'\xA0'   # Restart the brick in Firmware update mode

SYSTEM_REPLY                = b'\x03'   # System command reply OK
SYSTEM_REPLY_ERROR          = b'\x05'   # System command reply ERROR

SYSTEM_REPLY_OK             = b'\x00'
SYSTEM_UNKNOWN_HANDLE       = b'\x01'
SYSTEM_HANDLE_NOT_READY     = b'\x02'
SYSTEM_CORRUPT_FILE         = b'\x03'
SYSTEM_NO_HANDLES_AVAILABLE = b'\x04'
SYSTEM_NO_PERMISSION        = b'\x05'
SYSTEM_ILLEGAL_PATH         = b'\x06'
SYSTEM_FILE_EXITS           = b'\x07'
SYSTEM_END_OF_FILE          = b'\x08'
SYSTEM_SIZE_ERROR           = b'\x09'
SYSTEM_UNKNOWN_ERROR        = b'\x0A'
SYSTEM_ILLEGAL_FILENAME     = b'\x0B'
SYSTEM_ILLEGAL_CONNECTION   = b'\x0C'

DIRECT_COMMAND_REPLY        = b'\x00'
DIRECT_COMMAND_NO_REPLY     = b'\x80'

DIRECT_REPLY                = b'\x02'
DIRECT_REPLY_ERROR          = b'\x04'

opNop                       = b'\x01'
opCom_Ready                 = b'\xD0'
opCom_Get                   = b'\xD3'
GET_BRICKNAME               = b'\x0D'
opCom_Test                  = b'\xD5'
opCom_Set                   = b'\xD4'
SET_BRICKNAME               = b'\x08'
opFile                      = b'\xC0'
GET_FOLDERS                 = b'\x0D'
GET_SUBFOLDER_NAME          = b'\x0F'
opInput_Device              = b'\x99'
GET_TYPEMODE                = b'\x05'
opUI_Read                   = b'\x81'
GET_HW_VERS                 = b'\x09'
GET_FW_VERS                 = b'\x0A'
GET_FW_BUILD                = b'\x0B'
GET_VBATT                   = b'\x01'   # (DataF) Value – Battery voltage [V]
GET_LBATT                   = b'\x12'   # (Data8) PCT – Battery level in percentage [0 - 100]
GET_OS_VERS                 = b'\x03'   # get OS version string
GET_OS_BUILD                = b'\x0C'
opMemory_Usage              = b'\xC5'   # ((Data32) TOTAL – Total amount of internal memory [KB],
                                        #  (Data32) FREE – Free memory [KB])
opSound                     = b'\x94'
PLAY                        = b'\x02'
