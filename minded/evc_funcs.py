# -*- coding: utf-8 -*-
evc_funcs = [
    ['InitEV3', 'InitEV3()', '<b>InitEV3()</b>\n\n' +
        'Initialization of all EV3-Functions.\n' +
        'Should be the first command in main.', 'General'],
    ['CloseEV3', 'CloseEV3()', '', 'General'],
    ['ExitEV3', '', 'ExitEV3()', 'General'],
    ['FreeEV3', 'FreeEV3()', '<b>FreeEV3()</b>\n\n' +
        'Close and exit of all EV3-Functions', 'General'],
    ['ButtonIsDown', 'ButtonIsDown()','<b>ButtonIsDown(' +
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
    ['ButtonIsUp', 'ButtonIsUp()', '<b>ButtonIsUp(' +
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
    ['ButtonWaitForAnyPress', 'ButtonWaitForAnyPress()', 
        '<b>ButtonWaitForAnyPress(<span foreground="brown">time</span>)</b>\n\n' +
        'Waiting for button press for given time.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">time</span>  Time in milliseconds\n' +
        '<b>Example:</b>\n' +
        '  ButtonWaitForAnyPress(10000);  // waits max 10 seconds', 'Button'],
    ['ButtonWaitForPress', 'ButtonWaitForPress()',
        '<b>ButtonWaitForPress(<span foreground="brown">button</span>)</b>\n\n' +
        'Wait till a specific button is pressed.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">button</span>   BTNEXIT   BTN1 The exit (escape) button.\n' +
        '           BTNRIGHT  BTN2 The right button.\n' +
        '           BTNLEFT   BTN3 The left button.\n' +
        '           BTNCENTER BTN4 The enter button.\n' +
        '           BTNUP     BTN5 The up button.\n' +
        '           BTNDOWN   BTN6 The down button.', 'Button'],
    ['ButtonWaitForPressAndRelease', 'ButtonWaitForPressAndRelease',
        '<b>ButtonWaitForPressAndRelease(<span foreground="brown">button</span>)</b>\n\n' +
        'Wait till a specific button is pressed and released.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">button</span>   BTNEXIT   BTN1 The exit (escape) button.\n' +
        '           BTNRIGHT  BTN2 The right button.\n' +
        '           BTNLEFT   BTN3 The left button.\n' +
        '           BTNCENTER BTN4 The enter button.\n' +
        '           BTNUP     BTN5 The up button.\n' +
        '           BTNDOWN   BTN6 The down button.', 'Button'],
    ['CircleOut', 'CircleOut(,,)', '<b>CircleOut(' +
        '<span foreground="brown">x</span>, ' +
        '<span foreground="brown">y</span>, ' +
        '<span foreground="brown">r</span>)</b>', 'Display'],
    ['EllipseOut','EllipseOut(,,,)','<b>EllipseOut(x, y, radiusX, radiusY)</b>\n\n' +
        'This function lets you draw an ellipse on the screen\n' +
        'with its center at the specified x and y location,\n' +
        'using the specified radii.', 'Display'],
    ['LcdText', 'LcdText(,,,)', '<b>LcdText(' +
        '<span foreground="brown">color</span>, ' +
        '<span foreground="brown">x</span>, <span foreground="brown">y</span>, ' +
        '<span foreground="brown">str</span>)</b>\n\n' +
        'Draw a text value on the screen at the specified x and y location.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">color</span>  1: black text, 0: white text on black background\n' +
        '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
        '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
        '  <span foreground="brown">str</span>    The text to output to the LCD screen.\n' +
        '<b>Example:</b>\n' +
        '  LcdText(1, 0, <span foreground="green">LCD_LINE1</span>, "Hello World!");', 'Display'],
    ['TextOut', 'TextOut(,,)', '<b>TextOut (' +
        '<span foreground="brown">x</span>, ' +
        '<span foreground="brown">y</span>, ' +
        '<span foreground="brown">str</span>)</b>\n\n' +
        'Draw a text value on the screen at the specified x and y location.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
        '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
        '  <span foreground="brown">str</span>    The text to output to the LCD screen.\n' +
        '<b>Example:</b>\n' +
        '  TextOut(0, <span foreground="green">LCD_LINE1</span>, "Hello World!");', 'Display'],
    ['LcdTextf', 'LcdTextf(,,,,)', '<b>LcdTextf(' +
        '<span foreground="brown">color</span>, ' +
        '<span foreground="brown">x</span>, <span foreground="brown">y</span>, ' +
        '<span foreground="brown">fmt</span>,...)</b>\n\n' +
        'Print text with variables, works like printf()\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">color</span>   1: black text, 0: white text with black background\n' +
        '  <span foreground="brown">x</span>       The x value for the start of the number output.\n' +
        '  <span foreground="brown">y</span>       The text line number for the number output.\n' +
        '  <span foreground="brown">fmt</span>     The string to output to the LCD screen.\n' +
        '<b>Example:</b>\n' +
        '  int x = 1234567890;\n' +
        '  LcdTextf(1, 10, LCD_LINE7, "Variable: %d", x);', 'Display'],
    ['LcdBmpFile', 'LcdBmpFile(,,,)', '<b>LcdBmpFile(' +
        '<span foreground="brown">color</span>, ' +
        '<span foreground="brown">x</span>, <span foreground="brown">y</span>, ' +
        '<span foreground="brown">name)</b>\n\n', 'Display'],
    ['NumOut', 'NumOut(,,)', '<b>NumOut(' +
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
    ['LcdSelectFont', 'LcdSelectFont()', '<b>LcdSelectFont(' +
        '<span foreground="brown">FontType</span>)</b>\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">FontType</span>  0 normal\n' +
        '            1 small, bold\n' +
        '            2 large\n' +
        '            3 tiny', 'Display'],
    ['LcdClearDisplay', 'LcdClearDisplay()','', 'Display'],
    ['LcdIcon', 'LcdIcon(,,,,)', '<b>LcdIcon(color, x, y, IconType, IconNum)</b>\n\n' +
        'Draw a icon on the screen at the specified location\n' +
        '<b>Parameters:</b>\n' +
        'IconType   ICONTYPE_NORMAL 0   IconNum 0..34\n' +
        '           ICONTYPE_SMALL  1           0..21\n' +
        '           ICONTYPE_LARGE  2           0..27\n' +
        '           ICONTYPE_MENU   3           0..10\n' +
        '           ICONTYPE_ARROW  4           0..2', 'Display'],
    ['LcdUpdate', 'LcdUpdate()', '', 'Display'],
    ['LcdInit', 'LcdInit()', '', 'General'],
    ['LcdExit', 'LcdExit()', '', 'General'],
    ['LineOut', 'LineOut(,,,)', '<b>LineOut(' +
        '<span foreground="brown">x1</span>, ' +
        '<span foreground="brown">y1</span>, ' +
        '<span foreground="brown">x2</span>, ' +
        '<span foreground="brown">y2</span>)</b>\n\n' +
        'This function lets you draw a line on the screen\n' +
        'from x1, y1 to x2, y2.', 'Display'],
    ['MotorBusy', 'MotorBusy()', '<b>MotorBusy(' +
        '<span foreground="brown">output</span>)</b>\n\n' +
        'Returns 1 if motor is busy, 0 if not.\n\n' +
        '<b>Example:</b>\n' +
        ' while(MotorBusy(OUT_B));  // wait till motor finishes', 'Output'],
    ['MotorRotationCount', 'MotorRotationCount()', '<b>MotorRotationCount(' +
        '<span foreground="brown">output</span>)</b>\n\n' +
        'This function enables the program to read the tacho count in degrees as\n' +
        'sensor input. This count is set to 0 at boot time, not at program start.\n' +
        'See also: ResetRotationCount()', 'Output'],
    ['MotorTachoCount', 'MotorTachoCount()', '<b>MotorTachoCount(' +
        '<span foreground="brown">output</span>)</b>\n\n' +
        'This function enables reading current output tacho count in degrees.\n' +
        'This count is set to 0 at program start.\n' +
        'See also: ResetTachoCount()', 'Output'],
    ['OutputInit', 'OutputInit()', '', 'General'],
    ['OutputExit', 'OutputExit()', '', 'General'],
    ['OnFwd', 'OnFwd(,)', '<b>OnFwd(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>)</b>\n\n' +
        'Run motors forward with given power.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>   Desired output ports.\n' +
        '  <span foreground="brown">power</span>     Output power, 0 to 127.\n' +
        '            Can be negative to reverse direction.\n' +
        '<b>Example:</b>\n' +
        ' OnFwd(OUT_BC, 127);', 'Output'],
    ['OnFor', 'OnFor(,,)', '<b>OnFor(' +
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
    ['OnFwdEx', 'OnFwdEx(,,)', '<b>OnFwdEx(' +
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
    ['OnFwdReg', 'OnFwdReg(,)', '<b>OnFwdReg(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>)</b>\n\n' +
        'Forwards with given speed', 'Output'],
    ['OnFwdSync', 'OnFwdSync(,)', '<b>OnFwdSync(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>)</b>\n\n' +
        'Run two motors synchronized forwards with given speed.', 'Output'],
    ['OnFwdSyncEx', 'OnFwdSyncEx(,,,)', '<b>OnFwdSyncEx(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>, <span foreground="brown">turn</span>, ' +
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
    ['OnForSync', 'OnForSync(,,)', '<b>OnForSync(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">time</span>, ' +
        '<span foreground="brown">speed</span>)</b>\n\n', 'Output'],
    ['OnForSyncEx', 'OnForSyncEx(,,,,)', '<b>OnForSyncEx(' +
        '<span foreground="brown">Outputs</span>, ' +
        '<span foreground="brown">Time</span>, ' +
        '<span foreground="brown">Speed</span>, ' +
        '<span foreground="brown">Turn</span>, ' +
        '<span foreground="brown">Stop</span>)</b>\n\n', 'Output'],
    ['OnRev', 'OnRev(,)', '<b>OnRev(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>)</b>\n\n' +
        'Run motors backwards with given power.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>   Desired output ports.\n' +
        '  <span foreground="brown">power</span>     Output power, 0 to 127.\n' +
        '            Can be negative to reverse direction.\n' +
        '<b>Example:</b>\n' +
        '  OnRev(OUT_BC, 127);', 'Output'],
    ['OnRevEx', 'OnRevEx(,,)', '<b>OnRevEx(' +
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
    ['OnRevReg', 'OnRevReg()', '<b>OnRevReg(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>)</b>\n\n' +
        'Backwards with given speed', 'Output'],
    ['OnRevSync', 'OnRevSync(,)', '<b>OnRevSync(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>)</b>\n\n' +
        'Run two motors synchronized backwards with given speed.\n\n', 'Output'],
    ['OnRevSyncEx', 'OnRevSyncEx(,,,)', '<b>OnRevSyncEx(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>, <span foreground="brown">turn</span>, ' +
        '<span foreground="brown">reset</span>)</b>\n\n' +
        'Run two motors synchronized backwards with given speed and given turn ratio.\n' +
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
    ['OutputPower', 'OutputPower(,)', '<b>OutputPower(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>)</b>\n\n' +
        'This function enables setting the output percentage power on the output ports', 'Output'],
    ['OutputSpeed', 'OutputSpeed(,)','<b>OutputSpeed(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>)</b>\n\n' +
        'This function enables setting the output percentage speed on the output\n' +
        'ports. This modes automatically enables speed control, which means the\n' +
        'system will automatically adjust the power to keep the specified speed.', 'Output'],
    ['OutputStart', 'OutputStart()','<b>OutputStart(' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'This function enables starting the specified output port.', 'Output'],
    ['OutputStop', 'OutputStop(,)', '<b>OutputStop(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">useBrake</span>)</b>\n\n' +
        'This function enables stopping the specified output port.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">useBreak</span>   0: Float, 1: Break', 'Output'],
    ['OutputStepPower','OutputStepPower(,,,,)','<b>OutputStepPower(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>, ' +
        '<span foreground="brown">step1</span>, ' +
        '<span foreground="brown">step2</span>, ' +
        '<span foreground="brown">step3</span>)</b>\n\n' +
        'This function enables specifying a full motor power cycle in tacho counts.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">step1</span> specifyes the power ramp up periode in tacho counts, \n' +
        '  <span foreground="brown">step2</span> specifyes the constant power period in tacho counts,\n' +
        '  <span foreground="brown">step3</span> specifyes the power down period in tacho counts.', 'Output'],
    ['OutputStepSpeed', 'OutputStepSpeed(,,,,)', '<b>OutputStepSpeed(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>, ' +
        '<span foreground="brown">step1</span>, ' +
        '<span foreground="brown">step2</span>, ' +
        '<span foreground="brown">step3</span>)</b>\n\n' +
        'This function enables specifying a full motor power cycle in tacho counts.\n' +
        'The system will automatically adjust the power level to the motor to keep\n' +
        'the specified output speed.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">step1</span> specifyes the power ramp up periode in tacho counts,\n' +
        '  <span foreground="brown">step2</span> specifyes the constant power period in tacho counts,\n' +
        '  <span foreground="brown">step3</span> specifyes the power down period in tacho counts.', 'Output'],
    ['OutputStepSync', 'OutputStepSync(,,,)', '<b>OutputStepSync(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>, ' +
        '<span foreground="brown">turn</span>, ' +
        '<span foreground="brown">step</span>)</b>\n\n' +
        'This function enables synchronizing two motors. Synchronization should be\n' +
        'used when motors should run as synchrone as possible, for example to\n' +
        'archieve a model driving straight. Duration is specified in tacho counts.\n\n' +
        '<b>Parameters</b>\n' +
        '<span foreground="brown">turn</span>:  0  :  Motor will run with same power\n' +
        '       100:  One motor will run with specified power while the other will\n' +
        '             be close to zero\n' +
        '       200:  One motor will run with specified power forward while the other\n' +
        '             will run in the opposite direction at the same power level.\n' +
        '<span foreground="brown">step</span>:  Tacho pulses, 0 = Infinite', 'Output'],
    ['OutputTimePower', 'OutputTimePower(,,,,)', '<b>OutputTimePower(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>, ' +
        '<span foreground="brown">time1</span>, ' +
        '<span foreground="brown">time2</span>, ' +
        '<span foreground="brown">time3</span>)</b>\n\n' +
        'This function enables specifying a full motor power cycle in time.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">time1</span> specifyes the power ramp up periode in milliseconds,\n' +
        '  <span foreground="brown">time2</span> specifyes the constant power period in milliseconds,\n' +
        '  <span foreground="brown">time3</span> specifyes the power down period in milliseconds.', 'Output'],
    ['OutputTimeSpeed', 'OutputTimeSpeed(,,,,)', '<b>OutputTimePower(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>, ' +
        '<span foreground="brown">time1</span>, ' +
        '<span foreground="brown">time2</span>, ' +
        '<span foreground="brown">time3</span>)</b>\n\n' +
        'This function enables specifying a full motor power cycle in time.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">time1</span> specifyes the power ramp up periode in milliseconds,\n' +
        '  <span foreground="brown">time2</span> specifyes the constant power period in milliseconds,\n' +
        '  <span foreground="brown">time3</span> specifyes the power down period in milliseconds.', 'Output'],
    ['OutputTimeSync', 'OutputTimeSync(,,,)', '<b>OutputTimeSync('+ 
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>, ' +
        '<span foreground="brown">turn</span>, ' +
        '<span foreground="brown">time</span>)</b>\n\n' +
        'This function enables synchronizing two motors. Synchronization should be\n' +
        'used when motors should run as synchrone as possible, for example to\n' +
        'archieve a model driving straight. Duration is specified in time.', 'Output'],
    ['Off', 'Off()', '<b>Off(' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'Turn the specified outputs off (with braking).\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>  Desired output ports.\n\n' +
        '<b>Example:</b>\n' +
        ' Off(OUT_A); // turn off output A', 'Output'],
    ['PlayTone', 'PlayTone(,)', '<b>PlayTone(' +
        '<span foreground="brown">frequency</span>, ' +
        '<span foreground="brown">duration</span>)</b>\n\n', 'Sound'],
    ['PlayToneEx', 'PlayToneEx(,,)', '<b>PlayToneEx(' +
        '<span foreground="brown">frequency</span>, ' +
        '<span foreground="brown">duration</span>, ' +
        '<span foreground="brown">volume</span>)</b>\n\n', 'Sound'],
    ['PlaySound', 'PlaySound()', '<b>PlaySound(' +
        '<span foreground="brown">aCode</span>)</b>\n\n' +
        'Play a sound that mimics the RCX system sounds using one of the RCXSoundConstants.\n\n' +
        '<b>Parameters</b>\n' +
        '  aCode   SOUND_CLICK        key click sound\n' +
        '          SOUND_DOUBLE_BEEP  double beep\n' +
        '          SOUND_UP           sweep up\n' +
        '          SOUND_DOWN         sweep down\n' +
        '          SOUND_LOW_BEEP     error sound\n' +
        '          SOUND_FAST_UP      fast sweep up\n' +
        '<b>Example:</b>\n' +
        '  PlaySound(SOUND_CLICK);', 'Sound'],
    ['PlayTones', 'PlayTones()', '<b>PlayTones(tones[])</b>\n\n' +
        'Play a series of tones contained in the tones array.  Each element in\n' +
        'the array is an instance of the Tone structure, containing a frequency\n' +
        'and a duration.\n' +
        '<b>Example:</b>\n' +
        '  unsigned short melody[7][2] = {' +
        '    {TONE_D4, NOTE_QUARTER},       // = 1000ms / 4\n' +
        '    {TONE_E4, NOTE_EIGHT},\n' +
        '    {TONE_D4, NOTE_EIGHT},\n' +
        '    {TONE_F4, NOTE_EIGHT},\n' +
        '    {TONE_D4, NOTE_EIGHT},\n' +
        '    {TONE_E4, NOTE_EIGHT},\n' +
        '    {TONE_D4, 750}\n' +
        '  };\n' +
        '  PlayTones(melody);', 'Sound'],
    ['PlayFile', 'PlayFile()', '<b>PlayFile(<span foreground="brown">name</span>)</b>\n\n', 'Sound'],
    ['PointOut', 'PointOut(,)', '<b>PointOut(' +
        '<span foreground="brown">x</span>, <span foreground="brown">y</span>)</b>\n\n', 'Display'],
    ['ReadSensor', 'ReadSensor()', '<b>ReadSensor(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Readout of the actual sensor data\n' +
        '<b>Example:</b>\n' +
        '  int touched;\n' +
        '  touched = ReadSensor(IN_1);', 'Input'],
    ['ReadSensorData', 'ReadSensorData()', '', 'Input'],
    ['RectOut', 'RectOut(,,,)', '<b>RectOut(' +
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
        'Reset the angle of the gyrosensor to 0 by changing modes back and forth.\n' +
        'This will take 2 seconds and is NOT SURE to work as expected.\n\n' +
        '<b>Example:</b>\n' +
        '  ResetGyro();', 'Input'],
    ['ResetTachoCount', 'ResetTachoCount()', '<b>ResetTachoCount(' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'This function enables resetting the tacho count for the individual output\n' +
        'ports. The tacho count is also resetted at program start.', 'Input'],
    ['ResetRotationCount', 'ResetRotationCount()', '<b>ResetRotationCount(' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'This function enables the program to clear the tacho count used as sensor\n' +
        'input. This rotation count is resetted at boot time, not at program start.', 'Input'],
    ['ResetAllTachoCounts', 'ResetAllTachoCounts()', '<b>ResetAllTachoCounts(' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'Resets tacho and rotation count.', 'Input'],
    ['RotateMotor', 'RotateMotor(,,)', '<b>RotateMotor(' +
        '<span foreground="brown">output</span>, ' +
        '<span foreground="brown">speed</span>, ' +
        '<span foreground="brown">angle</span>)</b>\n\n' +
        'Rotate motor with given speed for a defined angle.\n' +
        'Code stops till the angle is reached', 'Output'],
    ['RotateMotorEx', 'RotateMotorEx(,,,,,)', '<b>RotateMotorEx(' +
        '<span foreground="brown">outputs</span>, <span foreground="brown">speed</span>, ' +
        '<span foreground="brown">angle</span>, <span foreground="brown">turn</span>, ' +
        '<span foreground="brown">sync</span>, <span foreground="brown">stop</span>)</b>\n\n' +
        'Rotate two motors with given speed and given turn ratio for\n' +
        'a definded angle. Code stops till the angle is reached.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>  Has to be OUT_AB, OUT_AC, OUT_AD, OUT_BC,\n' +
        '           OUT_BD or OUT_CD. Anything else is invalid.\n' +
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
    ['RotateMotorNoWait', 'RotateMotorNoWait(,,)', '<b>RotateMotorNoWait(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>, ' +
        '<span foreground="brown">angle</span>)</b>\n\n', 'Output'],
    ['SetPower', 'SetPower(,)', '<b>SetPower(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>)</b>\n\n' +
        'Negative values forward, positive values backwards', 'Output'],
    ['SetSensorTouch', 'SetSensorTouch()', '<b>SetSensorTouch(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Allocate EV3 Touch Sensor to specified input port in TOUCH_PRESS mode.\n' +
        'Returns 0: not pressed, 1: pressed\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorTouch(IN_1);', 'Input'],
    ['SetSensorLight', 'SetSensorLight()', '<b>SetSensorLight(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Allocate EV3 Color Sensor to specified input port in COL_REFLECT mode.\n' +
        'Returns the reflected light intensities in % [0...100].\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorLight(IN_1);', 'Input'],
    ['SetSensorColor', 'SetSensorColor()', '<b>SetSensorColor(' +
        '<span foreground="brown">input</span>)</b>\n\n', 'Input'],
    ['SetSensorUS', 'SetSensorUS()', '<b>SetSensorUS(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Allocate EV3 Ultrasonic Sensor to specified input port in US_DIST_CM mode.\n' +
        'Returns distance in cm [1...250].\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorUS(IN_1);', 'Input'],
    ['SetSensorIR', 'SetSensorIR()', '<b>SetSensorIR(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Allocate EV3 Infrared Sensor to specified input port in IR_PROX mode.\n' +
        'Returns distance in cm [1...250].\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorIR(IN_1);', 'Input'],
    ['SetSensorGyro', 'SetSensorGyro()', '<b>SetSensorGyro(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Allocate EV3 Gyro Sensor to specified input port in angle mode\n' +
        'The value read will return the angle in degrees from -32768 to 32767.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>  The Input port to configure.\n' +
        '<b>Example:</b>\n  SetSensorGyro(IN_1);', 'Input'],
    ['SetSensorNXTTouch', 'SetSensorNXTTouch()', '<b>SetSensorNXTTouch(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Configure the sensor on the specified port as a NXT-touch sensor.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorNXTTouch(IN_1);', 'Input'],
    ['SetSensorNXTLight', 'SetSensorNXTLight()', '<b>SetSensorNXTLight(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Configure the sensor on the specified port as a NXT-light sensor.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorNXTLight(IN_1);', 'Input'],
    ['SetSensorNXTSound', 'SetSensorNXTSound()', '<b>SetSensorNXTSound(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Configure the sensor on the specified port as a NXT-sound sensor.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorNXTSound(IN_1);', 'Input'],
    ['SetSensorMode', 'SetSensorMode()', '<b>SetSensorMode(' +
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
    ['SetIRBeaconCH', 'SetIRBeaconCH()', '', 'Input'],
    ['SetLedPattern', 'SetLedPattern()', '<b>SetLedPattern(' +
        '<span foreground="brown">pattern</span>)</b>\n\n', 'Button'],
    ['SetLedWarning', 'SetLedWarning()', '<b>SetLedWarning(' +
        '<span foreground="brown">value</span>)</b>\n\n', 'Button'],
    ['Wait', 'Wait()', '<b>Wait(<span foreground="brown">time_ms</span>)</b>\n\n' +
        'Make code sleep for specified amount of time.\n\n' + 
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">time_ms</span>   The number of milliseconds to sleep.\n\n' +
        '<b>Example:</b>\n' +
        ' Wait(1000);', 'General']
]
evc_consts = [
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
