# -*- coding: utf-8 -*-

''' EVC-Functions and -Constants for Completion and Api-viewer'''

# Copyright (C) 2017-20 Bernd Sellentin <sel@gge-em.org>
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

EVC_FUNCS = [
    ['InitEV3', 'InitEV3()', ('<b>InitEV3()</b>\n\n'
     'Initialization of all EV3-Functions. '
     'Should be the first command in main.\n\n'
     '<b>Example:</b>\n'
     '\t#include "ev3.h"\n'
     '\tint main(){\n'
     '\t    InitEV3();\n'
     '\t    // do something\n'
     '\t    FreeEV3();\n'
     '\t    return 0;\n'
     '\t}'), 'General'],
    #['CloseEV3', 'CloseEV3()', 'CloseEV3()\n', 'General'],
    #['ExitEV3', 'ExitEV3()', 'ExitEV3()\n', 'General'],
    ['FreeEV3', 'FreeEV3()', ('<b>FreeEV3()</b>\n\n'
     'Close and exit of all EV3-Functions'), 'General'],
    ['ButtonIsDown', 'ButtonIsDown(button)', ('<b>ButtonIsDown('
     '<span foreground="brown">button</span>)</b>\n\n'
     'Check if button is pressed or not.\n'
     'Returns 1: true, 0: false\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">button</span>\tBTNEXIT\tBTN1 The exit (escape) button.\n'
     '\t\tBTNRIGHT\tBTN2 The right button.\n'
     '\t\tBTNLEFT\tBTN3 The left button.\n'
     '\t\tBTNCENTER\tBTN4 The enter button.\n'
     '\t\tBTNUP\tBTN5 The up button.\n'
     '\t\tBTNDOWN\tBTN6 The down button.\n'
     '<b>Example:</b>\n'
     '\twhile(!ButtonIsDown(BTNCENTER)){ //do something }'), 'Button'],
    ['ButtonIsUp', 'ButtonIsUp(button)', ('<b>ButtonIsUp('
     '<span foreground="brown">button</span>)</b>\n\n'
     'Check if button is not pressed or not.\n'
     'Returns 1: true, 0: false\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">button</span>\tBTNEXIT\tBTN1 The exit (escape) button.\n'
     '\t\tBTNRIGHT\tBTN2 The right button.\n'
     '\t\tBTNLEFT\tBTN3 The left button.\n'
     '\t\tBTNCENTER\tBTN4 The enter button.\n'
     '\t\tBTNUP\tBTN5 The up button.\n'
     '\t\tBTNDOWN\tBTN6 The down button.\n'
     '<b>Example:</b>\n'
     '\twhile(ButtonIsUp(BTNCENTER)){ //do something }'), 'Button'],
    ['ButtonWaitForAnyPress', 'ButtonWaitForAnyPress(time)',
     ('<b>ButtonWaitForAnyPress(<span foreground="brown">time</span>)</b>\n\n'
     'Waiting for any button press for given time.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">time</span>\tTime in milliseconds\n'
     '<b>Example:</b>\n'
     '  ButtonWaitForAnyPress(10000);  // waits max 10 seconds'), 'Button'],
    ['ButtonWaitForPress', 'ButtonWaitForPress(button)',
     ('<b>ButtonWaitForPress(<span foreground="brown">button</span>)</b>\n\n'
     'Wait till a specific button is pressed.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">button</span>\tBTNEXIT\tBTN1 The exit (escape) button.\n'
     '\t\tBTNRIGHT\tBTN2 The right button.\n'
     '\t\tBTNLEFT\tBTN3 The left button.\n'
     '\t\tBTNCENTER\tBTN4 The enter button.\n'
     '\t\tBTNUP\tBTN5 The up button.\n'
     '\t\tBTNDOWN\tBTN6 The down button.'), 'Button'],
    ['ButtonWaitForPressAndRelease', 'ButtonWaitForPressAndRelease(button)',
     ('<b>ButtonWaitForPressAndRelease(<span foreground="brown">button</span>)</b>\n\n'
     'Wait till a specific button is pressed and released.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">button</span>\tBTNEXIT\tBTN1 The exit (escape) button.\n'
     '\t\tBTNRIGHT\tBTN2 The right button.\n'
     '\t\tBTNLEFT\tBTN3 The left button.\n'
     '\t\tBTNCENTER\tBTN4 The enter button.\n'
     '\t\tBTNUP\tBTN5 The up button.\n'
     '\t\tBTNDOWN\tBTN6 The down button.'), 'Button'],
    ['CircleOut', 'CircleOut(x, y, radius)', ('<b>CircleOut('
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">radius</span>)</b>\n\n'
     'This function lets you draw a circle on the screen '
     'with its center at the specified x and y location, '
     'using the specified radius.'), 'Display'],
    ['CircleOutEx', 'CircleOutEx(x, y, radius, options)', ('<b>CircleOutEx('
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">radius</span>, '
     '<span foreground="brown">options</span>)</b>\n\n'
     'This function lets you draw a circle on the screen '
     'with its center at the specified x and y location, '
     'using the specified radius.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">options</span>\tDRAW_OPT_NORMAL\n'
     '\t\tDRAW_OPT_FILL_SHAPE'), 'Display'],
    ['CurrentTick', 'CurrentTick()', ('<b>CurrentTick()</b>\n\n'
     'Read the current system tick.\n\n'
     '<b>Example:</b>\n'
     '  long tick;\n'
     '  tick = CurrentTick();'), 'General'],
    ['EllipseOut', 'EllipseOut(x, y, radiusX, radiusY)', ('<b>EllipseOut('
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">radiusX</span>, '
     '<span foreground="brown">radiusY</span>)</b>\n\n'
     'This function lets you draw an ellipse on the screen '
     'with its center at the specified x and y location, '
     'using the specified radii.'), 'Display'],
    ['EllipseOutEx', 'EllipseOutEx(x, y, radiusX, radiusY, options)', ('<b>EllipseOutEx('
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">radiusX</span>, '
     '<span foreground="brown">radiusY</span>, '
     '<span foreground="brown">options</span>)</b>\n\n'
     'This function lets you draw an ellipse on the screen '
     'with its center at the specified x and y location, '
     'using the specified radii.\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">options</span>\tDRAW_OPT_NORMAL\n'
     '\t\tDRAW_OPT_FILL_SHAPE'), 'Display'],
    ['LcdText', 'LcdText(color, x, y, str)', ('<b>LcdText('
     '<span foreground="brown">color</span>, '
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">str</span>)</b>\n\n'
     'Draw a text value on the screen at the specified x and y location.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">color</span>\t1: black text, 0: white text on black background\n'
     '\t<span foreground="brown">x</span>\tThe x value for the start of the number output.\n'
     '\t<span foreground="brown">y</span>\tThe text line number for the number output.\n'
     '\t<span foreground="brown">str</span>\tThe text to output to the LCD screen.\n'
     '<b>Example:</b>\n'
     '\tLcdText(1, 0, <span foreground="green">LCD_LINE1</span>, "Hello World!");'), 'Display'],
    ['TextOut', 'TextOut(x, y, str)', ('<b>TextOut ('
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">str</span>)</b>\n\n'
     'Draw a text value on the screen at the specified x and y location.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">x</span>\tThe x value for the start of the text output.\n'
     '\t<span foreground="brown">y</span>\tThe y value for the text output.\n'
     '\t<span foreground="brown">str</span>\tThe text to output to the LCD screen.\n'
     '<b>Example:</b>\n'
     '\tTextOut(0, <span foreground="green">LCD_LINE1</span>, "Hello World!");'), 'Display'],
    ['LcdTextf', 'LcdTextf(color, x, y, str, fmt)', ('<b>LcdTextf('
     '<span foreground="brown">color</span>, '
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">fmt</span>,...)</b>\n\n'
     'Print text with variables, works like printf()\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">color</span>\t1: black text, 0: white text with black background\n'
     '\t<span foreground="brown">x</span>\tThe x value for the start of the string output.\n'
     '\t<span foreground="brown">y</span>\tThe y value for the string output.\n'
     '\t<span foreground="brown">fmt</span>\tThe string to output to the LCD screen.\n'
     '<b>Example:</b>\n'
     '\tint x = 1234567890;\n'
     '\tLcdTextf(1, 10, LCD_LINE7, "Variable: %d", x);'), 'Display'],
    ['LcdBmpFile', 'LcdBmpFile(color, x, y, name)', ('<b>LcdBmpFile('
     '<span foreground="brown">color</span>, '
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">name</span>)</b>\n\n'), 'Display'],
    ['NumOut', 'NumOut(x, y, value)', ('<b>NumOut('
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>,  <span foreground="brown">value</span>)</b>\n\n'
     'Draw a numeric value on the screen at the '
     'specified x and y location.\n'
     'The y value must be a multiple of 8.\n\n<b>Parameters</b>\n'
     '\t<span foreground="brown">x</span>\tThe x value for the start of the number output.\n'
     '\t<span foreground="brown">y</span>\tThe text line number for the number output.\n'
     '\t<span foreground="brown">value</span>\tThe value to output to the LCD screen. Any numeric\n'
     '\t\ttype is supported.\n'
     '<b>Example:</b>\n  NumOut(0, <span foreground="green">LCD_LINE1</span>, x);'), 'Display'],
    ['LcdClean', 'LcdClean()', '<b>LcdClean()</b>\n\n' +
     'Erase Display', 'Display'],
    ['LcdSelectFont', 'LcdSelectFont(FontType)', ('<b>LcdSelectFont('
     '<span foreground="brown">FontType</span>)</b>\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">FontType</span>\t0 normal\n'
     '\t\t1 small, bold\n'
     '\t\t2 large\n'
     '\t\t3 tiny'), 'Display'],
    ['LcdClearDisplay', 'LcdClearDisplay()', '<b>LcdClearDisplay()</b>\n\n', 'Display'],
    ['LcdIcon', 'LcdIcon(color, x, y, IconType, IconNum)',
     ('<b>LcdIcon(color, x, y, IconType, IconNum)</b>\n\n'
     'Draw a icon on the screen at the specified location\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">IconType</span>\tICONTYPE_NORMAL 0   IconNum 0..34\n'
     '\t\tICONTYPE_SMALL  1           0..21\n'
     '\t\tICONTYPE_LARGE  2           0..27\n'
     '\t\tICONTYPE_MENU   3           0..10\n'
     '\t\tICONTYPE_ARROW  4           0..2'), 'Display'],
    ['LcdUpdate', 'LcdUpdate()', '<b>LcdUpdate()</b>\n\n', 'Display'],
    #['LcdInit', 'LcdInit()', 'LcdInit()\n', 'General'],
    #['LcdExit', 'LcdExit()', 'LcdExit()\n', 'General'],
    ['LineOut', 'LineOut(x1, y1, x2, y2)', ('<b>LineOut('
     '<span foreground="brown">x1</span>, '
     '<span foreground="brown">y1</span>, '
     '<span foreground="brown">x2</span>, '
     '<span foreground="brown">y2</span>)</b>\n\n'
     'This function lets you draw a line on the screen '
     'from x1, y1 to x2, y2.'), 'Display'],
    ['MotorBusy', 'MotorBusy(outputs)', ('<b>MotorBusy('
     '<span foreground="brown">outputs</span>)</b>\n\n'
     'This function enables the program to test if a output port is busy. '
     'Returns 1 if output is busy, 0 if not.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '<b>Example:</b>\n'
     '\twhile(MotorBusy(OUT_B)){\n'
     '\t  Wait(2);  // 2ms between checks\n'
     '\t}'), 'Output'],
    ['MotorRotationCount', 'MotorRotationCount(output)', ('<b>MotorRotationCount('
     '<span foreground="brown">output</span>)</b>\n\n'
     'This function enables the program to read the tacho count in degrees as\n'
     'sensor input. This count is set to 0 at boot time, not at program start.\n'
     'See also: ResetRotationCount()'), 'Output'],
    ['MotorTachoCount', 'MotorTachoCount(output)', ('<b>MotorTachoCount('
     '<span foreground="brown">output</span>)</b>\n\n'
     'This function enables reading current output tacho count in degrees.\n'
     'This count is set to 0 at program start.\n'
     'See also: ResetTachoCount()'), 'Output'],
    #['OutputInit', 'OutputInit()', 'OutputInit()\n', 'General'],
    #['OutputExit', 'OutputExit()', 'OutputExit()\n', 'General'],
    ['OnFwd', 'OnFwd(outputs, power)', ('<b>OnFwd('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">power</span>)</b>\n\n'
     'Run motors forward with given power.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">power</span>\tOutput power, 0 to 127.\n'
     '\t\tCan be negative to reverse direction.\n'
     '<b>Example:</b>\n'
     '\tOnFwd(OUT_BC, 127);'), 'Output'],
    ['OnFor', 'OnFor(outputs, time, power)', ('<b>OnFor('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">time</span>, <span foreground="brown">power</span>)</b>\n\n'
     'Run motors for given time with given power.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">time</span>\tDesired time in milliseconds.\n'
     '\t<span foreground="brown">power</span>\tOutput power, 0 to 127.\n'
     '\t\tCan be negative to reverse direction.\n'
     '<b>Example:</b>\n'
     '\tOnFor(OUT_BC, 1000, 50);'), 'Output'],
    ['OnFwdEx', 'OnFwdEx(outputs, power, reset)', ('<b>OnFwdEx('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">power</span>, '
     '<span foreground="brown">reset</span>)</b>\n\n'
     'Run motors forward and reset counters.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">power</span>\tOutput power, 0 to 127.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">reset</span>\tconstants to specify which of the three\n'
     '\t\ttachometer counters should be reset.\n\n'
     '<b>Example:</b>\n'
     '\tOnFwdEx(OUT_BC, 75, RESET_ALL);'), 'Output'],
    ['OnFwdReg', 'OnFwdReg(outputs, speed)', ('<b>OnFwdReg('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>)</b>\n\n'
     'Forwards with given speed'), 'Output'],
    ['OnFwdSync', 'OnFwdSync(outputs, speed)', ('<b>OnFwdSync('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>)</b>\n\n'
     'Run two motors synchronized forwards with given speed.'), 'Output'],
    ['OnFwdSyncEx', 'OnFwdSyncEx(outputs, speed, turn, reset)', ('<b>OnFwdSyncEx('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>,'
     '<span foreground="brown">turn</span>, '
     '<span foreground="brown">reset</span>)</b>\n\n'
     'Run two motors synchronized forwards with given speed and given turn ratio.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tHas to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n'
     '\t\tOUT_BD or OUT_CD. Anything else is invalid.\n'
     '\t<span foreground="brown">speed</span>\tAngle limit, in degree.\n'
     '\t<span foreground="brown">turn</span>\tTurn ratio in range [-200 - 200]\n'
     '\t\t0  : Motors will run with same power\n'
     '\t\t100: One motor will run with specified power while the other\n'
     '\t\twill be close to zero\n'
     '\t\t200: One motor will run with specified power forward while \n'
     '\t\tthe other will run in the opposite direction at the same \n'
     '\t\tpower level.\n'
     '\t<span foreground="brown">reset</span>\tRESET_NONE\tNo counters will be reset\n'
     '\t\tRESET_COUNT\tReset the internal tachometer\n'
     '\t\tRESET_BLOCK_COUNT\tReset the block tachometer\n'
     '\t\tRESET_ROTATION_COUNT\tReset the rotation counter\n'
     '\t\tRESET_BLOCKANDTACHO\tReset both the internal counter\n'
     '\t\t\tand the block counter\n'
     '\t\tRESET_ALL\tReset all tachometer counters\n'
     '<b>Example:</b>\n'
     '\tOnFwdSyncEx(OUT_BC, 50, 30, RESET_NONE);'), 'Output'],
    ['OnForSync', 'OnForSync(outputs, time, speed)', ('<b>OnForSync('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">time</span>, '
     '<span foreground="brown">speed</span>)</b>\n\n'), 'Output'],
    ['OnForSyncEx', 'OnForSyncEx(outputs, time, speed, turn, stop)', ('<b>OnForSyncEx('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">time</span>, '
     '<span foreground="brown">speed</span>, '
     '<span foreground="brown">turn</span>, '
     '<span foreground="brown">stop</span>)</b>\n\n'), 'Output'],
    ['OnRev', 'OnRev(outputs, power)', ('<b>OnRev('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">power</span>)</b>\n\n'
     'Run motors backwards with given power.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">power</span>\tOutput power, 0 to 127.\n'
     '\t\tCan be negative to reverse direction.\n'
     '<b>Example:</b>\n'
     '\tOnRev(OUT_BC, 127);'), 'Output'],
    ['OnRevEx', 'OnRevEx(outputs, power, reset)', ('<b>OnRevEx('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">power</span>, '
     '<span foreground="brown">reset</span>)</b>\n\n'
     'Run motors backward and reset counters. \n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">power</span>\tOutput power, 0 to 127.\n'
     '\t\tCan be negative to reverse direction.\n'
     '\t<span foreground="brown">reset</span>\tconstants to specify which of the three\n'
     '\t\ttachometer counters should be reset.\n\n'
     '<b>Example:</b>\n'
     '\tOnRevEx(OUT_BC, 75, RESET_ALL);'), 'Output'],
    ['OnRevReg', 'OnRevReg(outputs, speed)', ('<b>OnRevReg('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>)</b>\n\n'
     'Backwards with given speed'), 'Output'],
    ['OnRevSync', 'OnRevSync(outputs, speed)', ('<b>OnRevSync('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>)</b>\n\n'
     'Run two motors synchronized backwards with given speed.\n\n'), 'Output'],
    ['OnRevSyncEx', 'OnRevSyncEx(outputs, speed, turn, reset)', ('<b>OnRevSyncEx('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>, '
     '<span foreground="brown">turn</span>, '
     '<span foreground="brown">reset</span>)</b>\n\n'
     'Run two motors synchronized backwards with given speed and given turn ratio.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tHas to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n'
     '\t\tOUT_BD or OUT_CD. Anything else is invalid.\n'
     '\t<span foreground="brown">speed</span>\tAngle limit, in degree.\n'
     '\t<span foreground="brown">turn</span>\tTurn ratio in range [-200 - 200]\n'
     '\t\t0 both motors with same speed same direction\n'
     '\t\t0 - 99 same direction, higher port with lower speed\n'
     '\t\t100 only lower port rotates,\n'
     '\t\t101 - 200 motors run in opposite direction, higher port\n'
     '\t\twith lower speed.\n'
     '\t\tNegative values regulate lower port\n'
     '\t<span foreground="brown">reset</span>\tRESET_NONE\tNo counters will be reset\n'
     '\t\tRESET_COUNT\tReset the internal tachometer \n'
     '\t\t\tcounter\n'
     '\t\tRESET_BLOCK_COUNT\tReset the block tachometer \n'
     '\t\t\tcounter\n'
     '\t\tRESET_ROTATION_COUNT\tReset the rotation counter\n'
     '\t\tRESET_BLOCKANDTACHO\tReset both the internal counter\n'
     '\t\t\tand the block counter\n'
     '\t\tRESET_ALL\tReset all tachometer counters\n'
     '<b>Example:</b>\n'
     '\tOnRevSyncEx(OUT_BC, 50, 30, RESET_NONE);'), 'Output'],
    ['OutputPower', 'OutputPower(outputs, power)', ('<b>OutputPower('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">power</span>)</b>\n\n'
     'This function enables setting the output percentage power on '
     'the output ports\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">power</span>\tSpecify output speed [-100 – 100 %]\n'), 'Output'],
    ['OutputSpeed', 'OutputSpeed(outputs, speed)', ('<b>OutputSpeed('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>)</b>\n\n'
     'This function enables setting the output percentage speed on the output '
     'ports. This modes automatically enables speed control, which means the '
     'system will automatically adjust the power to keep the specified speed.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports\n'
     '\t<span foreground="brown">speed</span>\tSpecify output speed [-100 – 100 %]\n'), 'Output'],
    ['OutputStart', 'OutputStart(outputs)', ('<b>OutputStart('
     '<span foreground="brown">outputs</span>)</b>\n\n'
     'This function enables starting the specified output ports.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.'), 'Output'],
    ['OutputStop', 'OutputStop(outputs, useBrake)', ('<b>OutputStop('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">useBrake</span>)</b>\n\n'
     'This function enables stopping the specified output port.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports\n'
     '\t<span foreground="brown">useBreak</span>\t0: Float, 1: Break'), 'Output'],
    ['OutputStepPower', 'OutputStepPower(outputs, power, step1, step2, step3)',
     ('<b>OutputStepPower('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">power</span>, '
     '<span foreground="brown">step1</span>, '
     '<span foreground="brown">step2</span>, '
     '<span foreground="brown">step3</span>)</b>\n\n'
     'This function enables specifying a full motor power cycle in tacho counts.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\n'
     '\t<span foreground="brown">power</span>\n'
     '\t<span foreground="brown">step1</span>\tspecifyes the power ramp up periode in tacho counts, \n'
     '\t<span foreground="brown">step2</span>\tspecifyes the constant power period in tacho counts,\n'
     '\t<span foreground="brown">step3</span>\tspecifyes the power down period in tacho counts.'), 'Output'],
    ['OutputStepSpeed', 'OutputStepSpeed(outputs, speed, step1, step2, step3)',
     ('<b>OutputStepSpeed('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>, '
     '<span foreground="brown">step1</span>, '
     '<span foreground="brown">step2</span>, '
     '<span foreground="brown">step3</span>)</b>\n\n'
     'This function enables specifying a full motor power cycle in tacho counts. '
     'The system will automatically adjust the power level to the motor to keep '
     'the specified output speed.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\n'
     '\t<span foreground="brown">speed</span>\n'
     '\t<span foreground="brown">step1</span>\tspecifyes the power ramp up periode in tacho counts,\n'
     '\t<span foreground="brown">step2</span>\tspecifyes the constant power period in tacho counts,\n'
     '\t<span foreground="brown">step3</span>\tspecifyes the power down period in tacho counts.'), 'Output'],
    ['OutputStepSync', 'OutputStepSync(outputs, speed, turn, step)',
     ('<b>OutputStepSync('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>, '
     '<span foreground="brown">turn</span>, '
     '<span foreground="brown">step</span>)</b>\n\n'
     'This function enables synchronizing two motors. Synchronization should be '
     'used when motors should run as synchrone as possible, for example to '
     'archieve a model driving straight. Duration is specified in tacho counts.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tHas to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n'
     '\t\tOUT_BD or OUT_CD. Anything else is invalid.\n'
     '\t<span foreground="brown">speed</span>\n'
     '\t<span foreground="brown">turn</span>\t0  :  Motor will run with same power\n'
     '\t\t100:  One motor will run with specified power while the other \n'
     '\t\twill be close to zero\n'
     '\t\t200:  One motor will run with specified power forward while \n'
     '\t\tthe other will run in the opposite direction at the \n'
     '\t\tsame power level.\n'
     '\t<span foreground="brown">step</span>\tTacho pulses, 0 = Infinite'), 'Output'],
    ['OutputTimePower', 'OutputTimePower(outputs, power, time1, time2, time3)',
     ('<b>OutputTimePower('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">power</span>, '
     '<span foreground="brown">time1</span>, '
     '<span foreground="brown">time2</span>, '
     '<span foreground="brown">time3</span>)</b>\n\n'
     'This function enables specifying a full motor power cycle in time.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">power</span>\n'
     '\t<span foreground="brown">time1</span>\tspecifyes the power ramp up periode in milliseconds,\n'
     '\t<span foreground="brown">time2</span>\tspecifyes the constant power period in milliseconds,\n'
     '\t<span foreground="brown">time3</span>\tspecifyes the power down period in milliseconds.'), 'Output'],
    ['OutputTimeSpeed', 'OutputTimeSpeed(outputs, speed, time1, time2, time3)',
     ('<b>OutputTimeSpeed('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>, '
     '<span foreground="brown">time1</span>, '
     '<span foreground="brown">time2</span>, '
     '<span foreground="brown">time3</span>)</b>\n\n'
     'This function enables specifying a full motor power cycle in time.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n'
     '\t<span foreground="brown">speed</span>\n'
     '\t<span foreground="brown">time1</span>\tspecifyes the power ramp up periode in milliseconds,\n'
     '\t<span foreground="brown">time2</span>\tspecifyes the constant power period in milliseconds,\n'
     '\t<span foreground="brown">time3</span>\tspecifyes the power down period in milliseconds.'), 'Output'],
    ['OutputTimeSync', 'OutputTimeSync(outputs, speed, turn, time)',
     ('<b>OutputTimeSync('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>, '
     '<span foreground="brown">turn</span>, '
     '<span foreground="brown">time</span>)</b>\n\n'
     'This function enables synchronizing two motors. Synchronization should be '
     'used when motors should run as synchrone as possible, for example to '
     'archieve a model driving straight. Duration is specified in time.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tHas to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n'
     '\t\tOUT_BD or OUT_CD. Anything else is invalid.\n'
     '\t<span foreground="brown">speed</span>\n'
     '\t<span foreground="brown">turn</span>\t0  :  Motor will run with same power\n'
     '\t\t100:  One motor will run with specified power while the other \n'
     '\t\twill be close to zero\n'
     '\t\t200:  One motor will run with specified power forward while \n'
     '\t\tthe other will run in the opposite direction at the same \n'
     '\t\tpower level.\n'
     '\t<span foreground="brown">time</span>'), 'Output'],
    ['Off', 'Off(outputs)', ('<b>Off('
     '<span foreground="brown">outputs</span>)</b>\n\n'
     'Turn the specified outputs off (with braking).\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tDesired output ports.\n\n'
     '<b>Example:</b>\n'
     '\tOff(OUT_A); // turn off output A'), 'Output'],
    ['PlayTone', 'PlayTone(frequency, duration)', ('<b>PlayTone('
     '<span foreground="brown">frequency</span>, '
     '<span foreground="brown">duration</span>)</b>\n\n'), 'Sound'],
    ['PlayToneEx', 'PlayToneEx(frequency, duration, volume)', ('<b>PlayToneEx('
     '<span foreground="brown">frequency</span>, '
     '<span foreground="brown">duration</span>, ' 
     '<span foreground="brown">volume</span>)</b>\n\n'), 'Sound'],
    ['PlaySound', 'PlaySound(aCode)', ('<b>PlaySound('
     '<span foreground="brown">aCode</span>)</b>\n\n'
     'Play a sound that mimics the RCX system sounds using one of the RCXSoundConstants.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">aCode</span>\tSOUND_CLICK\tkey click sound\n'
     '\t\tSOUND_DOUBLE_BEEP\tdouble beep\n'
     '\t\tSOUND_UP\tsweep up\n'
     '\t\tSOUND_DOWN\tsweep down\n'
     '\t\tSOUND_LOW_BEEP\terror sound\n'
     '\t\tSOUND_FAST_UP\tfast sweep up\n'
     '<b>Example:</b>\n'
     '  PlaySound(SOUND_CLICK);'), 'Sound'],
    ['PlayTones', 'PlayTones(tones)', ('<b>PlayTones('
     '<span foreground="brown">tones[]</span>)</b>\n\n'
     'Play a series of tones contained in the tones array.  Each element in '
     'the array is an instance of the Tone structure, containing a frequency '
     'and a duration.\n\n'
     '<b>Example:</b>\n'
     '  unsigned short melody[7][2] = {\n'
     '    {TONE_D4, NOTE_QUARTER},       // = 1000ms / 4\n'
     '    {TONE_E4, NOTE_EIGHT},\n'
     '    {TONE_D4, NOTE_EIGHT},\n'
     '    {TONE_F4, NOTE_EIGHT},\n'
     '    {TONE_D4, NOTE_EIGHT},\n'
     '    {TONE_E4, NOTE_EIGHT},\n'
     '    {TONE_D4, 750}\n'
     '  };\n'
     '  PlayTones(melody);'), 'Sound'],
    ['PlayFile', 'PlayFile(name)',
     ('<b>PlayFile(<span foreground="brown">name</span>)</b>\n\n'
     'Play rmd-, wav- or rso-soundfile.\n'
     'Check that the wav-format is PCM, Mono 8 bits.\n\n'
     '<b>Example:</b>\n'
     '  PlayFile("../prjs/sound/Dog bark 2.rsf");'), 'Sound'],
    ['PointOut', 'PointOut(x, y)', ('<b>PointOut('
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>)</b>\n\n'), 'Display'],
    ['Random', 'Random(int)',
     ('<b>Random (<span foreground="brown">n = 0</span>)</b>\n\n'
     'Generate random number. The returned value will range '
     'between 0 and n (exclusive).\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">int</span>\tThe maximum unsigned value desired.\n'
     '<b>Example:</b>\n'
     '  int x = Random(100); // unsigned int between 0..99\n'), 'General'],
    ['ReadSensor', 'ReadSensor(input)', ('<b>ReadSensor('
     '<span foreground="brown">input</span>)</b>\n\n'
     'Readout of the actual sensor data.\n\n'
     '<b>Parameters:</b>\n'
     '  <span foreground="brown">input</span>        The port to read from.\n'
     '<b>Example:</b>\n'
     '  int touched;\n'
     '  SetSensorTouch(IN_1);\n'
     '  touched = ReadSensor(IN_1);'), 'Input'],
    ['ReadSensorData', 'ReadSensorData(input)', 'ReadSensorData(input)\n', 'Input'],
    ['RectOut', 'RectOut(x, y, w, h)', ('<b>RectOut('
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">w</span>, '
     '<span foreground="brown">h</span>)</b>\n\n'
     'This function lets you draw a rectangle on the screen at x, y with '
     'the specified width and height.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">x</span>\tThe x value for the lower left corner of the rectangle.\n'
     '\t<span foreground="brown">y</span>\tThe y value for the lower left corner of the rectangle.\n'
     '\t<span foreground="brown">width</span>\tThe width of the rectangle.\n'
     '\t<span foreground="brown">height</span>\tThe height of the rectangle.\n'
     '<b>Example:</b>\n'
     '\tRectOut(5,5,168,118);'), 'Display'],
    ['RectOutEx', 'RectOutEx(x, y, w, h, options)', ('<b>RectOutEx('
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, '
     '<span foreground="brown">w</span>, '
     '<span foreground="brown">h</span>, '
     '<span foreground="brown">options</span>)</b>\n\n'
     'This function lets you draw a rectangle on the screen at x, y with '
     'the specified width and height.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">x</span>\tThe x value for the lower left corner of the rectangle.\n'
     '\t<span foreground="brown">y</span>\tThe y value for the lower left corner of the rectangle.\n'
     '\t<span foreground="brown">width</span>\tThe width of the rectangle.\n'
     '\t<span foreground="brown">height</span>\tThe height of the rectangle.\n'
     '\t<span foreground="brown">options</span>\tDRAW_OPT_NORMAL\n'
     '\t\tDRAW_OPT_FILL_SHAPE\n'
     '<b>Example:</b>\n'
     '\tRectOut(5,5,168,118, DRAW_OPT_FILL_SHAPE);'), 'Display'],
    ['ResetGyro', 'ResetGyro()', ('<b>ResetGyro()</b>\n\n'
     'Reset the angle of the gyrosensor to 0 by changing modes back '
     'and forth. This will take 2 seconds and is NOT SURE to work '
     'as expected.\n\n'
     '<b>Example:</b>\n'
     '\tResetGyro();'), 'Input'],
    ['ResetTachoCount', 'ResetTachoCount(outputs)', ('<b>ResetTachoCount('
     '<span foreground="brown">outputs</span>)</b>\n\n'
     'This function enables resetting the tacho count for the '
     'individual output ports. The tacho count is also resetted '
     'at program start.\n'), 'Output'],
    ['ResetRotationCount', 'ResetRotationCount(outputs)', ('<b>ResetRotationCount('
     '<span foreground="brown">outputs</span>)</b>\n\n'
     'This function enables the program to clear the tacho count '
     'used as sensor input. This rotation count is resetted at '
     'boot time, not at program start.'), 'Output'],
    ['ResetAllTachoCounts', 'ResetAllTachoCounts()', ('<b>ResetAllTachoCounts('
     '<span foreground="brown">outputs</span>)</b>\n\n'
     'Resets tacho and rotation count.'), 'Output'],
    ['RotateMotor', 'RotateMotor(output, speed, angle)', ('<b>RotateMotor('
     '<span foreground="brown">output</span>, '
     '<span foreground="brown">speed</span>, '
     '<span foreground="brown">angle</span>)</b>\n\n'
     'Rotate motor with given speed for a defined angle. '
     'Code stops till the angle is reached\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tHas to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n'
     '\t\tOUT_BD or OUT_CD. Anything else is invalid.\n'
     '\t<span foreground="brown">speed</span>\t\n'
     '\t<span foreground="brown">angle</span>\tAngle limit, in degree\n'
     '<b>Example:</b>\n'
     '\tRotateMotor(OUT_A, 75, 180);'), 'Output'],
    ['RotateMotorEx', 'RotateMotorEx(outputs, speed, angle, turn, sync, stop)',
     ('<b>RotateMotorEx('
     '<span foreground="brown">outputs</span>,'
     '<span foreground="brown">speed</span>, '
     '<span foreground="brown">angle</span>, '
     '<span foreground="brown">turn</span>, '
     '<span foreground="brown">sync</span>, '
     '<span foreground="brown">stop</span>)</b>\n\n'
     'Rotate two motors with given speed and given turn ratio for '
     'a definded angle. Code stops till the angle is reached.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">outputs</span>\tHas to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n'
     '\t\tOUT_BD or OUT_CD. Anything else is invalid.\n'
     '\t<span foreground="brown">speed</span>\n'
     '\t<span foreground="brown">angle</span>\tAngle limit, in degree.\n'
     '\t<span foreground="brown">turn</span>\tTurn ratio in range [-200 - 200]\n'
     '\t\t0 both motors with same speed same direction\n'
     '\t\t0 - 99 same direction, higher port with lower speed\n'
     '\t\t100 only lower port rotates,\n'
     '\t\t101 - 200 motors run in opposite direction, higher port\n'
     '\t\twith lower speed.\n'
     '\t\tNegative values regulate lower port\n'
     '\t<span foreground="brown">sync</span>\tShould be set to true if a non-zero turn percent\n'
     '\t\tis specified or no turning will occur.\n'
     '\t<span foreground="brown">stop</span>\tSpecify whether the motor(s) should brake at the end\n'
     '\t\tof the rotation\n'
     '<b>Example:</b>\n'
     '\tRotateMotorEx(OUT_BC,50,720,200,TRUE,TRUE);   // drive pirouette'), 'Output'],
    ['RotateMotorNoWait', 'RotateMotorNoWait(outputs, speed, angle)',
     ('<b>RotateMotorNoWait('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>, '
     '<span foreground="brown">angle</span>)</b>\n\n'
     'Rotate motor with given speed for a defined angle. '
     'Code does not stop till the angle is reached\n\n'), 'Output'],
    ['SetDirection', 'SetDirection(outputs, direction)', ('<b>SetDirection('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">direction</span>)</b>\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">direction</span>\tOUT_FWD\n'
     '\t\tOUT_REV\n'
     '\t\tOUT_TOGGLE'), 'Output'],
    ['SetPower', 'SetPower(outputs, power)', ('<b>SetPower('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">power</span>)</b>\n\n'
     'Negative values forward, positive values backwards'), 'Output'],
    ['SetSpeed', 'SetSpeed(outputs, speed)', ('<b>SetSpeed('
     '<span foreground="brown">outputs</span>, '
     '<span foreground="brown">speed</span>)</b>\n\n'), 'Output'],
    ['SetSensorTouch', 'SetSensorTouch(input)', ('<b>SetSensorTouch('
     '<span foreground="brown">input</span>)</b>\n\n'
     'Allocate EV3 Touch Sensor to specified input port '
     'in TOUCH_PRESS mode.\n\n'
     '<b>Returns</b>\t0: not pressed, 1: pressed\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">input</span>\tthe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorTouch(IN_1);'), 'Input'],
    ['SetSensorLight', 'SetSensorLight(input)', ('<b>SetSensorLight('
     '<span foreground="brown">input</span>)</b>\n\n'
     'Allocate EV3 Color Sensor to specified input port '
     'in COL_REFLECT mode.\n'
     'Returns the reflected light intensities in % [0...100].\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">input</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorLight(IN_1);'), 'Input'],
    ['SetSensorColor', 'SetSensorColor(input)', ('<b>SetSensorColor('
     '<span foreground="brown">input</span>)</b>\n\n'
     'Allocate EV3 Color Sensor to specified input port '
     'in COL_COLOR mode.\n\n'
     'Return of color\n'
     '\t\t0: transparent\n'
     '\t\t1: black\n'
     '\t\t2: blue\n'
     '\t\t3: green\n'
     '\t\t4: yellow\n'
     '\t\t5: red\n'
     '\t\t6: white\n'
     '\t\t7: brown\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">input</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorColor(IN_1);'), 'Input'],
    ['SetSensorUS', 'SetSensorUS(input)', ('<b>SetSensorUS('
     '<span foreground="brown">input</span>)</b>\n\n'
     'Allocate EV3 Ultrasonic Sensor to specified input port '
     'in US_DIST_CM mode.\n'
     'Returns distance in cm [1...250].\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">input</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorUS(IN_1);'), 'Input'],
    ['SetSensorIR', 'SetSensorIR(input)', ('<b>SetSensorIR('
     '<span foreground="brown">input</span>)</b>\n\n'
     'Allocate EV3 Infrared Sensor to specified input port '
     'in IR_PROX mode.\n'
     'Returns distance in cm [1...250].\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">input</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorIR(IN_1);'), 'Input'],
    ['SetSensorGyro', 'SetSensorGyro(input)', ('<b>SetSensorGyro('
     '<span foreground="brown">input</span>)</b>\n\n'
     'Allocate EV3 Gyro Sensor to specified input port in angle mode. '
     'The value read will return the angle in degrees from -32768 to 32767.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">input</span>\tThe Input port to configure.\n'
     '<b>Example:</b>\n\tSetSensorGyro(IN_1);'), 'Input'],
    ['SetSensorNXTTouch', 'SetSensorNXTTouch(input)', ('<b>SetSensorNXTTouch('
     '<span foreground="brown">input</span>)</b>\n\n'
     'Configure the sensor on the specified port as a NXT-touch sensor.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">input</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorNXTTouch(IN_1);'), 'Input'],
    ['SetSensorNXTLight', 'SetSensorNXTLight(input)', ('<b>SetSensorNXTLight('
     '<span foreground="brown">input</span>)</b>\n\n'
     'Configure the sensor on the specified port as a NXT-light sensor.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">input</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorNXTLight(IN_1);'), 'Input'],
    ['SetSensorNXTSound', 'SetSensorNXTSound(input)', ('<b>SetSensorNXTSound('
     '<span foreground="brown">input</span>)</b>\n\n'
     'Configure the sensor on the specified port as a NXT-sound sensor.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">input</span>\tThe port to configure.\n'
     '<b>Example:</b>\n'
     '\tSetSensorNXTSound(IN_1);'), 'Input'],
     ['SetSensorNXTUS', 'SetSensorNXTUS(input)', ('<b>SetSensorNXTUS('
     '<span foreground="brown">input</span>)</b>\n\n'
     'Configure the sensor on the specified port as a NXT-ultrasonic sensor.\n\n'), 'Input'],
    ['SetSensorMode', 'SetSensorMode(input, mode)', ('<b>SetSensorMode('
     '<span foreground="brown">input</span>, '
     '<span foreground="brown">mode</span>)</b>\n\n'
     'Touch sensor\tTOUCH\tReturn of state\n'
     '\t\t\t(2 states possible)\n'
     'Light sensor\tCOL_REFLECT\tReturn of the reflected light\n'
     '\t\t\tintensities in %\n'
     '\t\tCOL_AMBIENT\tReturn of room light\n'
     '\t\t\tintensities in %\n'
     '\t\tCOL_COLOR\tReturn of color\n'
     '\t\t\t0: transparent\n'
     '\t\t\t1: black\n'
     '\t\t\t2: blue\n'
     '\t\t\t3: green\n'
     '\t\t\t4: yellow\n'
     '\t\t\t5: red\n'
     '\t\t\t6: white\n'
     '\t\t\t7: brown\n'
     'Sonar sensor\tUS_DIST_CM\tReturn of distance in mm,\n'
     '\t\t\t0 to 2550\n'
     'Gyro sensor\tGYRO_ANG\tReturn angle in degrees.\n'
     '\t\t\tClockwise is positive.\n'
     '\t\tGYRO_RATE\tReturn rotational speed\n'
     '\t\t\tin degrees per second\n'
     'Infrared\tIR_PROX\tReturn of distance\n'
     '\t\t\tin % (up to 70cm)\n'
     '\t\tIR_SEEK\tPosition of the Beacon\n'
     '\t\tIR_REMOTE\tControlling EV3 with Beacon'), 'Input'],
    ['SetAllSensorMode', 'SetAllSensorMode()', 'obsolete', 'Input'],
    ['SetIRBeaconCH', 'SetIRBeaconCH(input, channel)', ('<b>SetIRBeaconCH('
     '<span foreground="brown">input</span>, '
     '<span foreground="brown">channel</span>)</b>\n\n'
     'Set Channel of the Beacon for Readout.\n\n'
     '<b>Parameters:</b>\n'
     '\t<span foreground="brown">input</span>\n'
     '\t<span foreground="brown">channel</span>\t0 or BEACON_CH_1 default\n'
     '\t\t1 or BEACON_CH_2\n'
     '\t\t2 or BEACON_CH_3\n'
     '\t\t3 or BEACON_CH_4\n'
     '<b>Example:</b>\n'
     '  SetIRBeaconCH(IN_1, 1);    // channel 2'), 'Input'],
    ['SetLedPattern', 'SetLedPattern(pattern)', ('<b>SetLedPattern('
     '<span foreground="brown">pattern</span>)</b>\n\n'), 'Button'],
    ['SetLedWarning', 'SetLedWarning(value)', ('<b>SetLedWarning('
     '<span foreground="brown">value</span>)</b>\n\n'), 'Button'],
    ['LedPattern', 'LedPattern()', 'LedPattern()', 'Button'],
    ['LedWarning', 'LedWarning()', 'LedWarning()', 'Button'],
    ['Wait', 'Wait(time)', ('<b>Wait(<span foreground="brown">time_ms</span>)</b>\n\n'
     'Make code sleep for specified amount of time.\n\n'
     '<b>Parameters</b>\n'
     '\t<span foreground="brown">time_ms</span>\tThe number of milliseconds to sleep.\n\n'
     '<b>Example:</b>\n'
     '  Wait(1000);'), 'General']
]
EVC_CONSTS = [
    ['BEACON_CH_1', 'BEACON_CH_1'],
    ['BEACON_CH_2', 'BEACON_CH_2'],
    ['BEACON_CH_3', 'BEACON_CH_3'],
    ['BEACON_CH_4', 'BEACON_CH_4'],
    ['BEACON_OFF', 'BEACON_OFF'],
    ['BEACON_UP_LEFT', 'BEACON_UP_LEFT'],
    ['BEACON_DOWN_LEFT', 'BEACON_DOWN_LEFT'],
    ['BEACON_UP_RIGHT', 'BEACON_UP_RIGHT'],
    ['BEACON_DOWN_RIGHT', 'BEACON_DOWN_RIGHT'],
    ['BEACON_UP', 'BEACON_UP'],
    ['BEACON_DIAG_UP_LEFT', 'BEACON_DIAG_UP_LEFT'],
    ['BEACON_DIAG_UP_RIGHT', 'BEACON_DIAG_UP_RIGHT'],
    ['BEACON_DOWN', 'BEACON_DOWN'],
    ['BEACON_ON', 'BEACON_ON'],
    ['BEACON_LEFT', 'BEACON_LEFT'],
    ['BEACON_RIGHT', 'BEACON_RIGHT'],
    ['BTNEXIT', 'BTNEXIT'],
    ['BTNRIGHT', 'BTNRIGHT'],
    ['BTNLEFT', 'BTNLEFT'],
    ['BTNCENTER', 'BTNCENTER'],
    ['BTNUP', 'BTNUP'],
    ['BTNDOWN', 'BTNDOWN'],
    ['DRAW_OPT_NORMAL ','DRAW_OPT_NORMAL'],
    ['DRAW_OPT_FILL_SHAPE', 'DRAW_OPT_FILL_SHAPE'],
    ['LCD_WIDTH', 'LCD_WIDTH'],
    ['LCD_HEIGHT', 'LCD_HEIGHT'],
    ['ICONTYPE_NORMAL', 'ICONTYPE_NORMAL'],
    ['ICONTYPE_SMALL', 'ICONTYPE_SMALL'],
    ['ICONTYPE_LARGE', 'ICONTYPE_LARGE'],
    ['ICONTYPE_MENU', 'ICONTYPE_MENU'],
    ['ICONTYPE_ARROW', 'ICONTYPE_ARROW'],
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
    ['LED_BLACK', 'LED_BLACK'],
    ['LED_GREEN', 'LED_GREEN'],
    ['LED_RED', 'LED_RED'],
    ['LED_ORANGE', 'LED_ORANGE'],
    ['LED_GREEN_FLASH', 'LED_GREEN_FLASH'],
    ['LED_RED_FLASH', 'LED_RED_FLASH'],
    ['LED_ORANGE_FLASH', 'LED_ORANGE_FLASH'],
    ['LED_GREEN_PULSE', 'LED_GREEN_PULSE'],
    ['LED_RED_PULSE', 'LED_RED_PULSE'],
    ['LED_ORANGE_PULSE', 'LED_ORANGE_PULSE'],
    ['NUM_LED_PATTERNS', 'NUM_LED_PATTERNS'],
    ['OUT_A', 'OUT_A'],
    ['OUT_B', 'OUT_B'],
    ['OUT_C', 'OUT_C'],
    ['OUT_D', 'OUT_D'],
    ['OUT_AB', 'OUT_AB'],
    ['OUT_AC', 'OUT_AC'],
    ['OUT_AD', 'OUT_AD'],
    ['OUT_BC', 'OUT_BC'],
    ['OUT_BD', 'OUT_BD'],
    ['OUT_CD', 'OUT_CD'],
    ['OUT_ABC', 'OUT_ABC'],
    ['OUT_ABD', 'OUT_ABD'],
    ['OUT_ACD', 'OUT_ACD'],
    ['OUT_BCD', 'OUT_BCD'],
    ['OUT_ALL', 'OUT_ALL'],
    ['OUT_ON', 'OUT_ON'],
    ['OUT_OFF', 'OUT_OFF'],
    ['OUT_FWD', 'OUT_FWD'],
    ['OUT_REV', 'OUT_REV'],
    ['RESET_NONE', 'RESET_NONE'],
    ['RESET_COUNT', 'RESET_COUNT'],
    ['RESET_BLOCK_COUNT', 'RESET_BLOCK_COUNT'],
    ['RESET_ROTATION_COUNT', 'RESET_ROTATION_COUNT'],
    ['RESET_BLOCKANDTACHO', 'RESET_BLOCKANDTACHO'],
    ['RESET_ALL', 'RESET_ALL'],
    ['SENSOR_1', 'SENSOR_1'],
    ['SENSOR_2', 'SENSOR_2'],
    ['SENSOR_3', 'SENSOR_3'],
    ['SENSOR_4', 'SENSOR_4'],
    ['TOUCH', 'TOUCH'],
    ['COL_REFLECT', 'COL_REFLECT'],
    ['COL_AMBIENT', 'COL_AMBIENT'],
    ['COL_COLOR', 'COL_COLOR'],
    ['US_DIST_CM', 'US_DIST_CM'],
    ['US_DIST_IN', 'US_DIST_IN'],
    ['US_LISTEN', 'US_LISTEN'],
    ['GYRO_ANG', 'GYRO_ANG'],
    ['GYRO_RATE', 'GYRO_RATE'],
    ['IR_PROX', 'IR_PROX'],
    ['IR_REMOTE', 'IR_REMOTE'],
    ['IR_SEEK', 'IR_SEEK'],
    ['NXT_TEMP_C', 'NXT_TEMP_C'],
    ['NXT_TEMP_F', 'NXT_TEMP_F'],
    ['NXT_SND_DB', 'NXT_SND_DB'],
    ['NXT_SND_DBA', 'NXT_SND_DBA'],
    ['NXT_TOUCH', 'NXT_TOUCH'],
    ['NXT_REFLECT', 'NXT_REFLECT'],
    ['NXT_AMBIENT', 'NXT_AMBIENT'],
    ['NXT_COL_REF', 'NXT_COL_REF'],
    ['NXT_COL_AMB', 'NXT_COL_AMB'],
    ['NXT_COL_COL', 'NXT_COL_COL'],
    ['NXT_US_CM', 'NXT_US_CM'],
    ['NXT_US_IN', 'NXT_US_IN'],
    ['HT_DIR_DC', 'HT_DIR_DC'],
    ['HT_DIR_AC', 'HT_DIR_AC'],
    ['HT_DIR_DALL', 'HT_DIR_DALL'],
    ['HT_DIR_AALL', 'HT_DIR_DALL'],
    ['SEC_1', 'SEC_1'],
    ['SEC_2', 'SEC_2'],
    ['SEC_3', 'SEC_3'],
    ['SEC_4', 'SEC_4'],
    ['SEC_5', 'SEC_5'],
    ['SEC_6', 'SEC_6'],
    ['SEC_7', 'SEC_7'],
    ['SEC_8', 'SEC_8'],
    ['SEC_9', 'SEC_9'],
    ['SEC_10', 'SEC_10'],
    ['SEC_15', 'SEC_15'],
    ['SEC_20', 'SEC_20'],
    ['SEC_30', 'SEC_30'],
    ['MIN_1', 'MIN_1'],
    ['SOUND_CLICK', 'SOUND_CLICK'],
    ['SOUND_DOUBLE_BEEP', 'SOUND_DOUBLE_BEEP'],
    ['SOUND_UP', 'SOUND_UP'],
    ['SOUND_DOWN', 'SOUND_DOWN'],
    ['SOUND_LOW_BEEP', 'SOUND_LOW_BEEP'],
    ['SOUND_FAST_UP', 'SOUND_FAST_UP'],
    ['FONTTYPE_NORMAL', 'FONTTYPE_NORMAL'],
    ['FONTTYPE_SMALL', 'FONTTYPE_SMALL'],
    ['FONTTYPE_LARGE', 'FONTTYPE_LARGE'],
    ['FONTTYPE_TINY', 'FONTTYPE_TINY'],
    ['S_ICON_CHARGING', 'S_ICON_CHARGING'],
    ['S_ICON_BATT_4', 'S_ICON_BATT_4'],
    ['S_ICON_BATT_3', 'S_ICON_BATT_3'],
    ['S_ICON_BATT_2', 'S_ICON_BATT_2'],
    ['S_ICON_BATT_1', 'S_ICON_BATT_1'],
    ['S_ICON_BATT_0', 'S_ICON_BATT_0'],
    ['S_ICON_WAIT1', 'S_ICON_WAIT1'],
    ['S_ICON_WAIT2', 'S_ICON_WAIT2'],
    ['S_ICON_BT_ON', 'S_ICON_BT_ON'],
    ['S_ICON_BT_VISIBLE', 'S_ICON_BT_VISIBLE'],
    ['S_ICON_BT_CONNECTED', 'S_ICON_BT_CONNECTED'],
    ['S_ICON_BT_CONNVISIB', 'S_ICON_BT_CONNVISIB'],
    ['S_ICON_WIFI_3', 'S_ICON_WIFI_3'],
    ['S_ICON_WIFI_2', 'S_ICON_WIFI_2'],
    ['S_ICON_WIFI_1', 'S_ICON_WIFI_1'],
    ['S_ICON_WIFI_CONNECTED', 'S_ICON_WIFI_CONNECTED'],
    ['S_ICON_USB', 'S_ICON_USB'],
    ['NUM_S_ICONS', 'NUM_S_ICONS'],
    ['N_ICON_NONE', 'N_ICON_NONE'],
    ['N_ICON_RUN', 'N_ICON_RUN'],
    ['N_ICON_FOLDER', 'N_ICON_FOLDER'],
    ['N_ICON_FOLDER2', 'N_ICON_FOLDER2'],
    ['N_ICON_USB', 'N_ICON_USB'],
    ['N_ICON_SD', 'N_ICON_SD'],
    ['N_ICON_SOUND', 'N_ICON_SOUND'],
    ['N_ICON_IMAGE', 'N_ICON_IMAGE'],
    ['N_ICON_SETTINGS', 'N_ICON_SETTINGS'],
    ['N_ICON_ONOFF', 'N_ICON_ONOFF'],
    ['N_ICON_SEARCH', 'N_ICON_SEARCH'],
    ['N_ICON_WIFI', 'N_ICON_WIFI'],
    ['N_ICON_CONNECTIONS', 'N_ICON_CONNECTIONS'],
    ['N_ICON_ADD_HIDDEN', 'N_ICON_ADD_HIDDEN'],
    ['N_ICON_TRASHBIN', 'N_ICON_TRASHBIN'],
    ['N_ICON_VISIBILITY', 'N_ICON_VISIBILITY'],
    ['N_ICON_KEY', 'N_ICON_KEY'],
    ['N_ICON_CONNECT', 'N_ICON_CONNECT'],
    ['N_ICON_DISCONNECT', 'N_ICON_DISCONNECT'],
    ['N_ICON_UP', 'N_ICON_UP'],
    ['N_ICON_DOWN', 'N_ICON_DOWN'],
    ['N_ICON_WAIT1', 'N_ICON_WAIT1'],
    ['N_ICON_WAIT2', 'N_ICON_WAIT2'],
    ['N_ICON_BLUETOOTH', 'N_ICON_BLUETOOTH'],
    ['N_ICON_INFO', 'N_ICON_INFO'],
    ['N_ICON_TEXT', 'N_ICON_TEXT'],
    ['N_ICON_QUESTIONMARK', 'N_ICON_QUESTIONMARK'],
    ['N_ICON_INFO_FILE', 'N_ICON_INFO_FILE'],
    ['N_ICON_DISC', 'N_ICON_DISC'],
    ['N_ICON_CONNECTED', 'N_ICON_CONNECTED'],
    ['N_ICON_OBP', 'N_ICON_OBP'],
    ['N_ICON_OBD', 'N_ICON_OBD'],
    ['N_ICON_OPENFOLDER', 'N_ICON_OPENFOLDER'],
    ['N_ICON_BRICK1', 'N_ICON_BRICK1'],
    ['NUM_N_ICONS', 'NUM_N_ICONS'],
    ['L_ICON_YES_NOTSEL', 'L_ICON_YES_NOTSEL'],
    ['L_ICON_YES_SEL', 'L_ICON_YES_SEL'],
    ['L_ICON_NO_NOTSEL', 'L_ICON_NO_NOTSEL'],
    ['L_ICON_NO_SEL', 'L_ICON_NO_SEL'],
    ['L_ICON_OFF', 'L_ICON_OFF'],
    ['L_ICON_WAIT_VERT', 'L_ICON_WAIT_VERT'],
    ['L_ICON_WAIT_HORZ', 'L_ICON_WAIT_HORZ'],
    ['L_ICON_TO_MANUAL', 'L_ICON_TO_MANUAL'],
    ['L_ICON_WARNSIGN', 'L_ICON_WARNSIGN'],
    ['L_ICON_WARN_BATT', 'L_ICON_WARN_BATT'],
    ['L_ICON_WARN_POWER', 'L_ICON_WARN_POWER'],
    ['L_ICON_WARN_TEMP', 'L_ICON_WARN_TEMP'],
    ['L_ICON_NO_USBSTICK', 'L_ICON_NO_USBSTICK'],
    ['L_ICON_TO_EXECUTE', 'L_ICON_TO_EXECUTE'],
    ['L_ICON_TO_BRICK', 'L_ICON_TO_BRICK'],
    ['L_ICON_TO_SDCARD', 'L_ICON_TO_SDCARD'],
    ['L_ICON_TO_USBSTICK', 'L_ICON_TO_USBSTICK'],
    ['L_ICON_TO_BLUETOOTH', 'L_ICON_TO_BLUETOOTH'],
    ['L_ICON_TO_WIFI', 'L_ICON_TO_WIFI'],
    ['L_ICON_TO_TRASH', 'L_ICON_TO_TRASH'],
    ['L_ICON_TO_COPY', 'L_ICON_TO_COPY'],
    ['L_ICON_TO_FILE', 'L_ICON_TO_FILE'],
    ['L_ICON_CHAR_ERROR', 'L_ICON_CHAR_ERROR'],
    ['L_ICON_COPY_ERROR', 'L_ICON_COPY_ERROR'],
    ['L_ICON_PROGRAM_ERROR', 'L_ICON_PROGRAM_ERROR'],
    ['L_ICON_WARN_MEMORY', 'L_ICON_WARN_MEMORY'],
    ['NUM_L_ICONS', 'NUM_L_ICONS'],
    ['M_ICON_STAR', 'M_ICON_STAR'],
    ['M_ICON_LOCKSTAR', 'M_ICON_LOCKSTAR'],
    ['M_ICON_LOCK', 'M_ICON_LOCK'],
    ['M_ICON_PC', 'M_ICON_PC'],
    ['M_ICON_PHONE', 'M_ICON_PHONE'],
    ['M_ICON_BRICK', 'M_ICON_BRICK'],
    ['M_ICON_UNKNOWN', 'M_ICON_UNKNOWN'],
    ['M_ICON_FROM_FOLDER', 'M_ICON_FROM_FOLDER'],
    ['M_ICON_CHECKBOX', 'M_ICON_CHECKBOX'],
    ['M_ICON_CHECKED', 'M_ICON_CHECKED'],
    ['M_ICON_XED', 'M_ICON_XED'],
    ['NUM_M_ICONS', 'NUM_M_ICONS'],
    ['A_ICON_LEFT', 'A_ICON_LEFT'],
    ['A_ICON_RIGHT', 'A_ICON_RIGHT'],
    ['A_ICON_STAR', 'A_ICON_STAR'],
    ['NUM_A_ICONS', 'NUM_A_ICONS']
]
