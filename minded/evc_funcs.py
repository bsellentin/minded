# -*- coding: utf-8 -*-

''' EVC-Functions and -Constants for Completion and Api-viewer'''

EVC_FUNCS = [
    ['InitEV3', 'InitEV3()', '<b>InitEV3()</b>\n\n' +
     'Initialization of all EV3-Functions.\n' +
     'Should be the first command in main.\n\n' +
     '<b>Example:</b>\n' +
     '  #include "ev3.h"\n' +
     '  int main(){\n' +
     '      InitEV3();\n' +
     '      // do something\n' +
     '      FreeEV3();\n' +
     '      return 0;\n' +
     '  }', 'General'],
    #['CloseEV3', 'CloseEV3()', 'CloseEV3()\n', 'General'],
    #['ExitEV3', 'ExitEV3()', 'ExitEV3()\n', 'General'],
    ['FreeEV3', 'FreeEV3()', '<b>FreeEV3()</b>\n\n' +
     'Close and exit of all EV3-Functions', 'General'],
    ['ButtonIsDown', 'ButtonIsDown(button)', '<b>ButtonIsDown(' +
     '<span foreground="brown">button</span>)</b>\n\n' +
     'Check if button is pressed or not.\n' +
     'Returns 1: true, 0: false\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">button</span>   BTNEXIT   BTN1 The exit (escape) button.\n' +
     '           BTNRIGHT  BTN2 The right button.\n' +
     '           BTNLEFT   BTN3 The left button.\n' +
     '           BTNCENTER BTN4 The enter button.\n' +
     '           BTNUP     BTN5 The up button.\n' +
     '           BTNDOWN   BTN6 The down button.\n' +
     '<b>Example:</b>\n' +
     '  while(!ButtonIsDown(BTNCENTER)){ //do something }', 'Button'],
    ['ButtonIsUp', 'ButtonIsUp(button)', '<b>ButtonIsUp(' +
     '<span foreground="brown">button</span>)</b>\n\n' +
     'Check if button is not pressed or not.\n' +
     'Returns 1: true, 0: false\n\n'+
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">button</span>   BTNEXIT   BTN1 The exit (escape) button.\n' +
     '           BTNRIGHT  BTN2 The right button.\n' +
     '           BTNLEFT   BTN3 The left button.\n' +
     '           BTNCENTER BTN4 The enter button.\n' +
     '           BTNUP     BTN5 The up button.\n' +
     '           BTNDOWN   BTN6 The down button.\n' +
     '<b>Example:</b>\n' +
     '  while(ButtonIsUp(BTNCENTER)){ //do something }', 'Button'],
    ['ButtonWaitForAnyPress', 'ButtonWaitForAnyPress(time)',
     '<b>ButtonWaitForAnyPress(<span foreground="brown">time</span>)</b>\n\n' +
     'Waiting for any button press for given time.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">time</span>  Time in milliseconds\n' +
     '<b>Example:</b>\n' +
     '  ButtonWaitForAnyPress(10000);  // waits max 10 seconds', 'Button'],
    ['ButtonWaitForPress', 'ButtonWaitForPress(button)',
     '<b>ButtonWaitForPress(<span foreground="brown">button</span>)</b>\n\n' +
     'Wait till a specific button is pressed.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">button</span>   BTNEXIT   BTN1 The exit (escape) button.\n' +
     '           BTNRIGHT  BTN2 The right button.\n' +
     '           BTNLEFT   BTN3 The left button.\n' +
     '           BTNCENTER BTN4 The enter button.\n' +
     '           BTNUP     BTN5 The up button.\n' +
     '           BTNDOWN   BTN6 The down button.', 'Button'],
    ['ButtonWaitForPressAndRelease', 'ButtonWaitForPressAndRelease(button)',
     '<b>ButtonWaitForPressAndRelease(<span foreground="brown">button</span>)</b>\n\n' +
     'Wait till a specific button is pressed and released.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">button</span>   BTNEXIT   BTN1 The exit (escape) button.\n' +
     '           BTNRIGHT  BTN2 The right button.\n' +
     '           BTNLEFT   BTN3 The left button.\n' +
     '           BTNCENTER BTN4 The enter button.\n' +
     '           BTNUP     BTN5 The up button.\n' +
     '           BTNDOWN   BTN6 The down button.', 'Button'],
    ['CircleOut', 'CircleOut(x, y, radius)', '<b>CircleOut(' +
     '<span foreground="brown">x</span>, ' +
     '<span foreground="brown">y</span>, ' +
     '<span foreground="brown">radius</span>)</b>\n\n' +
     'This function lets you draw a circle on the screen\n' +
     'with its center at the specified x and y location,\n' +
     'using the specified radius.', 'Display'],
    ['CurrentTick', 'CurrentTick()', '<b>CurrentTick()</b>\n\n' +
     'Read the current system tick.\n\n' +
     '<b>Example:</b>\n' +
     '  long tick;\n' +
     '  tick = CurrentTick();', 'General'],
    ['EllipseOut', 'EllipseOut(x, y, radiusX, radiusY)', '<b>EllipseOut(' +
     '<span foreground="brown">x</span>, ' +
     '<span foreground="brown">y</span>, ' +
     '<span foreground="brown">radiusX</span>, ' +
     '<span foreground="brown">radiusY</span>)</b>\n\n' +
     'This function lets you draw an ellipse on the screen\n' +
     'with its center at the specified x and y location,\n' +
     'using the specified radii.', 'Display'],
    ['LcdText', 'LcdText(color, x, y, str)', '<b>LcdText(' +
     '<span foreground="brown">color</span>, ' +
     '<span foreground="brown">x</span>, ' +
     '<span foreground="brown">y</span>, ' +
     '<span foreground="brown">str</span>)</b>\n\n' +
     'Draw a text value on the screen at the specified x and y location.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">color</span>  1: black text, 0: white text on black background\n' +
     '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
     '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
     '  <span foreground="brown">str</span>    The text to output to the LCD screen.\n' +
     '<b>Example:</b>\n' +
     '  LcdText(1, 0, <span foreground="green">LCD_LINE1</span>, "Hello World!");', 'Display'],
    ['TextOut', 'TextOut(x, y, str)', '<b>TextOut (' +
     '<span foreground="brown">x</span>, ' +
     '<span foreground="brown">y</span>, ' +
     '<span foreground="brown">str</span>)</b>\n\n' +
     'Draw a text value on the screen at the specified x and y location.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">x</span>      The x value for the start of the text output.\n' +
     '  <span foreground="brown">y</span>      The y value for the text output.\n' +
     '  <span foreground="brown">str</span>    The text to output to the LCD screen.\n' +
     '<b>Example:</b>\n' +
     '  TextOut(0, <span foreground="green">LCD_LINE1</span>, "Hello World!");', 'Display'],
    ['LcdTextf', 'LcdTextf(color, x, y, str, fmt)', '<b>LcdTextf(' +
     '<span foreground="brown">color</span>, ' +
     '<span foreground="brown">x</span>, ' +
     '<span foreground="brown">y</span>, ' +
     '<span foreground="brown">fmt</span>,...)</b>\n\n' +
     'Print text with variables, works like printf()\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">color</span>   1: black text, 0: white text with black background\n' +
     '  <span foreground="brown">x</span>       The x value for the start of the string output.\n' +
     '  <span foreground="brown">y</span>       The y value for the string output.\n' +
     '  <span foreground="brown">fmt</span>     The string to output to the LCD screen.\n' +
     '<b>Example:</b>\n' +
     '  int x = 1234567890;\n' +
     '  LcdTextf(1, 10, LCD_LINE7, "Variable: %d", x);', 'Display'],
    ['LcdBmpFile', 'LcdBmpFile(color, x, y, name)', '<b>LcdBmpFile(' +
     '<span foreground="brown">color</span>, ' +
     '<span foreground="brown">x</span>, ' +
     '<span foreground="brown">y</span>, ' +
     '<span foreground="brown">name</span>)</b>\n\n', 'Display'],
    ['NumOut', 'NumOut(x, y, value)', '<b>NumOut(' +
     '<span foreground="brown">x</span>, ' +
     '<span foreground="brown">y</span>,  <span foreground="brown">value</span>)</b>\n\n' +
     'Draw a numeric value on the screen at the ' +
     'specified x and y location.\n' +
     'The y value must be a multiple of 8.\n\n<b>Parameters</b>\n' +
     '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
     '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
     '  <span foreground="brown">value</span>  The value to output to the LCD screen. Any numeric\n' +
     '         type is supported.\n' +
     '<b>Example:</b>\n  NumOut(0, <span foreground="green">LCD_LINE1</span>, x);', 'Display'],
    ['LcdClean', 'LcdClean()', '<b>LcdClean()</b>\n\n' +
     'Erase Display', 'Display'],
    ['LcdSelectFont', 'LcdSelectFont(FontType)', '<b>LcdSelectFont(' +
     '<span foreground="brown">FontType</span>)</b>\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">FontType</span>  0 normal\n' +
     '            1 small, bold\n' +
     '            2 large\n' +
     '            3 tiny', 'Display'],
    ['LcdClearDisplay', 'LcdClearDisplay()', '<b>LcdClearDisplay()</b>\n\n', 'Display'],
    ['LcdIcon', 'LcdIcon(color, x, y, IconType, IconNum)',
     '<b>LcdIcon(color, x, y, IconType, IconNum)</b>\n\n' +
     'Draw a icon on the screen at the specified location\n\n' +
     '<b>Parameters:</b>\n' +
     'IconType   ICONTYPE_NORMAL 0   IconNum 0..34\n' +
     '           ICONTYPE_SMALL  1           0..21\n' +
     '           ICONTYPE_LARGE  2           0..27\n' +
     '           ICONTYPE_MENU   3           0..10\n' +
     '           ICONTYPE_ARROW  4           0..2', 'Display'],
    ['LcdUpdate', 'LcdUpdate()', '<b>LcdUpdate()</b>\n\n', 'Display'],
    #['LcdInit', 'LcdInit()', 'LcdInit()\n', 'General'],
    #['LcdExit', 'LcdExit()', 'LcdExit()\n', 'General'],
    ['LineOut', 'LineOut(x1, y1, x2, y2)', '<b>LineOut(' +
     '<span foreground="brown">x1</span>, ' +
     '<span foreground="brown">y1</span>, ' +
     '<span foreground="brown">x2</span>, ' +
     '<span foreground="brown">y2</span>)</b>\n\n' +
     'This function lets you draw a line on the screen\n' +
     'from x1, y1 to x2, y2.', 'Display'],
    ['MotorBusy', 'MotorBusy(outputs)', '<b>MotorBusy(' +
     '<span foreground="brown">outputs</span>)</b>\n\n' +
     'This function enables the program to test if a output port is busy.\n' +
     'Returns 1 if output is busy, 0 if not.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>   Desired output ports.\n' +
     '<b>Example:</b>\n' +
     ' while(MotorBusy(OUT_B)){\n' +
     '     Wait(2);  // 2ms between checks\n' +
     ' }', 'Output'],
    ['MotorRotationCount', 'MotorRotationCount(output)', '<b>MotorRotationCount(' +
     '<span foreground="brown">output</span>)</b>\n\n' +
     'This function enables the program to read the tacho count in degrees as\n' +
     'sensor input. This count is set to 0 at boot time, not at program start.\n' +
     'See also: ResetRotationCount()', 'Output'],
    ['MotorTachoCount', 'MotorTachoCount(output)', '<b>MotorTachoCount(' +
     '<span foreground="brown">output</span>)</b>\n\n' +
     'This function enables reading current output tacho count in degrees.\n' +
     'This count is set to 0 at program start.\n' +
     'See also: ResetTachoCount()', 'Output'],
    #['OutputInit', 'OutputInit()', 'OutputInit()\n', 'General'],
    #['OutputExit', 'OutputExit()', 'OutputExit()\n', 'General'],
    ['OnFwd', 'OnFwd(outputs, power)', '<b>OnFwd(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">power</span>)</b>\n\n' +
     'Run motors forward with given power.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>   Desired output ports.\n' +
     '  <span foreground="brown">power</span>     Output power, 0 to 127.\n' +
     '            Can be negative to reverse direction.\n' +
     '<b>Example:</b>\n' +
     ' OnFwd(OUT_BC, 127);', 'Output'],
    ['OnFor', 'OnFor(outputs, time, power)', '<b>OnFor(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">time</span>, <span foreground="brown">power</span>)</b>\n\n' +
     'Run motors for given time with given power.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>   Desired output ports.\n' +
     '  <span foreground="brown">time</span>      Desired time in milliseconds.\n' +
     '  <span foreground="brown">power</span>     Output power, 0 to 127.\n' +
     '            Can be negative to reverse direction.\n' +
     '<b>Example:</b>\n' +
     '  OnFor(OUT_BC, 1000, 50);', 'Output'],
    ['OnFwdEx', 'OnFwdEx(outputs, power, reset)', '<b>OnFwdEx(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">power</span>, ' +
     '<span foreground="brown">reset</span>)</b>\n\n' +
     'Run motors forward and reset counters.\n\n'
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
     '  <span foreground="brown">power</span>    Output power, 0 to 127.\n' +
     '           Can be negative to reverse direction.\n' +
     '  <span foreground="brown">reset</span>    constants to specify which of the three\n' +
     '           tachometer counters should be reset.\n\n' +
     '<b>Example:</b>\n' +
     '  OnFwdEx(OUT_BC, 75, RESET_ALL);', 'Output'],
    ['OnFwdReg', 'OnFwdReg(outputs, speed)', '<b>OnFwdReg(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>)</b>\n\n' +
     'Forwards with given speed', 'Output'],
    ['OnFwdSync', 'OnFwdSync(outputs, speed)', '<b>OnFwdSync(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>)</b>\n\n' +
     'Run two motors synchronized forwards with given speed.', 'Output'],
    ['OnFwdSyncEx', 'OnFwdSyncEx(outputs, speed, turn, reset)', '<b>OnFwdSyncEx(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>,' +
     '<span foreground="brown">turn</span>, ' +
     '<span foreground="brown">reset</span>)</b>\n\n' +
     'Run two motors synchronized forwards with given speed and given turn ratio.\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Has to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n' +
     '           OUT_BD or OUT_CD. Anything else is invalid.\n' +
     '  <span foreground="brown">speed</span>    Angle limit, in degree.\n' +
     '  <span foreground="brown">turn</span>     Turn ratio in range [-200 - 200]\n' +
     '           0  : Motors will run with same power\n'
     '           100: One motor will run with specified power while the other\n' +
     '                will be close to zero\n' +
     '           200: One motor will run with specified power forward while the other\n' +
     '                will run in the opposite direction at the same power level.\n' +
     '  <span foreground="brown">reset</span>    RESET_NONE           No counters will be reset\n' +
     '           RESET_COUNT          Reset the internal tachometer counter\n' +
     '           RESET_BLOCK_COUNT    Reset the block tachometer counter\n' +
     '           RESET_ROTATION_COUNT Reset the rotation counter\n' +
     '           RESET_BLOCKANDTACHO  Reset both the internal counter and\n' +
     '                                the block counter\n' +
     '           RESET_ALL            Reset all tachometer counters\n' +
     '<b>Example:</b>\n' +
     ' OnFwdSyncEx(OUT_BC, 50, 30, RESET_NONE);', 'Output'],
    ['OnForSync', 'OnForSync(outputs, time, speed)', '<b>OnForSync(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">time</span>, ' +
     '<span foreground="brown">speed</span>)</b>\n\n', 'Output'],
    ['OnForSyncEx', 'OnForSyncEx(outputs, time, speed, turn, stop)', '<b>OnForSyncEx(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">time</span>, ' +
     '<span foreground="brown">speed</span>, ' +
     '<span foreground="brown">turn</span>, ' +
     '<span foreground="brown">stop</span>)</b>\n\n', 'Output'],
    ['OnRev', 'OnRev(outputs, power)', '<b>OnRev(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">power</span>)</b>\n\n' +
     'Run motors backwards with given power.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>   Desired output ports.\n' +
     '  <span foreground="brown">power</span>     Output power, 0 to 127.\n' +
     '            Can be negative to reverse direction.\n' +
     '<b>Example:</b>\n' +
     '  OnRev(OUT_BC, 127);', 'Output'],
    ['OnRevEx', 'OnRevEx(outputs, power, reset)', '<b>OnRevEx(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">power</span>, ' +
     '<span foreground="brown">reset</span>)</b>\n\n' +
     'Run motors backward and reset counters. \n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
     '  <span foreground="brown">power</span>    Output power, 0 to 127.\n' +
     '           Can be negative to reverse direction.\n' +
     '  <span foreground="brown">reset</span>    constants to specify which of the three\n' +
     '           tachometer counters should be reset.\n\n' +
     '<b>Example:</b>\n' +
     '  OnRevEx(OUT_BC, 75, RESET_ALL);', 'Output'],
    ['OnRevReg', 'OnRevReg(outputs, speed)', '<b>OnRevReg(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>)</b>\n\n' +
     'Backwards with given speed', 'Output'],
    ['OnRevSync', 'OnRevSync(outputs, speed)', '<b>OnRevSync(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>)</b>\n\n' +
     'Run two motors synchronized backwards with given speed.\n\n', 'Output'],
    ['OnRevSyncEx', 'OnRevSyncEx(outputs, speed, turn, reset)', '<b>OnRevSyncEx(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>, ' +
     '<span foreground="brown">turn</span>, ' +
     '<span foreground="brown">reset</span>)</b>\n\n' +
     'Run two motors synchronized backwards with given speed and given turn ratio.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Has to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n' +
     '           OUT_BD or OUT_CD. Anything else is invalid.\n' +
     '  <span foreground="brown">speed</span>    Angle limit, in degree.\n' +
     '  <span foreground="brown">turn</span>     Turn ratio in range [-200 - 200]\n' +
     '           0 both motors with same speed same direction\n'
     '           0 - 99 same direction, higher port with lower speed\n' +
     '           100 only lower port rotates,\n' +
     '           101 - 200 motors run in opposite direction, higher port\n' +
     '           with lower speed.\n' +
     '           Negative values regulate lower port\n' +
     '  <span foreground="brown">reset</span>    RESET_NONE           No counters will be reset\n' +
     '           RESET_COUNT          Reset the internal tachometer counter\n' +
     '           RESET_BLOCK_COUNT    Reset the block tachometer counter\n' +
     '           RESET_ROTATION_COUNT Reset the rotation counter\n' +
     '           RESET_BLOCKANDTACHO  Reset both the internal counter and\n' +
     '                                the block counter\n' +
     '           RESET_ALL            Reset all tachometer counters\n' +
     '<b>Example:</b>\n' +
     '  OnRevSyncEx(OUT_BC, 50, 30, RESET_NONE);', 'Output'],
    ['OutputPower', 'OutputPower(outputs, power)', '<b>OutputPower(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">power</span>)</b>\n\n' +
     'This function enables setting the output percentage power on\n' +
     'the output ports\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
     '  <span foreground="brown">power</span>    Specify output speed [-100 – 100 %]\n', 'Output'],
    ['OutputSpeed', 'OutputSpeed(outputs, speed)', '<b>OutputSpeed(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>)</b>\n\n' +
     'This function enables setting the output percentage speed on the output\n' +
     'ports. This modes automatically enables speed control, which means the\n' +
     'system will automatically adjust the power to keep the specified speed.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Desired output ports\n' +
     '  <span foreground="brown">speed</span>    Specify output speed [-100 – 100 %]\n', 'Output'],
    ['OutputStart', 'OutputStart(outputs)', '<b>OutputStart(' +
     '<span foreground="brown">outputs</span>)</b>\n\n' +
     'This function enables starting the specified output ports.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Desired output ports.', 'Output'],
    ['OutputStop', 'OutputStop(outputs, useBrake)', '<b>OutputStop(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">useBrake</span>)</b>\n\n' +
     'This function enables stopping the specified output port.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>    Desired output ports\n' +
     '  <span foreground="brown">useBreak</span>   0: Float, 1: Break', 'Output'],
    ['OutputStepPower', 'OutputStepPower(outputs, power, step1, step2, step3)',
     '<b>OutputStepPower(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">power</span>, ' +
     '<span foreground="brown">step1</span>, ' +
     '<span foreground="brown">step2</span>, ' +
     '<span foreground="brown">step3</span>)</b>\n\n' +
     'This function enables specifying a full motor power cycle in tacho counts.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>\n' +
     '  <span foreground="brown">power</span>\n' +
     '  <span foreground="brown">step1</span>  specifyes the power ramp up periode in tacho counts, \n' +
     '  <span foreground="brown">step2</span>  specifyes the constant power period in tacho counts,\n' +
     '  <span foreground="brown">step3</span>  specifyes the power down period in tacho counts.', 'Output'],
    ['OutputStepSpeed', 'OutputStepSpeed(outputs, speed, step1, step2, step3)',
     '<b>OutputStepSpeed(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>, ' +
     '<span foreground="brown">step1</span>, ' +
     '<span foreground="brown">step2</span>, ' +
     '<span foreground="brown">step3</span>)</b>\n\n' +
     'This function enables specifying a full motor power cycle in tacho counts.\n' +
     'The system will automatically adjust the power level to the motor to keep\n' +
     'the specified output speed.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>\n' +
     '  <span foreground="brown">speed</span>\n' +
     '  <span foreground="brown">step1</span>    specifyes the power ramp up periode in tacho counts,\n' +
     '  <span foreground="brown">step2</span>    specifyes the constant power period in tacho counts,\n' +
     '  <span foreground="brown">step3</span>    specifyes the power down period in tacho counts.', 'Output'],
    ['OutputStepSync', 'OutputStepSync(outputs, speed, turn, step)',
     '<b>OutputStepSync(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>, ' +
     '<span foreground="brown">turn</span>, ' +
     '<span foreground="brown">step</span>)</b>\n\n' +
     'This function enables synchronizing two motors. Synchronization should be\n' +
     'used when motors should run as synchrone as possible, for example to\n' +
     'archieve a model driving straight. Duration is specified in tacho counts.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Has to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n' +
     '           OUT_BD or OUT_CD. Anything else is invalid.\n' +
     '  <span foreground="brown">speed</span>\n' +
     '  <span foreground="brown">turn</span>:    0  :  Motor will run with same power\n' +
     '           100:  One motor will run with specified power while the other will\n' +
     '                 be close to zero\n' +
     '           200:  One motor will run with specified power forward while the other\n' +
     '                 will run in the opposite direction at the same power level.\n' +
     '  <span foreground="brown">step</span>:    Tacho pulses, 0 = Infinite', 'Output'],
    ['OutputTimePower', 'OutputTimePower(outputs, power, time1, time2, time3)',
     '<b>OutputTimePower(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">power</span>, ' +
     '<span foreground="brown">time1</span>, ' +
     '<span foreground="brown">time2</span>, ' +
     '<span foreground="brown">time3</span>)</b>\n\n' +
     'This function enables specifying a full motor power cycle in time.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
     '  <span foreground="brown">power</span>\n' +
     '  <span foreground="brown">time1</span>    specifyes the power ramp up periode in milliseconds,\n' +
     '  <span foreground="brown">time2</span>    specifyes the constant power period in milliseconds,\n' +
     '  <span foreground="brown">time3</span>    specifyes the power down period in milliseconds.', 'Output'],
    ['OutputTimeSpeed', 'OutputTimeSpeed(outputs, speed, time1, time2, time3)',
     '<b>OutputTimeSpeed(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>, ' +
     '<span foreground="brown">time1</span>, ' +
     '<span foreground="brown">time2</span>, ' +
     '<span foreground="brown">time3</span>)</b>\n\n' +
     'This function enables specifying a full motor power cycle in time.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
     '  <span foreground="brown">speed</span>\n' +
     '  <span foreground="brown">time1</span>    specifyes the power ramp up periode in milliseconds,\n' +
     '  <span foreground="brown">time2</span>    specifyes the constant power period in milliseconds,\n' +
     '  <span foreground="brown">time3</span>    specifyes the power down period in milliseconds.', 'Output'],
    ['OutputTimeSync', 'OutputTimeSync(outputs, speed, turn, time)',
     '<b>OutputTimeSync('+
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>, ' +
     '<span foreground="brown">turn</span>, ' +
     '<span foreground="brown">time</span>)</b>\n\n' +
     'This function enables synchronizing two motors. Synchronization should be\n' +
     'used when motors should run as synchrone as possible, for example to\n' +
     'archieve a model driving straight. Duration is specified in time.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Has to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n' +
     '           OUT_BD or OUT_CD. Anything else is invalid.\n' +
     '  <span foreground="brown">speed</span>\n' +
     '  <span foreground="brown">turn</span>     0  :  Motor will run with same power\n' +
     '           100:  One motor will run with specified power while the other will\n' +
     '                 be close to zero\n' +
     '           200:  One motor will run with specified power forward while the other\n' +
     '                 will run in the opposite direction at the same power level.\n' +
     '  <span foreground="brown">time</span>', 'Output'],
    ['Off', 'Off(outputs)', '<b>Off(' +
     '<span foreground="brown">outputs</span>)</b>\n\n' +
     'Turn the specified outputs off (with braking).\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Desired output ports.\n\n' +
     '<b>Example:</b>\n' +
     ' Off(OUT_A); // turn off output A', 'Output'],
    ['PlayTone', 'PlayTone(frequency, duration)', '<b>PlayTone(' +
     '<span foreground="brown">frequency</span>, ' +
     '<span foreground="brown">duration</span>)</b>\n\n', 'Sound'],
    ['PlayToneEx', 'PlayToneEx(frequency, duration, volume)', '<b>PlayToneEx(' +
     '<span foreground="brown">frequency</span>, ' +
     '<span foreground="brown">duration</span>, ' +
     '<span foreground="brown">volume</span>)</b>\n\n', 'Sound'],
    ['PlaySound', 'PlaySound(aCode)', '<b>PlaySound(' +
     '<span foreground="brown">aCode</span>)</b>\n\n' +
     'Play a sound that mimics the RCX system sounds using one of the RCXSoundConstants.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">aCode</span>   SOUND_CLICK        key click sound\n' +
     '          SOUND_DOUBLE_BEEP  double beep\n' +
     '          SOUND_UP           sweep up\n' +
     '          SOUND_DOWN         sweep down\n' +
     '          SOUND_LOW_BEEP     error sound\n' +
     '          SOUND_FAST_UP      fast sweep up\n' +
     '<b>Example:</b>\n' +
     '  PlaySound(SOUND_CLICK);', 'Sound'],
    ['PlayTones', 'PlayTones(tones)', '<b>PlayTones(' +
     '<span foreground="brown">tones[]</span>)</b>\n\n' +
     'Play a series of tones contained in the tones array.  Each element in\n' +
     'the array is an instance of the Tone structure, containing a frequency\n' +
     'and a duration.\n\n' +
     '<b>Example:</b>\n' +
     '  unsigned short melody[7][2] = {\n' +
     '    {TONE_D4, NOTE_QUARTER},       // = 1000ms / 4\n' +
     '    {TONE_E4, NOTE_EIGHT},\n' +
     '    {TONE_D4, NOTE_EIGHT},\n' +
     '    {TONE_F4, NOTE_EIGHT},\n' +
     '    {TONE_D4, NOTE_EIGHT},\n' +
     '    {TONE_E4, NOTE_EIGHT},\n' +
     '    {TONE_D4, 750}\n' +
     '  };\n' +
     '  PlayTones(melody);', 'Sound'],
    ['PlayFile', 'PlayFile(name)',
     '<b>PlayFile(<span foreground="brown">name</span>)</b>\n\n', 'Sound'],
    ['PointOut', 'PointOut(x, y)', '<b>PointOut(' +
     '<span foreground="brown">x</span>, ' +
     '<span foreground="brown">y</span>)</b>\n\n', 'Display'],
    ['Random', 'Random(int)',
     '<b>Random (<span foreground="brown">n = 0</span>)</b>\n\n' +
     'Generate random number. The returned value will range\n' +
     'between 0 and n (exclusive).\n\n' +
     '<b>Parameters</b>\n  <span foreground="brown">int</span> The maximum unsigned value desired.\n' +
     '<b>Example:</b>\n' +
     '  int x = Random(100); // unsigned int between 0..99\n', 'General'],
    ['ReadSensor', 'ReadSensor(input)', '<b>ReadSensor(' +
     '<span foreground="brown">input</span>)</b>\n\n' +
     'Readout of the actual sensor data.\n\n' +
     '<b>Parameters:</b>\n' +
     '  <span foreground="brown">input</span>        The port to read from.\n' +
     '<b>Example:</b>\n' +
     '  int touched;\n' +
     '  SetSensorTouch(IN_1);\n'
     '  touched = ReadSensor(IN_1);', 'Input'],
    ['ReadSensorData', 'ReadSensorData(input)', 'ReadSensorData(input)\n', 'Input'],
    ['RectOut', 'RectOut(x, y, w, h)', '<b>RectOut(' +
     '<span foreground="brown">x</span>, '
     '<span foreground="brown">y</span>, ' +
     '<span foreground="brown">w</span>, ' +
     '<span foreground="brown">h</span>)</b>\n\n' +
     'This function lets you draw a rectangle on the screen at x, y with\n' +
     'the specified width and height.\n\n' +
     '<b>Parameters:</b>\n' +
     '  <span foreground="brown">x</span>       The x value for the lower left corner of the rectangle.\n' +
     '  <span foreground="brown">y</span>       The y value for the lower left corner of the rectangle.\n' +
     '  <span foreground="brown">width</span>   The width of the rectangle.\n' +
     '  <span foreground="brown">height</span>  The height of the rectangle.\n' +
     '<b>Example:</b>\n' +
     '  RectOut(5,5,168,118);', 'Display'],
    ['ResetGyro', 'ResetGyro()', '<b>ResetGyro()</b>\n\n' +
     'Reset the angle of the gyrosensor to 0 by changing modes back\n' +
     'and forth. This will take 2 seconds and is NOT SURE to work\n' +
     'as expected.\n\n' +
     '<b>Example:</b>\n' +
     '  ResetGyro();', 'Input'],
    ['ResetTachoCount', 'ResetTachoCount(outputs)', '<b>ResetTachoCount(' +
     '<span foreground="brown">outputs</span>)</b>\n\n' +
     'This function enables resetting the tacho count for the\n' +
     'individual output ports. The tacho count is also resetted\n' +
     'at program start.\n', 'Output'],
    ['ResetRotationCount', 'ResetRotationCount(outputs)', '<b>ResetRotationCount(' +
     '<span foreground="brown">outputs</span>)</b>\n\n' +
     'This function enables the program to clear the tacho count\n' +
     'used as sensor input. This rotation count is resetted at\n' +
     'boot time, not at program start.', 'Output'],
    ['ResetAllTachoCounts', 'ResetAllTachoCounts()', '<b>ResetAllTachoCounts(' +
     '<span foreground="brown">outputs</span>)</b>\n\n' +
     'Resets tacho and rotation count.', 'Output'],
    ['RotateMotor', 'RotateMotor(output, speed, angle)', '<b>RotateMotor(' +
     '<span foreground="brown">output</span>, ' +
     '<span foreground="brown">speed</span>, ' +
     '<span foreground="brown">angle</span>)</b>\n\n' +
     'Rotate motor with given speed for a defined angle.\n' +
     'Code stops till the angle is reached\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Has to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n' +
     '           OUT_BD or OUT_CD. Anything else is invalid.\n' +
     '  <span foreground="brown">speed</span>    \n' +
     '  <span foreground="brown">angle</span>    Angle limit, in degree\n' +
     '<b>Example:</b>\n' +
     '  RotateMotor(OUT_A, 75, 180);', 'Output'],
    ['RotateMotorEx', 'RotateMotorEx(outputs, speed, angle, turn, sync, stop)',
     '<b>RotateMotorEx(' +
     '<span foreground="brown">outputs</span>,' +
     '<span foreground="brown">speed</span>, ' +
     '<span foreground="brown">angle</span>, ' +
     '<span foreground="brown">turn</span>, ' +
     '<span foreground="brown">sync</span>, ' +
     '<span foreground="brown">stop</span>)</b>\n\n' +
     'Rotate two motors with given speed and given turn ratio for\n' +
     'a definded angle. Code stops till the angle is reached.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">outputs</span>  Has to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n' +
     '           OUT_BD or OUT_CD. Anything else is invalid.\n' +
     '  <span foreground="brown">speed</span>\n' +
     '  <span foreground="brown">angle</span>    Angle limit, in degree.\n' +
     '  <span foreground="brown">turn</span>     Turn ratio in range [-200 - 200]\n' +
     '           0 both motors with same speed same direction\n'
     '           0 - 99 same direction, higher port with lower speed\n' +
     '           100 only lower port rotates,\n' +
     '           101 - 200 motors run in opposite direction, higher port\n' +
     '           with lower speed.\n' +
     '           Negative values regulate lower port\n' +
     '  <span foreground="brown">sync</span>     Should be set to true if a non-zero turn percent\n' +
     '           is specified or no turning will occur.\n' +
     '  <span foreground="brown">stop</span>     Specify whether the motor(s) should brake at the end\n' +
     '           of the rotation\n' +
     '<b>Example:</b>\n' +
     '  RotateMotorEx(OUT_BC,50,720,200,TRUE,TRUE);   // drive pirouette', 'Output'],
    ['RotateMotorNoWait', 'RotateMotorNoWait(outputs, speed, angle)',
     '<b>RotateMotorNoWait(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>, ' +
     '<span foreground="brown">angle</span>)</b>\n\n' +
     'Rotate motor with given speed for a defined angle.\n' +
     'Code does not stop till the angle is reached\n\n', 'Output'],
    ['SetDirection', 'SetDirection(outputs, direction)', '<b>SetDirection(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">direction</span>)</b>\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">direction</span>        OUT_FWD\n' +
     '                   OUT_REV\n' +
     '                   OUT_TOGGLE', 'Output'],
    ['SetPower', 'SetPower(outputs, power)', '<b>SetPower(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">power</span>)</b>\n\n' +
     'Negative values forward, positive values backwards', 'Output'],
    ['SetSpeed', 'SetSpeed(outputs, speed)', '<b>SetSpeed(' +
     '<span foreground="brown">outputs</span>, ' +
     '<span foreground="brown">speed</span>)</b>\n\n', 'Output'],
    ['SetSensorTouch', 'SetSensorTouch(input)', '<b>SetSensorTouch(' +
     '<span foreground="brown">input</span>)</b>\n\n' +
     'Allocate EV3 Touch Sensor to specified input port\n' +
     'in TOUCH_PRESS mode.\n\n' +
     '<b>Returns</b>        0: not pressed, 1: pressed\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">input</span>        The port to configure.\n' +
     '<b>Example:</b>\n' +
     '  SetSensorTouch(IN_1);', 'Input'],
    ['SetSensorLight', 'SetSensorLight(input)', '<b>SetSensorLight(' +
     '<span foreground="brown">input</span>)</b>\n\n' +
     'Allocate EV3 Color Sensor to specified input port\n' +
     'in COL_REFLECT mode.\n' +
     'Returns the reflected light intensities in % [0...100].\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">input</span>        The port to configure.\n' +
     '<b>Example:</b>\n' +
     '  SetSensorLight(IN_1);', 'Input'],
    ['SetSensorColor', 'SetSensorColor(input)', '<b>SetSensorColor(' +
     '<span foreground="brown">input</span>)</b>\n\n' +
     'Allocate EV3 Color Sensor to specified input port\n' +
     'in COL_COLOR mode.\n\n' +
     'Return of color 0: transparent\n' +
     '                1: black\n' +
     '                2: blue\n' +
     '                3: green\n' +
     '                4: yellow\n' +
     '                5: red\n' +
     '                6: white\n' +
     '                7: brown\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">input</span>        The port to configure.\n' +
     '<b>Example:</b>\n' +
     '  SetSensorColor(IN_1);', 'Input'],
    ['SetSensorUS', 'SetSensorUS(input)', '<b>SetSensorUS(' +
     '<span foreground="brown">input</span>)</b>\n\n' +
     'Allocate EV3 Ultrasonic Sensor to specified input port\n' +
     'in US_DIST_CM mode.\n' +
     'Returns distance in cm [1...250].\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">input</span>        The port to configure.\n' +
     '<b>Example:</b>\n' +
     '  SetSensorUS(IN_1);', 'Input'],
    ['SetSensorIR', 'SetSensorIR(input)', '<b>SetSensorIR(' +
     '<span foreground="brown">input</span>)</b>\n\n' +
     'Allocate EV3 Infrared Sensor to specified input port\n' +
     'in IR_PROX mode.\n' +
     'Returns distance in cm [1...250].\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">input</span>        The port to configure.\n' +
     '<b>Example:</b>\n' +
     '  SetSensorIR(IN_1);', 'Input'],
    ['SetSensorGyro', 'SetSensorGyro(input)', '<b>SetSensorGyro(' +
     '<span foreground="brown">input</span>)</b>\n\n' +
     'Allocate EV3 Gyro Sensor to specified input port in angle mode\n' +
     'The value read will return the angle in degrees from -32768 to 32767.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">input</span>  The Input port to configure.\n' +
     '<b>Example:</b>\n  SetSensorGyro(IN_1);', 'Input'],
    ['SetSensorNXTTouch', 'SetSensorNXTTouch(input)', '<b>SetSensorNXTTouch(' +
     '<span foreground="brown">input</span>)</b>\n\n' +
     'Configure the sensor on the specified port as a NXT-touch sensor.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">input</span>        The port to configure.\n' +
     '<b>Example:</b>\n' +
     '  SetSensorNXTTouch(IN_1);', 'Input'],
    ['SetSensorNXTLight', 'SetSensorNXTLight(input)', '<b>SetSensorNXTLight(' +
     '<span foreground="brown">input</span>)</b>\n\n' +
     'Configure the sensor on the specified port as a NXT-light sensor.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">input</span>        The port to configure.\n' +
     '<b>Example:</b>\n' +
     '  SetSensorNXTLight(IN_1);', 'Input'],
    ['SetSensorNXTSound', 'SetSensorNXTSound(input)', '<b>SetSensorNXTSound(' +
     '<span foreground="brown">input</span>)</b>\n\n' +
     'Configure the sensor on the specified port as a NXT-sound sensor.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">input</span>        The port to configure.\n' +
     '<b>Example:</b>\n' +
     '  SetSensorNXTSound(IN_1);', 'Input'],
    ['SetSensorMode', 'SetSensorMode(input, mode)', '<b>SetSensorMode(' +
     '<span foreground="brown">input</span>, ' +
     '<span foreground="brown">mode</span>)</b>\n\n' +
     'Touch sensor TOUCH       Return of state (2 states possible)\n' +
     'Light sensor COL_REFLECT Return of the reflected light intensities in %\n' +
     '             COL_AMBIENT Return of room light intensities in %\n' +
     '             COL_COLOR   Return of color 0: transparent\n' +
     '                                         1: black\n' +
     '                                         2: blue\n' +
     '                                         3: green\n' +
     '                                         4: yellow\n' +
     '                                         5: red\n' +
     '                                         6: white\n' +
     '                                         7: brown\n' +
     'Sonar sensor US_DIST_CM Return of distance in mm, 0 to 2550\n' +
     'Gyro sensor  GYRO_ANG   Return angle in degrees. Clockwise is positive.\n' +
     '             GYRO_RATE  Return rotational speed in degrees per second\n' +
     'Infrared     IR_PROX    Return of distance in % (up to 70cm)\n' +
     '             IR_SEEK    Position of the Beacon\n' +
     '             IR_REMOTE  Controlling EV3 with Beacon', 'Input'],
    ['SetAllSensorMode', 'SetAllSensorMode()', 'obsolete', 'Input'],
    ['SetIRBeaconCH', 'SetIRBeaconCH(input, channel)', '<b>SetIRBeaconCH(' +
     '<span foreground="brown">input</span>, ' +
     '<span foreground="brown">channel</span>)</b>\n\n' +
     'Set Channel of the Beacon for Readout.\n\n' +
     '<b>Parameters:</b>\n' +
     '  <span foreground="brown">input</span>\n' +
     '  <span foreground="brown">channel</span>   0 or BEACON_CH_1 default\n' +
     '            1    BEACON_CH_2\n' +
     '            2    BEACON_CH_3\n' +
     '            3    BEACON_CH_4\n' +
     '<b>Example:</b>\n' +
     '  SetIRBeaconCH(IN_1,1)    // channel 2', 'Input'],
    ['SetLedPattern', 'SetLedPattern(pattern)', '<b>SetLedPattern(' +
     '<span foreground="brown">pattern</span>)</b>\n\n', 'Button'],
    ['SetLedWarning', 'SetLedWarning(value)', '<b>SetLedWarning(' +
     '<span foreground="brown">value</span>)</b>\n\n', 'Button'],
    ['Wait', 'Wait(time)', '<b>Wait(<span foreground="brown">time_ms</span>)</b>\n\n' +
     'Make code sleep for specified amount of time.\n\n' +
     '<b>Parameters</b>\n' +
     '  <span foreground="brown">time_ms</span>   The number of milliseconds to sleep.\n\n' +
     '<b>Example:</b>\n' +
     '  Wait(1000);', 'General']
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
    ['HT_DIR_DC', 'HT_DIR_DC'],
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
