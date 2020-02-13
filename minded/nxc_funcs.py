# -*- coding: utf-8 -*-

'''
NXC-functions for MindEd
'''

# Copyright (C) 2017 Bernd Sellentin <sel@gge-em.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

NXC_FUNCS = [
    ['Acquire', 'Acquire(m)',
     ('<b>Acquire (mutex <span foreground="brown">m</span>)</b>\n\n'
     'Acquire the specified mutex variable. If another task already '
     'has acquired the mutex then the current task will be suspended '
     'until the mutex is released by the other task. This function '
     'is used to ensure that the current task has exclusive access '
     'to a shared resource, such as the display or a motor. After the '
     'current task has finished using the shared resource the program '
     'should call Release to allow other tasks to acquire the mutex.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">m</span>\tThe mutex to acquire.\n'
     '<b>Example:</b>\n'
     '\tmutex motorMutex;\n'
     '\t// ...\n'
     '\tAcquire(motorMutex); // make sure we have exclusive access\n'
     '\t// use the motors\n'
     '\tRelease(motorMutex);'), 'Command'],
    ['ArrayInit', 'ArrayInit(aout, value, count)',
     ('<b>ArrayInit (<span foreground="brown">aout[]</span>, '
     '<span foreground="brown">value</span>, '
     '<span foreground="brown">count</span>)</b>\n\n'
     'Initialize an array to contain count elements with each element '
     'equal to the value provided. To initialize a multi-dimensional '
     'array, the value should be an array of N-1 dimensions, where N is '
     'the number of dimensions in the array being initialized.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">aout</span>\tThe output array to initialize.\n'
     '\t<span foreground="brown">value</span>\tThe value to initialize each element to.\n'
     '\t<span foreground="brown">count</span>\tThe number of elements to create in the output array.\n'
     '<b>Example:</b>\n'
     '\tint myArray[];\n'
     '\tArrayInit(myArray, 0, 10); // 10 elements == zero'), 'Command'],
    ['ArrayLen', 'ArrayLen(data)',
     ('<b>ArrayLen (<span foreground="brown">data[]</span>)</b>\n\n'
     'Return the length of the specified array. Any type of array '
     'of up to four dimensions can be passed into this function.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">data</span>\tThe array whose length you need to read.\n'
     '<b>Returns</b>\n'
     '\tThe length of the specified array.\n'
     '<b>Example:</b>\n'
     '\tx = ArrayLen(myArray);'), 'Command'],
    ['BluetoothStatus', 'BluetoothStatus(conn)',
     ('<b>BluetoothStatus (<span foreground="brown">conn</span>)</b>\n\n'
     'Check the status of the bluetooth subsystem for the specified '
     'connection slot.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">conn</span>\tThe connection slot (0..3).\n'
     '\t\tConnections 0 through 3 are for bluetooth connections.\n'
     '<b>Returns</b>\n'
     '\tThe bluetooth status for the specified connection.\n'
     '<b>Example:</b>\n'
     '\tx = BluetoothStatus(1);'), 'Communication'],
    ['ButtonCount', 'ButtonCount(btn)',
     ('<b>ButtonCount (<span foreground="brown">btn</span>, '
     '<span foreground="brown">resetCount</span> = false)</b>\n\n'
     'Return the number of times the specified button has been pressed '
     'since the last time the button press count was reset. Optionally '
     'clear the count after reading it.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">btn</span>\tThe button to check.\n'
     '\t<span foreground="brown">resetCount</span>\tWhether or not to reset the press counter.\n'
     '<b>Returns</b>\n'
     '\tThe button press count.\n'
     '<b>Example:</b>\n'
     '\tvalue = ButtonCount(BTNRIGHT, true);'), 'Button'],
    ['ButtonLongPressCount', 'ButtonLongPressCount(btn)',
     ('<b>ButtonLongPressCount ('
     '<span foreground="brown">btn</span>)</b>\n\n'
     'Get button long press count.\n'
     'Return the long press count of the specified button.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">btn</span>\tThe button to check. See Button name constants.\n'
     '<b>Returns</b>\n'
     '\tThe button long press count.\n'
     '<b>Example:</b>\n'
     '\tvalue = ButtonLongPressCount(BTN1);'), 'Button'],
    ['ButtonPressCount', 'ButtonPressCount(btn)',
     ('<b>ButtonPressCount ('
     '<span foreground="brown">btn</span>)</b>\n\n'
     'Get the press count of the specified button.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">btn</span>\tThe button to check.\n'
     '<b>Returns</b>\n'
     '\tThe button press count.\n'
     '<b>Example:</b>\n'
     '\tvalue = ButtonPressCount(BTN1);'), 'Button'],
    ['ButtonPressed', 'ButtonPressed(btn, resetCount)',
     ('<b>ButtonPressed ('
     '<span foreground="brown">btn</span>, '
     '<span foreground="brown">resetCount</span> = false)</b>\n\n'
     'Check for button press. This function checks whether the specified '
     'button is pressed or not. You may optionally reset the press count.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">btn</span>\tThe button to check. See Button name constants.\n'
     '\t<span foreground="brown">resetCount</span>\tWhether or not to reset the press counter.\n'
     '<b>Returns</b>\n'
     '\tA boolean value indicating whether the button is pressed or not.\n'
     '<b>Example:</b>\n'
     '\t// Wait until user presses and releases\n'
     '\t// exit button before continuing loop\n'
     '\twhile(!(ButtonPressed(BTNEXIT, 0)));\n'
     '\twhile(ButtonPressed(BTNEXIT, 0));'), 'Button'],
    ['ButtonState', 'ButtonState(btn)',
     ('<b>ButtonState (<span foreground="brown">btn</span>)</b>\n\n'
     'Get the state of the specified button.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">btn</span>\tThe button to check.\n'
     '<b>Returns</b>\n'
     '\tThe button state.\n'
     '<b>Example:</b>\n'
     '\tvalue = ButtonState(BTNLEFT);'), 'Button'],
    ['ClearScreen', 'ClearScreen()',
     ('<b>ClearScreen ()</b>\n\n'
     'Clear LCD screen. This function lets you clear '
     'the NXT LCD to a blank screen.\n\n'
     '<b>Example:</b>\n'
     '\tClearScreen();'), 'Display'],
    ['ClearSensor', 'ClearSensor(port)',
     ('<b>ClearSensor (<span foreground="brown">port</span>)</b>\n\n'
     'Clear the value of a sensor - only affects sensors that are '
     'configured to measure a cumulative quantity such as rotation '
     'or a pulse count.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe Input port to clear.\n'
     '<b>Example:</b>\n'
     '\tClearSensor(IN_1);'), 'Input'],
    ['CircleOut', 'CircleOut(x, y, radius)',
     ('<b>CircleOut ('
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">radius</span>, '
     '<span foreground="brown">options</span> = DRAW_OPT_NORMAL)</b>\n\n'
     'Draw a circle on the screen with its center at the specified '
     'x and y location, using the specified radius. Optionally specify '
     'drawing options. If this argument is not specified it defaults '
     'to DRAW_OPT_NORMAL.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">x</span>\tThe x value for the center of the circle.\n'
     '\t<span foreground="brown">y</span>\tThe y value for the center of the circle.\n'
     '\t<span foreground="brown">radius</span>\tThe radius of the circle.\n'
     '\t<span foreground="brown">options</span>\tThe optional drawing options.\n'
     '\t\t<b><span foreground="red">Warning:</span></b> These options require the\n'
     '\t\tenhanced NBC/NXC firmware\n'
     '<b>Example:</b>\n'
     '\tCircleOut(20, 50, 20, DRAW_OPT_FILL_SHAPE);'), 'Display'],
    ['Coast', 'Coast(outputs)',
     ('<b>Coast (<span foreground="brown">outputs</span>)</b>\n\n'
     'Coast motors. Turn off the specified outputs, making them '
     'coast to a stop.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '<b>Example:</b>\n'
     '\tCoast(OUT_A); // coast output A'), 'Output'],
    ['CurrentTick', 'CurrentTick()',
     ('<b>CurrentTick ()</b>\n\n'
     'Read the current system tick.\n\n'
     '<b>Returns</b>\n'
     '\tThe current system tick count.\n'
     '<b>Example:</b>\n'
     '\tlong tick;\n'
     '\tick = CurrentTick();'), 'Command'],
    ['CreateFile', 'CreateFile(fname, fsize, handle)',
     ('<b>CreateFile('
     '<span foreground="brown">fname</span>, '
     '<span foreground="brown">fsize</span>, '
     '<span foreground="brown">handle</span>)</b>\n\n'
     'Create a new file with the specified filename and size and open it for writing. '
     'The file handle is returned in the last parameter, which must be a variable. '
     'The loader result code is returned as the value of the function call.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">fname</span>\tThe name of the file to create.\n'
     '\t<span foreground="brown">fsize</span>\tThe size of the file.\n'
     '\t<span foreground="brown">handle</span>\tThe file handle output from the function call.\n'
     '<b>Returns</b>\n'
     '\tThe function call result.\n'
     '<b>Example:</b>\n'
     '\tresult = CreateFile("data.txt", 1024, handle);'), 'Loader'],
    ['CloseFile', 'CloseFile(handle)',
     ('<b>CloseFile('
     '<span foreground="brown">handle</span>)</b>\n\n'
     'Close the file associated with the specified file handle. The loader result '
     'code is returned as the value of the function call. The handle parameter must '
     'be a constant or a variable.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">handle</span>\tThe file handle.\n'
     '<b>Returns</b>\n'
     '\tThe function call result.\n'
     '<b>Example:</b>\n'
     '\tresult = CloseFile(handle);'), 'Loader'],
    ['DeleteFile', 'DeleteFile(fname)',
     ('<b>DeleteFile('
     '<span foreground="brown">fname</span>)</b>\n\n'
     'Delete the specified file. The loader result code is returned as the value of '
     'the function call. The filename parameter must be a constant or a variable.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">fname</span>\tThe name of the file to delete.\n'
     '<b>Returns</b>\n'
     '\tThe function call result.\n'
     '<b>Example:</b>\n'
     '\tresult = DeleteFile("data.txt");'), 'Loader'],
    ['Float', 'Float(outputs)',
     ('<b>Float (<span foreground="brown">outputs</span>)</b>\n\n'
     'Float motors. Make outputs float. Float is an alias for Coast.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '<b>Example:</b>\n'
     '\tFloat(OUT_A); // float output A'), 'Output'],
    ['GraphicOut', 'GraphicOut(x, y, filename)',
     ('<b>GraphicOut ('
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">filename</span>, '
     '<span foreground="brown">options</span> = DRAW_OPT_NORMAL)</b>\n\n'
     'Draw a graphic image file on the screen at the specified '
     'x and y location. Optionally specify drawing options. If '
     'this argument is not specified it defaults to DRAW_OPT_NORMAL.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">x</span>\tThe x value for the position\n'
     '\t<span foreground="brown">y</span>\tThe y value for the position\n'
     '\t<span foreground="brown">filename</span>\tThe filename of the RIC graphic image.\n'
     '\t<span foreground="brown">options</span>\tThe optional drawing options.\n'
     '\t\t<b><span foreground="red">Warning:</span></b> These options require the\n'
     '\t\tenhanced NBC/NXC firmware\n'
     '<b>Example:</b>\n'
     '\tGraphicOut(40, 40, "image.ric");'), 'Display'],
    ['I2CBytes', 'I2CBytes(port, inbuf[], &count, &outbuf[])',
     ('<b>I2CBytes ('
     '<span foreground="brown">port</span>, '
     '<span foreground="brown">inbuf[]</span>, '
     '<span foreground="brown">&count</span>, '
     '<span foreground="brown">&outbuf[]</span>)</b>\n\n'
     'This method writes the bytes contained in the input '
     'buffer (inbuf) to the I2C device on the specified port, '
     'checks for the specified number of bytes to be ready '
     'for reading, and then tries to read the specified '
     'number (count) of bytes from the I2C device into '
     'the output buffer (outbuf).\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to which the I2C device is attached.\n'
     '\t<span foreground="brown">inbuf</span>\tA byte array containing the address of\n'
     '\t\tthe I2C device, the I2C device register\n '
     '\t\tat which to write data, and up to 14 bytes\n'
     '\t\tof data to be written at the specified register.\n'
     '\t<span foreground="brown">count</span>\tThe number of bytes that should be returned\n'
     '\t\tby the I2C device. On output count is\n'
     '\t\t set to the number of bytes in outbuf.\n'
     '\t<span foreground="brown">outbuf</span>\tA byte array that contains the data\n'
     '\t\tread from the internal I2C buffer.\n'
     '<b>Returns</b>\n'
     '\tReturns true or false indicating whether the I2C transaction\n'
     '\tsucceeded or failed.\n'
     '<b>Example:</b>\n'
     '\tint count=6;                // 6 bytes to read\n'
     '\tbyte inbuf[] = {0x10, 0x43};// I2C adr, reg adr\n'
     '\tbyte respBuf[];             // output buffer\n'
     '\tbool success;\n'
     '\tsuccess = I2CBytes(port, inbuf, count, respBuf);'), 'Input'],
    ['LineOut', 'LineOut(x1, y1, x2, y2)',
     ('<b>LineOut ('
     '<span foreground="brown">x1</span>, '
     '<span foreground="brown">y1</span>, '
     '<span foreground="brown">x2</span>, '
     '<span foreground="brown">y2</span>, '
     '<span foreground="brown">options</span> = DRAW_OPT_NORMAL)</b>\n\n'
     'This function lets you draw a line on the screen from x1, y1 '
     'to x2, y2. Optionally specify drawing options. If this argument '
     'is not specified it defaults to DRAW_OPT_NORMAL.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">x1</span>\tThe x value for the start of the line.\n'
     '\t<span foreground="brown">y1</span>\tThe y value for the start of the line.\n'
     '\t<span foreground="brown">x2</span>\tThe x value for the end of the line.\n'
     '\t<span foreground="brown">y2</span>\tThe y value for the end of the line.\n'
     '\t<span foreground="brown">options</span>\tThe optional drawing options.\n'
     '\t\t<b><span foreground="red">Warning:</span></b> These options require the\n'
     '\t\tenhanced NBC/NXC firmware\n'
     '<b>Example:</b>\n'
     '\tLineOut(0, 0, <span foreground="green">DISPLAY_WIDTH</span>,'
     ' <span foreground="green">DISPLAY_HEIGHT</span>);'), 'Display'],
    ['MotorRotationCount', 'MotorRotationCount(output)',
     ('<b>MotorRotationCount'
     ' (<span foreground="brown">output</span>)</b>\n\n'
     'Get the program-relative position counter value of the '
     'specified output.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">output</span>\tDesired output port. Can be OUT_A, OUT_B, OUT_C.\n'
     '<b>Returns</b>\n'
     '\tThe program-relative position counter value of the\n'
     '\tspecified output.\n'
     '<b>Example:</b>\n'
     '\tlong deg = MotorRotationCount(OUT_A);'), 'Output'],
    ['NumOut', 'NumOut(x, y, value)',
     ('<b>NumOut (<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">value</span>)</b>\n\n'
     'Draw a numeric value on the screen at the '
     'specified x and y location.\n'
     'The y value must be a multiple of 8.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">x</span>\tThe x value for the start of the number output.\n'
     '\t<span foreground="brown">y</span>\tThe text line number for the number output.\n'
     '\t<span foreground="brown">value</span>\tThe value to output to the LCD screen. Any numeric\n'
     '\t\ttype is supported.\n'
     '<b>Example:</b>\n'
     '\tNumOut(0, <span foreground="green">LCD_LINE1</span>, x);'), 'Display'],
    ['NumToStr', 'NumToStr(num)',
     ('<b>NumToStr (<span foreground="brown">num</span>)</b>\n\n'
     'Return the string representation of the specified numeric value.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">num</span>\tA number.\n'
     '<b>Returns</b>\n'
     '\tThe string representation of the parameter num.\n'
     '<b>Example:</b>\n'
     '\tmsg = NumToStr(-2); // returns "-2" in a string'), 'C API'],
    ['OnFwd', 'OnFwd(outputs, pwr)',
     ('<b>OnFwd (<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>)</b>\n\n'
     'Run motors forward. Set outputs to forward direction '
     'and turn them on.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '<b>Example:</b>\n'
     '\tOnFwd(OUT_A, 75);'), 'Output'],
    ['OnRev', 'OnRev(outputs, pwr)',
     ('<b>OnRev (<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>)</b>\n\n'
     'Run motors backward. Set outputs to reverse direction '
     'and turn them on.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '<b>Example:</b>\n'
     '\tOnRev(OUT_A, 75);'), 'Output'],
    ['OnFwdReg', 'OnFwdReg(outputs, pwr, regmode)',
     ('<b>OnFwdReg (<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">regmode</span> )</b>\n\n'
     'Run motors forward using the specified regulation mode.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">regmode</span>\tRegulation modes, can be\n'
     '\t\tOUT_REGMODE_IDLE\tnone\n'
     '\t\tOUT_REGMODE_SPEED\tspeed regulation\n'
     '\t\tOUT_REGMODE_SYNC\tmulti-motor\n'
     '\t\t\tsynchronization\n'
     '\t\tOUT_REGMODE_POS\tposition\n'
     '\t\t\tregulation\n'
     '<b>Example:</b>\n'
     '\t// regulate speed\n'
     '\tOnFwdReg(OUT_A, 75, OUT_REGMODE_SPEED);'), 'Output'],
['OnFwdRegPID', 'OnFwdRegPID(outputs, pwr, regmode, p, i, d)',
     ('<b>OnFwdRegPID('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">regmode</span>, '
     '<span foreground="brown">p</span>, '
     '<span foreground="brown">i</span>, '
     '<span foreground="brown">d</span>)</b>\n\n'
     'Run motors forward regulated with PID factors.\n'
     'Run the specified outputs forward using the specified '
     'regulation mode. Specify proportional, integral and '
     'derivative factors.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">regmode</span>\tRegulation mode.\n'
     '\t<span foreground="brown">p</span>\tProportional factor.\n'
     '\t<span foreground="brown">i</span>\tIntegral factor.\n'
     '\t<span foreground="brown">d</span>\tDerivative factor.\n'
     '<b>Example:</b>\n'
     '\t// regulate speed\n'
     '\tOnFwdRegPID(OUT_A, 75, OUT_REGMODE_SPEED, 30, 50, 90);'), 'Output'],
    ['OnFwdSync', 'OnFwdSync(outputs, pwr, turnpct)',
     ('<b>OnFwdSync (<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">turnpct</span>)</b>\n\n'
     'Run motors forward with regulated synchronization using '
     'the specified turn ratio.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">turnpct</span>\tTurn ratio, -100 to 100.\n'
     '\t\tNegative TurnRatio values shift power toward\n'
     '\t\tthe left motor while positive values shift\n'
     '\t\tpower toward the right motor. An absolute\n'
     '\t\tvalue of 50 results in one motor stopping.\n'
     '\t\tAn absolute value of 100 usually results in\n'
     '\t\ttwo motors turning in opposite directions at\n'
     '\t\tequal power.\n'
     '<b>Example:</b>\n'
     '\tOnFwdSync(OUT_AB, 75, -100); // spin right'), 'Output'],
    ['OnFwdSyncPID', 'OnFwdSyncPID(outputs, pwr, turnpct, p, i, d)',
     ('<b>OnFwdSyncPID('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">turnpct</span>, '
     '<span foreground="brown">p</span>, '
     '<span foreground="brown">i</span>, '
     '<span foreground="brown">d</span>)</b>\n\n'
     'Run motors forward synchronised with PID factors.\n'
     'Run the specified outputs forward with regulated '
     'synchronization using the specified turn ratio. '
     'Specify proportional, integral and derivative factors.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">turnpct</span>\tTurn ratio, -100 to 100.\n'
     '\t<span foreground="brown">p</span>\tProportional factor.\n'
     '\t<span foreground="brown">i</span>\tIntegral factor.\n'
     '\t<span foreground="brown">d</span>\tDerivative factor.\n'
     '<b>Example:</b>\n'
     '\tOnFwdSyncPID(OUT_AB, 75, -100, 30, 50, 90); // spin right'), 'Output'],
    ['OnRevReg', 'OnRevReg(outputs, pwr, regmode)',
     ('<b>OnRevReg ( <span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">regmode</span> )</b>\n\n'
     'Run motors reverse using the specified regulation mode.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">regmode</span>\tRegulation modes, can be\n'
     '\t\tOUT_REGMODE_IDLE\tnone\n'
     '\t\tOUT_REGMODE_SPEED\tspeed regulation\n'
     '\t\tOUT_REGMODE_SYNC\tmulti-motor synchronization\n'
     '\t\tOUT_REGMODE_POS\tposition regulation\n'
     '<b>Example:</b>\n'
     '\tOnRevReg(OUT_A, 75, OUT_REGMODE_SPEED); // regulate speed'), 'Output'],
    ['OnRevRegPID', 'OnRevRegPID(outputs, pwr, regmode, p, i, d)',
     ('<b>OnRevRegPID('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">regmode</span>, '
     '<span foreground="brown">p</span>, '
     '<span foreground="brown">i</span>, '
     '<span foreground="brown">d</span>)</b>\n\n'
     'Run motors backward regulated with PID factors.\n'
     'Run the specified outputs reverse using the specified '
     'regulation mode. Specify proportional, integral and '
     'derivative factors.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">regmode</span>\tRegulation mode.\n'
     '\t<span foreground="brown">p</span>\tProportional factor.\n'
     '\t<span foreground="brown">i</span>\tIntegral factor.\n'
     '\t<span foreground="brown">d</span>\tDerivative factor.\n'
     '<b>Example:</b>\n'
     '\tOnRevRegPID(OUT_A, 75, OUT_REGMODE_SPEED, 30, 50, 90); // regulate speed'), 'Output'],
    ['OnRevSync', 'OnRevSync(outputs, pwr, turnpct)',
     ('<b>OnRevSync (<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">turnpct</span>)</b>\n\n'
     'Run motors reverse with regulated synchronization using '
     'the specified turn ratio.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">turnpct</span>\tTurn ratio, -100 to 100.\n'
     '\t\tNegative TurnRatio values shift power toward the\n'
     '\t\tleft motor while positive values shift power toward\n'
     '\t\tthe right motor. An absolute value of 50 results in\n'
     '\t\tone motor stopping. An absolute value of 100 usually\n'
     '\t\tresults in two motors turning in opposite directions\n'
     '\t\tat equal power.\n'
     '<b>Example:</b>\n'
     '\tOnRevSync(OUT_AB, 75, -100); // spin left'), 'Output'],
    ['OnRevSyncPID', 'OnRevSyncPID(outputs, pwr, turnpct, p, i, d)',
     ('<b>OnRevSyncPID('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">turnpct</span>, '
     '<span foreground="brown">p</span>, '
     '<span foreground="brown">i</span>, '
     '<span foreground="brown">d</span>)</b>\n\n'
     'Run motors backward synchronised with PID factors.\n'
     'Run the specified outputs reverse with regulated '
     'synchronization using the specified turn ratio. '
     'Specify proportional, integral and derivative factors.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">turnpct</span>\tTurn ratio, -100 to 100.\n'
     '\t<span foreground="brown">p</span>\tProportional factor.\n'
     '\t<span foreground="brown">i</span>\tIntegral factor.\n'
     '\t<span foreground="brown">d</span>\tDerivative factor.\n'
     '<b>Example:</b>\n'
     '\tOnRevSyncPID(OUT_AB, 75, -100, 30, 50, 90); // spin left'), 'Output'],
    ['PlayTone', 'PlayTone(frequency, duration)',
     ('<b>PlayTone (<span foreground="brown">frequency</span>,'
     ' <span foreground="brown">duration</span>)</b>\n\n'
     'Play a single tone of the specified frequency and duration.\n'
     'The frequency is in Hz. The duration is in 1000ths of a second. '
     'The tone is played at the loudest sound level.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">frequency</span>\tThe desired tone frequency, in Hz.\n'
     '\t<span foreground="brown">duration</span>\tThe desired tone duration, in ms.\n'
     '<b>Example:</b>\n'
     '\t// Play Tone A for one half second\n'
     '\tPlayTone(440, 500);'), 'Sound'],
    ['PlayTones', 'PlayTones(tones)',
     ('<b>PlayTones (<span foreground="brown">tones[]</span>)</b>\n\n'
     'Play a series of tones contained in the tones array. Each element '
     'in the array is an instance of the Tone  structure, containing a '
     'frequency and a duration.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">tones[]</span>\tThe array of tones to play.\n'
     '<b>Example:</b>\n'
     '\tTone sweepUp[] = {\n'
     '\t  TONE_C4, MS_50, \n'
     '\t  TONE_E4, MS_50, \n'
     '\t  TONE_G4, MS_50,\n'
     '\t  TONE_C5, MS_50, \n'
     '\t  TONE_E5, MS_50, \n'
     '\t  TONE_G5, MS_50, \n'
     '\t  TONE_C6, MS_200\n'
     '\t};\n'
     '\ttask main(){\n'
     '\t  PlayTones(sweepUp);\n'
     '\t  Wait(SEC_1);\n'
     '\t}'), 'Sound'],
    ['PlayToneEx', 'PlayToneEx(frequency, duration, volume, loop)',
     ('<b>PlayToneEx('
     '<span foreground="brown">frequency</span>, '
     '<span foreground="brown">duration</span>, '
     '<span foreground="brown">volume</span>, '
     '<span foreground="brown">loop</span>)</b>\n\n'
     'Play a tone with extra options.\n'
     'Play a single tone of the specified frequency, duration and '
     'volume. The frequency is in Hz (see the Tone constants group). '
     'The duration is in 1000ths of a second (see the Time constants group). '
     'Volume should be a number from 0 (silent) to 4 (loudest). '
     'Play the tone repeatedly if loop is true.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">frequency</span>\tThe desired tone frequency, in Hz.\n'
     '\t<span foreground="brown">duration</span>\tThe desired tone duration, in ms.\n'
     '\t<span foreground="brown">volume</span>\tThe desired tone volume.\n'
     '\t<span foreground="brown">loop</span>\tA boolean flag indicating whether to\n'
     '\t\tplay the tone repeatedly.\n'
     '<b>Example:</b>\n'
     '\tPlayToneEx(440, 500, 2, false);'), 'Sound'],
    ['PlayFile', 'PlayFile(filename)',
     ('<b>PlayFile (<span foreground="brown">filename</span> )</b>\n\n'
     'Play the specified file. The sound file can either be '
     'an RSO file or it can be an NXT melody (RMD) file containing '
     'frequency and duration values.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">filename</span>\tThe name of the sound or melody file to play.\n'
     '<b>Example:</b>\n'
     '\tPlayFile("! Startup.rso");'), 'Sound'],
    ['PlayFileEx', 'PlayFileEx(filename, volume, loop)',
     ('<b>PlayFileEx('
     '<span foreground="brown">filename</span>, '
     '<span foreground="brown">volume</span>, '
     '<span foreground="brown">loop</span>)</b>\n\n'
     'Play a file with extra options.\n'
     'Play the specified file. Volume should be a number '
     'from 0 (silent) to 4 (loudest). Play the file repeatedly '
     'if loop is true. The sound file can either be an RSO file '
     'or it can be an NXT melody (RMD) file.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">filename</span>\tThe name of the sound or melody file to play.\n'
     '\t<span foreground="brown">volume</span>\tThe desired tone volume.\n'
     '\t<span foreground="brown">loop</span>\tA boolean flag indicating whether to play the\n'
     '\t\tfile repeatedly.\n'
     '<b>Example:</b>\n'
     '\tPlayFileEx("! Startup.rso", 3, true);'), 'Sound'],
    ['PointOut', 'PointOut(x, y)',
     ('<b>PointOut (<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">options</span> = DRAW_OPT_NORMAL)</b>\n\n'
     'This function lets you draw a point on the screen at x, y. '
     'Optionally specify drawing options. If this argument is not '
     'specified it defaults to DRAW_OPT_NORMAL.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">x</span>\tThe x value for the point.\n'
     '\t<span foreground="brown">y</span>\tThe y value for the point.\n'
     '\t<span foreground="brown">options</span>\tThe optional drawing options.\n'
     '\t\t<b><span foreground="red">Warning:</span></b> These options require the\n'
     '\t\tenhanced NBC/NXC firmware\n'
     '<b>Example:</b>\n'
     '\tPointOut(40, 40);'), 'Display'],
    ['Precedes', 'Precedes(tasks)',
     ('<b>Precedes ('
     '<span foreground="brown">task1</span>, '
     '<span foreground="brown">task2</span>, '
     '..., <span foreground="brown">taskN</span>)</b>\n\n'
     'Schedule the listed tasks for execution once the current task has '
     'completed executing. The tasks will all execute simultaneously '
     'unless other dependencies prevent them from doing. '
     'This statement should be used once within a task, preferably at '
     'the start of the task definition. Any number of tasks may be listed '
     'in the Precedes statement.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">task1</span>\tThe first task to start after the current task ends.\n'
     '\t<span foreground="brown">task2</span>\tThe second task to start after the current task ends.\n'
     '\t<span foreground="brown">taskN</span>\tThe last task to start after the current task ends.\n'
     '<b>Example:</b>\n'
     '\tPrecedes(moving, drawing, playing);'), 'Command'],
    ['Random', 'Random()',
     ('<b>Random (<span foreground="brown">n = 0</span>)</b>\n\n'
     'Generate random number. The returned value will range '
     'between 0 and n (exclusive).\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">n</span>\tThe maximum unsigned value desired (optional).\n'
     '<b>Example:</b>\n'
     '\tint x = Random(100); // unsigned int 0..99\n'
     '\tint x = Random(); // signed int -32767..32767'), 'C API'],
    ['RectOut', 'RectOut(x, y, width, height)',
     ('<b>RectOut (<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">width</span>, '
     '<span foreground="brown">height</span>, '
     '<span foreground="brown">options</span>'
     ' = DRAW_OPT_NORMAL)</b>\n\n'
     'This function draws a rectangle on the screen at x, y with the '
     'specified width and height. Optionally specify drawing options. '
     'If this argument is not specified it defaults to DRAW_OPT_NORMAL.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">x</span>\tThe x value for the top left corner of the rectangle.\n'
     '\t<span foreground="brown">y</span>\tThe y value for the top left corner of the rectangle.\n'
     '\t<span foreground="brown">width</span>\tThe width of the rectangle.\n'
     '\t<span foreground="brown">height</span>\tThe height of the rectangle.\n'
     '\t<span foreground="brown">options</span>\tThe optional drawing options.\n'
     '\t\t<b><span foreground="red">Warning:</span></b> These options require the\n'
     '\t\tenhanced NBC/NXC firmware\n'
     '<b>Example:</b>\n'
     '\tRectOut(40, 40, 30, 10);'), 'Display'],
    ['Release', 'Release(m)',
     ('<b>Release (mutex <span foreground="brown">m</span>)</b>\n\n'
     'Release the specified mutex variable. Use this to relinquish '
     'a mutex so that it can be acquired by another task. Release '
     'should always be called after a matching call to Acquire and '
     'as soon as possible after a shared resource is no longer needed.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">m</span>\tThe mutex to release.\n'
     '<b>Example:</b>\n'
     '\tAcquire(motorMutex); // make sure we have exclusive access\n'
     '\t// use the motors\n'
     '\tRelease(motorMutex); // release mutex for other tasks'), 'Command'],
    ['RenameFile', 'RenameFile(oldname, newname)',
     ('<b>RenameFile('
     '<span foreground="brown">oldname</span>, '
     '<span foreground="brown">newname</span>)</b>\n\n'
     'Rename a file from the old filename to the new filename. The '
     'loader result code is returned as the value of the function call. '
     'The filename parameters must be constants or variables.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">oldname</span>\tThe old filename.\n'
     '\t<span foreground="brown">newname</span>\tThe new filename.\n'
     '<b>Returns</b>\n'
     '\tThe function call result. See Loader module error codes.\n'
     '<b>Example:</b>\n'
     '\tresult = RenameFile("data.txt", "mydata.txt");'), 'Loader'],
    ['ResetScreen', 'ResetScreen()',
     ('<b>ResetScreen ()</b>\n\n'
     'Reset LCD screen. This function lets you restore '
     'the standard NXT running program screen.\n\n'
     '<b>Example:</b>\n'
     '\tResetScreen();'), 'Display'],
    ['ResetSensor', 'ResetSensor(port)',
     ('<b>ResetSensor (<span foreground="brown">port</span>)</b>\n\n'
     'Reset the sensor port. Sets the invalid data flag on the specified '
     'port and waits for it to become valid again. After changing the type '
     'or the mode of a sensor port you must call this function to give the '
     'firmware time to reconfigure the sensor port.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to reset.\n'
     '<b>Example:</b>\n'
     '\tResetSensor(S1);'), 'Input'],
    ['ResetRotationCount', 'ResetRotationCount(outputs)',
     ('<b>ResetRotationCount ('
     '<span foreground="brown">outputs</span>)</b>\n\n'
     'Reset the program-relative position counter for the '
     'specified outputs.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '<b>Example:</b>\n'
     '\tResetRotationCount(OUT_AB);'), 'Output'],
    ['ResetTachoCount', 'ResetTachoCount(outputs)',
     ('<b>ResetTachoCount ('
     '<span foreground="brown">outputs</span>)</b>\n\n'
     'Reset the tachometer count and tachometer limit goal '
     'for the specified outputs.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '<b>Example:</b>\n'
     '\tResetTachoCount(OUT_AB);'), 'Output'],
    ['ResetAllTachoCounts', 'ResetAllTachoCounts(outputs)',
     ('<b>ResetAllTachoCounts('
     '<span foreground="brown">outputs</span>)</b>\n\n'
     'Reset all tachometer counters.\n'
     'Reset all three position counters and reset the current '
     'tachometer limit goal for the specified outputs.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '<b>Example:</b>\n'
     '\tResetAllTachoCounts(OUT_AB);'), 'Output'],
    ['RotateMotor', 'RotateMotor(outputs, pwr, angle)',
     ('<b>RotateMotor ('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">angle</span>)</b>\n\n'
     'Rotate motor. Run the specified outputs forward for the '
     'specified number of degrees.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">angle</span>\tAngle limit, in degree.\n'
     '\t\tCan be negative to reverse direction.\n'
     '<b>Example:</b>\n'
     '\tRotateMotor(OUT_A, 75, 45);  // forward 45 degrees\n'
     '\tRotateMotor(OUT_A, -75, 45); // reverse 45 degrees'), 'Output'],
    ['RotateMotorEx', 'RotateMotorEx(outputs, pwr, angle, turnpct, sync, stop)',
     ('<b>RotateMotorEx (<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">angle</span>, '
     '<span foreground="brown">turnpct</span>, '
     '<span foreground="brown">sync</span>, '
     '<span foreground="brown">stop</span>)</b>\n\n'
     'Run the specified outputs forward for the specified number '
     'of degrees. Also specify synchronization, turn percentage, '
     'and braking options. Use this function primarily with more '
     'than one motor specified via the outputs parameter.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">angle</span>\tAngle limit, in degree.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">turnpct</span>\tTurn ratio, -100 to 100.\n'
     '\t<span foreground="brown">sync</span>\tSynchronise two motors. Should be set to true\n'
     '\t\tif a non-zero turn percent is specified\n'
     '\t\tor no turning will occur.\n'
     '\t<span foreground="brown">stop</span>\tSpecify whether the motor(s) should brake at \n'
     '\t\tthe end of the rotation.\n'
     '<b>Example:</b>:\n'
     '\tRotateMotorEx(OUT_AB, 75, 360, 50, true, true);'), 'Output'],
    ['RotateMotorPID', 'RotateMotorPID(outputs, pwr, angle, p, i, d)',
     ('<b>RotateMotorPID('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">angle</span>, '
     '<span foreground="brown">p</span>, '
     '<span foreground="brown">i</span>, '
     '<span foreground="brown">d</span>)</b>\n\n'
     'Rotate motor with PID factors.\n'
     'Run the specified outputs forward for the specified '
     'number of degrees. Specify proportional, integral '
     'and derivative factors.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">angle</span>\tAngle limit, in degree.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">p</span>\tProportional factor.\n'
     '\t<span foreground="brown">i</span>\tIntegral factor.\n'
     '\t<span foreground="brown">d</span>\tDerivative factor.\n'
     '<b>Example:</b>\n'
     '\tRotateMotorPID(OUT_A, 75, 45, 20, 40, 100);'), 'Output'],
    ['RotateMotorExPID', 'RotateMotorExPID(outputs, pwr, angle, turnpct, sync, stop, p, i, d)',
     ('<b>RotateMotorExPID('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">pwr</span>, '
     '<span foreground="brown">angle</span>, '
     '<span foreground="brown">turnpct</span>, '
     '<span foreground="brown">sync</span>, '
     '<span foreground="brown">stop</span>, '
     '<span foreground="brown">p</span>, '
     '<span foreground="brown">i</span>, '
     '<span foreground="brown">d</span>)</b>\n\n'
     'Rotate motor Ex with PID factors.\n'
     'Run the specified outputs forward for the specified '
     'number of degrees. Specify proportional, integral and '
     'derivative factors. Also specify synchronization, '
     'turn percentage, and braking options. Use this function '
     'primarily with more than one motor specified via the '
     'outputs parameter.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">pwr</span>\tOutput power, 0 to 100.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">angle</span>\tAngle limit, in degree.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">turnpct</span>\tTurn ratio, -100 to 100.\n'
     '\t<span foreground="brown">sync</span>\tSynchronise two motors. Should be set\n'
     '\t\tto true if a non-zero turn percent is\n'
     '\t\tspecified or no turning will occur.\n'
     '\t<span foreground="brown">stop</span>\tSpecify whether the motor(s) should\n'
     '\t\tbrake at the end of the rotation.\n'
     '\t<span foreground="brown">p</span>\tProportional factor.\n'
     '\t<span foreground="brown">i</span>\tIntegral factor.\n'
     '\t<span foreground="brown">d</span>\tDerivative factor.\n'
     '<b>Example:</b>\n'
     '\tRotateMotorExPID(OUT_AB, 75, 360, 50, true, true, 30, 50, 90);'), 'Output'],
    ['ReadLn', 'ReadLn(handle, value)',
     ('<b>ReadLn('
     '<span foreground="brown">handle</span>, '
     '<span foreground="brown">value</span>)</b>\n\n'
     'Read a value from a file plus line ending.\n'
     'Read a value from the file associated with the specified handle. '
     'The handle parameter must be a variable. The value parameter must '
     'be a variable. The type of the value parameter determines the '
     'number of bytes of data read. The ReadLn function reads two additional '
     'bytes from the file which it assumes are a carriage return and line feed pair.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">handle</span>\tThe file handle.\n'
     '\t<span foreground="brown">value</span>\tThe variable to store the data read from the file.\n'
     '<b>Returns</b>\n'
     '\tThe function call result.\n'
     '<b>Example:</b>:\n'
     '\tresult = ReadLn(handle, value);'), 'Loader'],
    ['ReadLnString', 'ReadLnString(handle, output)',
     ('<b>ReadLnString('
     '<span foreground="brown">handle</span>, '
     '<span foreground="brown">output</span>)</b>\n\n'
     'Read a string from a file plus line ending.\n'
     'Read a string from the file associated with the specified handle. '
     'The handle parameter must be a variable. The output parameter must '
     'be a variable. Appends bytes to the output variable until a line '
     'ending (CRLF) is reached. The line ending is also read but it is not '
     'appended to the output parameter.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">handle</span>\tThe file handle.\n'
     '\t<span foreground="brown">output</span>\tThe variable to store the string read from the file.\n'
     '<b>Returns</b>\n'
     '\tThe function call result'), 'Loader'],
    ['ReceiveRemoteNumber', 'ReceiveRemoteNumber(queue, clear, val)',
     ('<b>ReceiveRemoteNumber ('
     '<span foreground="brown">queue</span>, '
     '<span foreground="brown">clear</span>, '
     '<span foreground="brown">val</span>)</b>\n\n'
     'Read a numeric value from a mailbox and optionally remove it. '
     'If the local mailbox is empty and this NXT is the master then '
     'it attempts to poll one of its slave NXTs for a message from '
     'the response mailbox that corresponds to the specified local '
     'mailbox number.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">queue</span>\tThe mailbox number.\n'
     '\t<span foreground="brown">clear</span>\tA flag indicating whether to remove the message from\n'
     '\t\tthe mailbox after it has been read.\n'
     '\t<span foreground="brown">val</span>\tThe numeric value that is read from the mailbox.\n'
     '<b>Returns</b>\n'
     '\tA char value indicating whether the function call succeeded or not.\n'
     '<b>Example:</b>\n'
     '\tx = ReceiveRemoteNumber(queue, true, val);'), 'Communication'],
    ['ReceiveRemoteString', 'ReceiveRemoteString(queue, clear, str)',
     ('<b>ReceiveRemoteString ('
     '<span foreground="brown">queue</span>, '
     '<span foreground="brown">clear</span>, '
     '<span foreground="brown">str</span>)</b>\n\n'
     'Read a string value from a mailbox and optionally remove it. '
     'If the local mailbox is empty and this NXT is the master then '
     'it attempts to poll one of its slave NXTs for a message from '
     'the response mailbox that corresponds to the specified local '
     'mailbox number.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">queue</span>\tThe mailbox number.\n'
     '\t<span foreground="brown">clear</span>\tA flag indicating whether to remove the message from\n'
     '\t\tthe mailbox after it has been read.\n'
     '\t<span foreground="brown">str</span>\tThe string value that is read from the mailbox.\n'
     '<b>Returns</b>\n'
     '\tA char value indicating whether the function call succeeded or not.\n'
     '<b>Example:</b>\n'
     '\tx = ReceiveRemoteString(queue, true, strval);'), 'Communication'],
    ['RemoteConnectionIdle', 'RemoteConnectionIdle(conn)',
     'RemoteConnectionIdle(conn)', 'Communication'],
    ['RemotePlayTone', 'RemotePlayTone(conn, frequency, duration)',
     'RemotePlayTone(conn, frequency, duration)', 'Communication'],
    ['RemotePlaySoundFile', 'RemotePlaySoundFile(conn, filename, bloop)',
     'RemotePlaySoundFile(conn, filename, bloop)', 'Communication'],
    ['RemoteResetMotorPosition', 'RemoteResetMotorPosition(conn, port, brelative)',
     'RemoteResetMotorPosition(conn, port, brelative)', 'Communication'],
    ['RemoteStartProgramm', 'RemoteStartProgramm(conn, filename)',
     'RemoteStartProgramm(conn, filename)', 'Communication'],
    ['RemoteStopProgramm', 'RemoteStopProgramm(conn)',
     'RemoteStopProgramm(conn)', 'Communication'],
    ['RemoteStopSound', 'RemoteStopSound(conn)',
     'RemoteStopSound(conn)', 'Communication'],
    ['Sensor', 'Sensor(port)',
     ('<b>Sensor (<span foreground="brown">port</span>)</b>\n\n'
     'Return the processed sensor reading for a sensor on the specified port.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe sensor port.\n'
     '<b>Returns</b>\n'
     '\tThe sensor´s scaled value.\n'
     '<b>Example:</b>\n'
     '\tx = Sensor(IN_1); // read sensor 1'), 'Input'],
    ['SensorUS', 'SensorUS(port)',
     ('<b>SensorUS (<span foreground="brown">port</span> )</b>\n\n'
     'Read ultrasonic sensor value. Return the ultrasonic sensor distance value. '
     'Since an ultrasonic sensor is an I2C digital sensor its value cannot be '
     'read using the standard Sensor(n) value. The port must be configured as '
     'a Lowspeed port before using this function.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to which the ultrasonic sensor is attached.\n'
     '<b>Returns</b>\n'
     '\tThe ultrasonic sensor distance value (0..255)\n'
     '<b>Example:</b>\n'
     '\tSetSensorLowspeed(IN_4);\n  x = SensorUS(IN_4); // read sensor 4'), 'Input'],
    ['SetSensorTouch', 'SetSensorTouch(port)',
     ('<b>SetSensorTouch ('
     '<span foreground="brown">port</span>)</b>\n\n'
     'Configure a touch sensor on the specified Input port.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe Input port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorTouch(IN_1);'), 'Input'],
    ['SetSensorLight', 'SetSensorLight(port)',
     ('<b>SetSensorLight ('
     '<span foreground="brown">port</span>, '
     '<span foreground="brown">bActive</span> = true)</b>\n\n'
     'Configure the sensor on the specified port as an NXT light sensor.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to configure.\n'
     '\t<span foreground="brown">bActive</span>'
     '\tA boolean flag indicating whether to configure the port\n'
     '\t\tas an active or inactive light sensor. The default\n'
     '\t\tvalue for this optional parameter is true.\n'
     '<b>Example:</b>\n'
     '\tSetSensorLight(IN_1);'), 'Input'],
    ['SetSensorSound', 'SetSensorSound(port)',
     ('<b>SetSensorSound ('
     '<span foreground="brown">port</span>, '
     '<span foreground="brown">bdBScaling</span> = true)</b>\n\n'
     'Configure the sensor on the specified port as a sound sensor.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to configure.\n'
     '\t<span foreground="brown">bdBScaling</span>'
     '\tA boolean flag indicating whether to configure the\n'
     '\t\tport as a sound sensor with dB or dBA scaling.\n'
     '\t\tThe default value for this optional parameter is\n'
     '\t\ttrue, meaning dB scaling.\n'
     '<b>Example:</b>\n'
     '\tSetSensorSound(IN_1);'), 'Input'],
    ['SetSensorLowspeed', 'SetSensorLowspeed(port)',
     ('<b>SetSensorLowspeed ('
     '<span foreground="brown">port</span>, '
     '<span foreground="brown">bIsPowered</span> = true)</b>\n\n'
     'Configure an digital I2C sensor on the specified port for either '
     'powered (9 volt) or unpowered devices.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to configure.\n'
     '\t<span foreground="brown">bIsPowered</span>\tA boolean flag indicating whether to configure\n'
     '\t\tthe port for powered or unpowered I2C devices.\n'
     '\t\tDefault value is true.\n'
     '<b>Example:</b>\n'
     '\tSetSensorLowspeed(IN_1);'), 'Input'],
    ['SetSensor', 'SetSensor(port, config)',
     ('<b>SetSensor ('
     '<span foreground="brown">port</span>, '
     '<span foreground="brown">config</span>)</b>\n\n'
     'Set the type and mode of the given sensor to the specified '
     'configuration, which must be a special constant containing '
     'both type and mode information.\n\n'
     '<b>See Also</b>\n'
     '\tSetSensorType(), SetSensorMode(), and ResetSensor()\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to configure.\n'
     '\t<span foreground="brown">config</span>\tThe configuration constant containing both the type\n'
     '\t\tand mode: SENSOR_TOUCH, SENSOR_LIGHT,\n'
     '\t\tSENSOR_SOUND...\n'
     '<b>Example:</b>\n'
     '\tSetSensor(IN_1, SENSOR_TOUCH);'), 'Input'],
    ['SetSensorColorFull', 'SetSensorColorFull(port)',
     ('<b>SetSensorColorFull ('
     '<span foreground="brown">port</span>)</b>\n\n'
     'Configure an NXT 2.0 full color sensor on the specified '
     'port in full color mode.\n\n'
     '<b><span foreground="red">Warning</span></b>\n'
     '\tThis function requires an NXT 2.0 compatible firmware.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorColorFull(IN_1);'), 'Input'],
    ['SetSensorColorBlue', 'SetSensorColorBlue(port)',
     ('<b>SetSensorColorBlue ('
     '<span foreground="brown">port</span>)</b>\n\n'
     'Configure an NXT 2.0 full color sensor on the specified '
     'port in blue light mode.\n\n'
     '<b><span foreground="red">Warning</span></b>\n'
     '\tThis function requires an NXT 2.0 compatible firmware.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorColorBlue(IN_1);'), 'Input'],
    ['SetSensorColorGreen', 'SetSensorColorGreen(port)',
     ('<b>SetSensorColorGreen ('
     '<span foreground="brown">port</span>)</b>\n\n'
     'Configure an NXT 2.0 full color sensor on the specified '
     'port in green light mode.\n\n'
     '<b><span foreground="red">Warning</span></b>\n'
     '\tThis function requires an NXT 2.0 compatible firmware.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorColorGreen(IN_1);'), 'Input'],
    ['SetSensorColorRed', 'SetSensorColorRed(port)',
     ('<b>SetSensorColorRed ('
     '<span foreground="brown">port</span>)</b>\n\n'
     'Configure an NXT 2.0 full color sensor on the specified '
     'port in red light mode.\n\n'
     '<b><span foreground="red">Warning</span></b>\n'
     '\tThis function requires an NXT 2.0 compatible firmware.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorColorRed(IN_1);'), 'Input'],
    ['SetSensorColorNone', 'SetSensorColorNone(port)',
     ('<b>SetSensorColorNone ('
     '<span foreground="brown">port</span>)</b>\n\n'
     'Configure an NXT 2.0 full color sensor on the specified '
     'port in no light mode.\n\n'
     '<b><span foreground="red">Warning</span></b>\n'
     '\tThis function requires an NXT 2.0 compatible firmware.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorColorNone(IN_1);'), 'Input'],
    ['SetSensorMode', 'SetSensorMode(port, mode)',
     ('<b>SetSensorMode ('
     '<span foreground="brown">port</span>, '
     '<span foreground="brown">mode</span>)</b>\n\n'
     'Set a sensor\'s mode, which should be one of the predefined '
     'sensor mode constants. A slope parameter for boolean conversion, '
     'if desired, may be added to the mode. After changing the type '
     'or the mode of a sensor port you must call ResetSensor to give '
     'the firmware time to reconfigure the sensor port.\n\n'
     '<b>See Also</b>\n'
     '\tSetSensorType(), SetSensor()\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to configure. See Input port constants.\n'
     '\t<span foreground="brown">mode</span>\tThe desired sensor mode. Can be:\n'
     '\t\tSENSOR_MODE_RAW\tRaw value from 0 to 1023\n'
     '\t\tSENSOR_MODE_EDGE\tCounts the number of \n'
     '\t\t\tboolean transitions\n'
     '\t\tSENSOR_MODE_PULSE\tCounts the number of \n'
     '\t\t\tboolean periods\n'
     '\t\tSENSOR_MODE_PERCENT\tScaled value from 0 to 100\n'
     '\t\tSENSOR_MODE_CELSIUS\tRCX temperature sensor value \n'
     '\t\t\tin degrees celcius\n'
     '\t\tSENSOR_MODE_FAHRENHEIT\tRCX temperature sensor value in degrees fahrenheit\n'
     '\t\tSENSOR_MODE_ROTATION\tRCX rotation sensor (16 ticks per revolution)\n'
     '<b>Example:</b>\n'
     '\tSetSensorMode(IN_1, SENSOR_MODE_RAW); // raw mode'), 'Input'],
    ['SetSensorType', 'SetSensorType(port, type)',
     ('<b>SetSensorType ('
     '<span foreground="brown">port</span>, '
     '<span foreground="brown">type</span>)</b>\n\n'
     'Set a sensor\'s type, which must be one of the predefined sensor '
     'type constants. After changing the type or the mode of a sensor port '
     'you must call ResetSensor to give the firmware time to reconfigure '
     'the sensor port.\n\n'
     '<b>See Also</b>\n'
     '\tSetSensorMode(), SetSensor()\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">port</span>\tThe port to configure.\n'
     '\t<span foreground="brown">type</span>\tThe desired sensor type.\n'
     '<b>Example:</b>\n'
     '\tSetSensorType(S1, SENSOR_TYPE_TOUCH);'), 'Input'],
    ['SendRemoteNumber', 'SendRemoteNumber(conn, queue, val)',
     ('<b>SendRemoteNumber ('
     '<span foreground="brown">conn</span>, '
     '<span foreground="brown">queue</span>, '
     '<span foreground="brown">val</span>)</b>\n\n'
     'Send a numeric value on the specified connection to the specified '
     'remote mailbox number. Use RemoteConnectionIdle to determine when '
     'this write request is completed.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">conn</span>\tThe connection slot (0..4). '
     'Connections 0 through 3 are\n'
     '\t\tfor bluetooth connections. Connection 4 refers to the RS485\n'
     '\t\thi-speed port.\n'
     '\t<span foreground="brown">queue</span>\tThe mailbox number.\n'
     '\t<span foreground="brown">val</span>\tThe numeric value to send.\n'
     '<b>Returns</b>\n'
     '\tA char value indicating whether the function call succeeded or not.\n'
     '<b>Example:</b>\n'
     '\tx = SendRemoteNumber(1, MAILBOX1, 123);'), 'Communication'],
    ['SendRemoteString', 'SendRemoteString(conn, queue, str)',
     ('<b>SendRemoteString ('
     '<span foreground="brown">conn</span>, '
     '<span foreground="brown">queue</span>, '
     '<span foreground="brown">str</span>)</b>\n\n'
     'Send a string value on the specified connection to the specified '
     'remote mailbox number. Use RemoteConnectionIdle to determine when '
     'this write request is completed.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">conn</span>\tThe connection slot (0..4). '
     'Connections 0 through 3 are\n'
     '\t\tfor bluetooth connections. Connection 4 refers to the RS485\n'
     '\t\thi-speed port.\n'
     '\t<span foreground="brown">queue</span>\tThe mailbox number.\n'
     '\t<span foreground="brown">str</span>\tThe string value to send.\n'
     '<b>Returns</b>\n'
     '\tA char value indicating whether the function call succeeded or not.\n'
     '<b>Example:</b>\n'
     '\tx = SendRemoteString(1, MAILBOX1, "hello world");'), 'Communication'],
    ['SendResponseNumber', 'SendResponseNumber(queue, val)',
     ('<b>SendResponseNumber ('
     '<span foreground="brown">queue</span>, '
     '<span foreground="brown">val</span>)</b>\n\n'
     'Write a numeric value to a response mailbox (the mailbox number + 10).\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">queue</span>\tThe mailbox number. This function shifts the specified value \n'
     '\t\tinto the range of response mailbox numbers by adding 10.\n'
     '\t<span foreground="brown">val</span>\tThe numeric value to write.\n'
     '<b>Returns</b>\n'
     '\tA char value indicating whether the function call succeeded or not.\n'
     '<b>Example:</b>\n'
     '\tx = SendResponseNumber(MAILBOX1, 123);'), 'Communication'],
    ['SendResponseString', 'SendResponseString(queue, str)',
     ('<b>SendResponseString ('
     '<span foreground="brown">queue</span>, '
     '<span foreground="brown">str</span>)</b>\n\n'
     'Write a string value to a response mailbox (the mailbox number + 10).\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">queue</span>\tThe mailbox number. This function shifts the specified\n'
     '\t\tvalue into the range of response mailbox numbers by adding 10.\n'
     '\t<span foreground="brown">str</span>\tThe string value to write.\n'
     '<b>Returns</b>\n'
     '\tA char value indicating whether the function call succeeded or not.\n'
     '<b>Example:</b>\n'
     '\tx = SendResponseString(MAILBOX1, "hello world");'), 'Communication'],
    ['StartTask', 'StartTask(task)',
     ('<b>StartTask ('
     '<span foreground="brown">task</span>)</b>\n\n'
     'Start the specified task.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">task</span>\tThe task to start.\n'
     '<b>Example:</b>\n'
     '\tStartTask(sound); // start the sound task'), 'Command'],
    ['StrCat', 'StrCat(str1, str2, strN)',
     ('<b>StrCat ('
     '<span foreground="brown">str1</span>, '
     '<span foreground="brown">str2</span>, '
     '<span foreground="brown">strN</span>)</b>\n\n'
     'Return a string which is the result of concatenating all of the '
     'string arguments together. This function accepts any number of '
     'parameters which may be string variables, constants, or expressions.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">str1</span>\tThe first string.\n'
     '\t<span foreground="brown">str2</span>\tThe second string.\n'
     '\t<span foreground="brown">strN</span>\tThe Nth string.\n'
     '<b>Returns</b>\n'
     '\tThe concatenated string.\n'
     '<b>Example:</b>\n'
     '\tstr1 = "Put";\n'
     '\tstr2 = "me";\n'
     '\tstr3 = "together";\n'
     '\TextOut(0, LCD_LINE1, StrCat(str1, str2, str3));'), 'C API'],
    ['StrLen', 'StrLen(str)',
     ('<b>StrLen ('
     '<span foreground="brown">str</span>)</b>\n\n'
     'Return the length of the specified string. The input string '
     'parameter may be a variable, constant, or expression.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">str</span>   A string.\n'
     '<b>Returns</b>\n'
     '\tThe length of the string.\n'
     '<b>Example:</b>\n'
     '\tstring msg = "hi there";\n'
     '\tbyte x = StrLen(msg); // return the length of msg'), 'C API'],
    ['StrToNum', 'StrToNum(str)',
     ('<b>StrToNum (<span foreground="brown">str</span>)</b>\n\n'
     'Return the numeric value specified by the string passed to the '
     'function. If the content of the string is not a numeric value '
     'then this function returns zero. The input string parameter may '
     'be a variable, constant, or expression.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">str</span>\tA string.\n'
     '<b>Returns</b>\n'
     '\tA number.\n'
     '<b>Example:</b>\n'
     '\tx = StrToNum(str);'), 'C API'],
    ['TextOut', 'TextOut(x, y, str)',
     ('<b>TextOut (' 
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">str</span>)</b>\n\n'
     'Draw a text value on the screen at the specified x and y location. '
     'The y value must be a multiple of 8.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">x</span>\tThe x value for the start of the number output.\n'
     '\t<span foreground="brown">y</span>\tThe text line number for the number output.\n'
     '\t<span foreground="brown">str</span>\tThe text to output to the LCD screen.\n'
     '<b>Example:</b>\n'
     '\tTextOut(0, <span foreground="green">LCD_LINE1</span>, "Hello World!");'), 'Display'],
    ['Off', 'Off(outputs)',
     ('<b>Off (<span foreground="brown">outputs</span>)</b>\n\n'
     'Turn motors off. Turn the specified outputs off (with braking).\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '<b>Example:</b>\n'
     '\tOff(OUT_A); // turn off output A'), 'Output'],
    ['OpenFileRead', 'OpenFileRead(fname, fsize, handle)',
     ('<b>OpenFileRead ('
     '<span foreground="brown">fname</span>, '
     '<span foreground="brown">fsize</span>, '
     '<span foreground="brown">handle</span>)</b>\n\n'
     'Open an existing file with the specified filename for reading. '
     'The file size is returned in the second parameter, which must be '
     'a variable. The file handle is returned in the last parameter, '
     'which must be a variable. The loader result code is returned as '
     'the value of the function call.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">fname</span>\tThe name of the file to open.\n'
     '\t<span foreground="brown">fsize</span>\tThe size of the file returned by the function.\n'
     '\t<span foreground="brown">handle</span>\tThe file handle output from the function call.\n'
     '<b>Example:</b>\n'
     '\tresult = OpenFileRead("data.txt", fsize, handle);'), 'Loader'],
    ['Wait', 'Wait(ms)',
     ('<b>Wait (<span foreground="brown">ms</span>)</b>\n\n'
     'Make a task sleep for specified amount of time.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">ms</span>\tThe number of milliseconds to sleep.\n'
     '<b>Example:</b>\n'
     '\tWait(1000);'), 'Command'],
    ['WriteBytes', 'WriteBytes(handle, buf, cnt)',
     ('<b>WriteBytes('
     '<span foreground="brown">handle</span>, '
     '<span foreground="brown">buf</span>, '
     '<span foreground="brown">cnt</span>)</b>\n\n'
     'Write the contents of the data array to the file associated with the specified '
     'handle. The handle parameter must be a variable. The cnt parameter must be a '
     'variable. The data parameter must be a byte array. The actual number of bytes '
     'written is returned in the cnt parameter.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">handle</span>\tThe file handle.\n'
     '\t<span foreground="brown">buf</span>\tThe byte array or string containing the data to write.\n'
     '\t<span foreground="brown">cnt</span>\tThe number of bytes actually written to the file.\n'
     '<b>Example:</b>\n'
     '\tresult = WriteBytes(handle, buffer, count);'), 'Loader'],
    ['WriteLn', 'WriteLn(handle, value)',
     ('<b>WriteLn('
     '<span foreground="brown">handle</span>, '
     '<span foreground="brown">value</span>)</b>\n\n'
     'Write a value to the file associated with the specified handle. The handle parameter '
     'must be a variable. The value parameter must be a constant, a constant expression, '
     'or a variable. The type of the value parameter determines the number of bytes of data '
     'written. This function also writes a carriage return and a line feed to the file '
     'following the numeric data.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">handle</span>\tThe file handle.\n'
     '\t<span foreground="brown">value</span>\tThe value to write to the file.\n'
     '<b>Example:</b>\n'
     '\tresult = WriteLn(handle, value);'), 'Loader'],
    ['WriteLnString', 'WriteLnString(handle, str, cnt)',
     ('<b>WriteLnString('
     '<span foreground="brown">handle</span>, '
     '<span foreground="brown">str</span>, '
     '<span foreground="brown">cnt</span>)</b>\n\n'
     'Write the string to the file associated with the specified handle. The handle parameter '
     'must be a variable. The count parameter must be a variable. The str parameter must be '
     'a string variable or string constant. This function also writes a carriage return and a '
     'line feed to the file following the string data. The total number of bytes written is '
     'returned in the cnt parameter.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">handle</span>\tThe file handle.\n'
     '\t<span foreground="brown">str</span>\tThe string to write to the file.\n'
     '\t<span foreground="brown">cnt</span>\tThe number of bytes actually written to the file.\n'
     '<b>Example:</b>\n'
     '\tresult = WriteLnString(handle, "testing", count);'), 'Loader']
]

NXC_CONSTS = [
    ['BTNEXIT', 'BTNEXIT'],
    ['BTNRIGHT', 'BTNRIGHT'],
    ['BTNLEFT', 'BTNLEFT'],
    ['BTNCENTER', 'BTNCENTER'],
    ['BTN1', 'BTN1'],
    ['BTN2', 'BTN2'],
    ['BTN3', 'BTN3'],
    ['BTN4', 'BTN4'],
    ['DISPLAY_WIDTH', 'DISPLAY_WIDTH'],
    ['DISPLAY_HEIGHT', 'DISPLAY_HEIGHT'],
    ['DRAW_OPT_NORMAL', 'DRAW_OPT_NORMAL'],
    ['DRAW_OPT_CLEAR_WHOLE_SCREEN', 'DRAW_OPT_CLEAR_WHOLE_SCREEN'],
    ['DRAW_OPT_CLEAR_EXCEPT_STATUS_SCREEN', 'DRAW_OPT_CLEAR_EXCEPT_STATUS_SCREEN'],
    ['DRAW_OPT_CLEAR_PIXELS', 'DRAW_OPT_CLEAR_PIXELS'],
    ['DRAW_OPT_CLEAR', 'DRAW_OPT_CLEAR'],
    ['DRAW_OPT_INVERT', 'DRAW_OPT_INVERT'],
    ['DRAW_OPT_LOGICAL_COPY', 'DRAW_OPT_LOGICAL_COPY'],
    ['DRAW_OPT_LOGICAL_AND', 'DRAW_OPT_LOGICAL_AND'],
    ['DRAW_OPT_LOGICAL_OR', 'DRAW_OPT_LOGICAL_OR'],
    ['DRAW_OPT_LOGICAL_XOR', 'DRAW_OPT_LOGICAL_XOR'],
    ['DRAW_OPT_FILL_SHAPE', 'DRAW_OPT_FILL_SHAPE'],
    ['DRAW_OPT_CLEAR_SCREEN_MODES', 'DRAW_OPT_CLEAR_SCREEN_MODES'],
    ['DRAW_OPT_LOGICAL_OPERATIONS', 'DRAW_OPT_LOGICAL_OPERATIONS'],
    ['DRAW_OPT_POLYGON_POLYLINE', 'DRAW_OPT_POLYGON_POLYLINE'],
    ['DRAW_OPT_CLEAR_LINE', 'DRAW_OPT_CLEAR_LINE'],
    ['DRAW_OPT_CLEAR_EOL', 'DRAW_OPT_CLEAR_EOL'],
    ['IN_1', 'IN_1'],
    ['IN_2', 'IN_2'],
    ['IN_3', 'IN_3'],
    ['IN_4', 'IN_4'],
    ['LCD_LINE1', 'LCD_LINE1'],
    ['LCD_LINE2', 'LCD_LINE2'],
    ['LCD_LINE3', 'LCD_LINE3'],
    ['LCD_LINE4', 'LCD_LINE4'],
    ['LCD_LINE5', 'LCD_LINE5'],
    ['LCD_LINE6', 'LCD_LINE6'],
    ['LCD_LINE7', 'LCD_LINE7'],
    ['LCD_LINE8', 'LCD_LINE8'],
    ['NO_ERR', 'NO_ERR'],
    ['OUT_A', 'OUT_A'],
    ['OUT_B', 'OUT_B'],
    ['OUT_C', 'OUT_C'],
    ['OUT_AB', 'OUT_AB'],
    ['OUT_AC', 'OUT_AC'],
    ['OUT_BC', 'OUT_BC'],
    ['OUT_ABC', 'OUT_ABC'],
    ['OUT_MODE_BRAKE', 'OUT_MODE_BRAKE'],
    ['OUT_MODE_COAST', 'OUT_MODE_COAST'],
    ['OUT_MODE_MOTORON', 'OUT_MODE_MOTORON'],
    ['OUT_MODE_REGMETHOD', 'OUT_MODE_REGMETHOD'],
    ['OUT_MODE_REGULATED', 'OUT_MODE_REGULATED'],
    ['OUT_REGMODE_IDLE', 'OUT_REGMODE_IDLE'],
    ['OUT_REGMODE_POS', 'OUT_REGMODE_POS'],
    ['OUT_REGMODE_SPEED', 'OUT_REGMODE_SPEED'],
    ['OUT_REGMODE_SYNC', 'OUT_REGMODE_SYNC'],
    ['OUT_REGOPTION_NO_SATURATION', 'OUT_REGOPTION_NO_SATURATION'],
    ['OUT_RUNSTATE_HOLD', 'OUT_RUNSTATE_HOLD'],
    ['OUT_RUNSTATE_IDLE', 'OUT_RUNSTATE_IDLE'],
    ['OUT_RUNSTATE_RAMPDOWN', 'OUT_RUNSTATE_RAMPDOWN'],
    ['OUT_RUNSTATE_RAMPUP', 'OUT_RUNSTATE_RAMPUP'],
    ['OUT_RUNSTATE_RUNNING', 'OUT_RUNSTATE_RUNNING'],
    ['SENSOR_1', 'SENSOR_1'],
    ['SENSOR_2', 'SENSOR_2'],
    ['SENSOR_3', 'SENSOR_3'],
    ['SENSOR_4', 'SENSOR_4'],
    ['SENSOR_CELSIUS', 'SENSOR_CELSIUS'],
    ['SENSOR_COLORBLUE', 'SENSOR_COLORBLUE'],
    ['SENSOR_COLORFULL', 'SENSOR_COLORFULL'],
    ['SENSOR_COLORGREEN', 'SENSOR_COLORGREEN'],
    ['SENSOR_COLORNONE', 'SENSOR_COLORNONE'],
    ['SENSOR_COLORRED', 'SENSOR_COLORRED'],
    ['SENSOR_EDGE', 'SENSOR_EDGE'],
    ['SENSOR_FAHRENHEIT', 'SENSOR_FAHRENHEIT'],
    ['SENSOR_LIGHT', 'SENSOR_LIGHT'],
    ['SENSOR_LOWSPEED', 'SENSOR_LOWSPEED'],
    ['SENSOR_LOWSPEED_9V', 'SENSOR_LOWSPEED_9V'],
    ['SENSOR_MODE_BOOL', 'SENSOR_MODE_BOOL'],
    ['SENSOR_MODE_CELSIUS', 'SENSOR_MODE_CELSIUS'],
    ['SENSOR_MODE_EDGE', 'SENSOR_MODE_EDGE'],
    ['SENSOR_MODE_FAHRENHEIT', 'SENSOR_MODE_FAHRENHEIT'],
    ['SENSOR_MODE_PERCENT', 'SENSOR_MODE_PERCENT'],
    ['SENSOR_MODE_PULSE', 'SENSOR_MODE_PULSE'],
    ['SENSOR_MODE_RAW', 'SENSOR_MODE_RAW'],
    ['SENSOR_MODE_ROTATION', 'SENSOR_MODE_ROTATION'],
    ['SENSOR_SOUND', 'SENSOR_SOUND'],
    ['SENSOR_TOUCH', 'SENSOR_TOUCH'],
    ['SENSOR_TYPE_NONE', 'SENSOR_TYPE_NONE'],
    ['SENSOR_TYPE_TOUCH', 'SENSOR_TYPE_TOUCH'],
    ['SENSOR_TYPE_TEMPERATURE', 'SENSOR_TYPE_TEMPERATURE'],
    ['SENSOR_TYPE_LIGHT', 'SENSOR_TYPE_LIGHT'],
    ['SENSOR_TYPE_ROTATION', 'SENSOR_TYPE_ROTATION'],
    ['SENSOR_TYPE_LIGHT_ACTIVE', 'SENSOR_TYPE_LIGHT_ACTIVE'],
    ['SENSOR_TYPE_LIGHT_INACTIVE', 'SENSOR_TYPE_LIGHT_INACTIVE'],
    ['SENSOR_TYPE_SOUND_DB', 'SENSOR_TYPE_SOUND_DB'],
    ['SENSOR_TYPE_SOUND_DBA', 'SENSOR_TYPE_SOUND_DBA'],
    ['SENSOR_TYPE_CUSTOM', 'SENSOR_TYPE_CUSTOM'],
    ['SENSOR_TYPE_LOWSPEED', 'SENSOR_TYPE_LOWSPEED'],
    ['SENSOR_TYPE_LOWSPEED_9V', 'SENSOR_TYPE_LOWSPEED_9V'],
    ['SENSOR_TYPE_HIGHSPEED', 'SENSOR_TYPE_HIGHSPEED'],
    ['SENSOR_TYPE_COLORFULL', 'SENSOR_TYPE_COLORFULL'],
    ['SENSOR_TYPE_COLORRED', 'SENSOR_TYPE_COLORRED'],
    ['SENSOR_TYPE_COLORGREEN', 'SENSOR_TYPE_COLORGREEN'],
    ['SENSOR_TYPE_COLORBLUE', 'SENSOR_TYPE_COLORBLUE'],
    ['SENSOR_TYPE_COLORNONE', 'SENSOR_TYPE_COLORNONE'],
    ['STAT_MSG_EMPTY_MAILBOX', 'STAT_MSG_EMPTY_MAILBOX'],
    ['SOUND_CLICK', 'SOUND_CLICK'],
    ['SOUND_DOUBLE_BEEP', 'SOUND_DOUBLE_BEEP'],
    ['SOUND_DOWN', 'SOUND_DOWN'],
    ['SOUND_FAST_UP', 'SOUND_FAST_UP'],
    ['SOUND_LOW_BEEP', 'SOUND_LOW_BEEP'],
    ['SOUND_UP', 'SOUND_UP'],
    ['TONE_C3', 'TONE_C3'],
    ['TONE_CS3', 'TONE_CS3'],
    ['TONE_D3', 'TONE_D3'],
    ['TONE_DS3', 'TONE_DS3'],
    ['TONE_E3', 'TONE_E3'],
    ['TONE_F3', 'TONE_F3'],
    ['TONE_FS3', 'TONE_FS3'],
    ['TONE_G3', 'TONE_G3'],
    ['TONE_GS3', 'TONE_GS3'],
    ['TONE_A3', 'TONE_A3'],
    ['TONE_AS3', 'TONE_AS3'],
    ['TONE_B3', 'TONE_B3'],
    ['TONE_C4', 'TONE_C4'],
    ['TONE_CS4', 'TONE_CS4'],
    ['TONE_D4', 'TONE_D4'],
    ['TONE_DS4', 'TONE_DS4'],
    ['TONE_E4', 'TONE_E4'],
    ['TONE_F4', 'TONE_F4'],
    ['TONE_FS4', 'TONE_FS4'],
    ['TONE_G4', 'TONE_G4'],
    ['TONE_GS4', 'TONE_GS4'],
    ['TONE_A4', 'TONE_A4'],
    ['TONE_AS4', 'TONE_AS4'],
    ['TONE_B4', 'TONE_B4'],
    ['TONE_C5', 'TONE_C5'],
    ['TONE_CS5', 'TONE_CS5'],
    ['TONE_D5', 'TONE_D5'],
    ['TONE_DS5', 'TONE_DS5'],
    ['TONE_E5', 'TONE_E5'],
    ['TONE_F5', 'TONE_F5'],
    ['TONE_FS5', 'TONE_FS5'],
    ['TONE_G5', 'TONE_G5'],
    ['TONE_GS5', 'TONE_GS5'],
    ['TONE_A5', 'TONE_A5'],
    ['TONE_AS5', 'TONE_AS5'],
    ['TONE_B5', 'TONE_B5'],
    ['TONE_C6', 'TONE_C6'],
    ['TONE_CS6', 'TONE_CS6'],
    ['TONE_D6', 'TONE_D6'],
    ['TONE_DS6', 'TONE_DS6'],
    ['TONE_E6', 'TONE_E6'],
    ['TONE_F6', 'TONE_F6'],
    ['TONE_FS6', 'TONE_FS6'],
    ['TONE_G6', 'TONE_G6'],
    ['TONE_GS6', 'TONE_GS6'],
    ['TONE_A6', 'TONE_A6'],
    ['TONE_AS6', 'TONE_AS6'],
    ['TONE_B6', 'TONE_B6'],
    ['TONE_C7', 'TONE_C7'],
    ['TONE_CS7', 'TONE_CS7'],
    ['TONE_D7', 'TONE_D7'],
    ['TONE_DS7', 'TONE_DS7'],
    ['TONE_E7', 'TONE_E7'],
    ['TONE_F7', 'TONE_F7'],
    ['TONE_FS7', 'TONE_FS7'],
    ['TONE_G7', 'TONE_G7'],
    ['TONE_GS7', 'TONE_GS7'],
    ['TONE_A7', 'TONE_A7'],
    ['TONE_AS7', 'TONE_AS7'],
    ['TONE_B7', 'TONE_B7'],
    ['NOTE_WHOLE', 'NOTE_WHOLE'],
    ['NOTE_HALF', 'NOTE_HALF'],
    ['NOTE_QUARTER', 'NOTE_QUARTER'],
    ['NOTE_EIGHT', 'NOTE_EIGHT'],
    ['NOTE_SIXTEEN', 'NOTE_SIXTEEN']
]
