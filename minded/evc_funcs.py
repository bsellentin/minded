# -*- coding: utf-8 -*-
evc_funcs = [
    ['InitEV3', 'InitEV3()', '<small><b>InitEV3()</b>\n\n' +
        'Initialization of all EV3-Functions.\n' +
        'Should be the first command in main.</small>'],
    ['CloseEV3', 'CloseEV3()', ''],
    ['ExitEV3', '', 'ExitEV3()'],
    ['FreeEV3', 'FreeEV3()', '<small><b>FreeEV3()</b>\n\n' +
        'Close and exit of all EV3-Functions</small>'],
    ['ButtonIsDown', 'ButtonIsDown()','<small><b>ButtonIsDown(' +
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
        '  while(!ButtonIsDown(BTNCENTER)){ //do something }</small>'],
    ['ButtonIsUp', 'ButtonIsUp()', '<small><b>ButtonIsUp(' +
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
        '  while(ButtonIsUp(BTNCENTER)){ //do something }</small>'],
    ['ButtonWaitForAnyPress', 'ButtonWaitForAnyPress()', 
        '<small><b>ButtonWaitForAnyPress(<span foreground="brown">time</span>)</b>\n\n' +
        'Waiting for button press for given time.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">time</span>  Time in milliseconds\n' +
        '<b>Example:</b>\n' +
        '  ButtonWaitForAnyPress(10000);  // waits max 10 seconds</small>'],
    ['ButtonWaitForPress', 'ButtonWaitForPress()',
        '<small><b>ButtonWaitForPress(<span foreground="brown">button</span>)</b>\n\n' +
        'Wait till a specific button is pressed.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">button</span>   BTNEXIT   BTN1 The exit (escape) button.\n' +
        '           BTNRIGHT  BTN2 The right button.\n' +
        '           BTNLEFT   BTN3 The left button.\n' +
        '           BTNCENTER BTN4 The enter button.\n' +
        '           BTNUP     BTN5 The up button.\n' +
        '           BTNDOWN   BTN6 The down button.</small>'],
    ['ButtonWaitForPressAndRelease', 'ButtonWaitForPressAndRelease',
        '<small><b>ButtonWaitForPressAndRelease(<span foreground="brown">button</span>)</b>\n\n' +
        'Wait till a specific button is pressed and released.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">button</span>   BTNEXIT   BTN1 The exit (escape) button.\n' +
        '           BTNRIGHT  BTN2 The right button.\n' +
        '           BTNLEFT   BTN3 The left button.\n' +
        '           BTNCENTER BTN4 The enter button.\n' +
        '           BTNUP     BTN5 The up button.\n' +
        '           BTNDOWN   BTN6 The down button.</small>'],
    ['CircleOut', 'CircleOut(,,)', '<small><b>CircleOut(' +
        '<span foreground="brown">x</span>, ' +
        '<span foreground="brown">y</span>, ' +
        '<span foreground="brown">r</span>)</b></small>'],
    ['LcdText', 'LcdText(,,,)', '<small><b>LcdText(' +
        '<span foreground="brown">color</span>, ' +
        '<span foreground="brown">x</span>, <span foreground="brown">y</span>, ' +
        '<span foreground="brown">str</span>)</b>\n\n' +
        'Draw a text value on the screen at the specified x and y location.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">color</span>  1: black text, 0: white text on black background\n' +
        '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
        '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
        '  <span foreground="brown">str</span>    The text to output to the LCD screen.\n' +
        '<b>Examples:</b>\n' +
        '  LcdText(1, 0, <span foreground="green">LCD_LINE1</span>, "Hello World!");</small>'],
    ['TextOut', 'TextOut(,,)', '<small><b>TextOut (' +
        '<span foreground="brown">x</span>, ' +
        '<span foreground="brown">y</span>, ' +
        '<span foreground="brown">str</span>)</b>\n\n' +
        'Draw a text value on the screen at the specified x and y location.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
        '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
        '  <span foreground="brown">str</span>    The text to output to the LCD screen.\n' +
        '<b>Examples:</b>\n' +
        '  TextOut(0, <span foreground="green">LCD_LINE1</span>, "Hello World!");</small>'],
    ['LcdTextf', 'LcdTextf(,,,,)', '<small><b>LcdTextf(' +
        '<span foreground="brown">color</span>, ' +
        '<span foreground="brown">x</span>, <span foreground="brown">y</span>, ' +
        '<span foreground="brown">fmt</span>,...)</b>\n\n' +
        'Print text with variables, works like printf()\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">color</span>   1: black text, 0: white text with black background\n' +
        '  <span foreground="brown">x</span>       The x value for the start of the number output.\n' +
        '  <span foreground="brown">y</span>       The text line number for the number output.\n' +
        '  <span foreground="brown">fmt</span>     The string to output to the LCD screen.\n' +
        '<b>Examples:</b>\n' +
        '  int x = 1234567890;\n' +
        '  LcdTextf(1, 10, LCD_LINE7, "Variable: %d", x);</small>'],
    ['NumOut', 'NumOut(,,)', '<small><b>NumOut(' +
        '<span foreground="brown">x</span>, ' +
        '<span foreground="brown">y</span>,  <span foreground="brown">value</span>)</b>\n\n' +
        'Draw a numeric value on the screen at the ' +
        'specified x and y location.\n' +
        'The y value must be a multiple of 8.\n\n<b>Parameters</b>\n' +
        '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
        '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
        '  <span foreground="brown">value</span>  The value to output to the LCD screen. Any numeric\n' +
        '         type is supported.\n' +
        '<b>Examples:</b>\n  NumOut(0, <span foreground="green">LCD_LINE1</span>, x);</small>'], 
    ['LcdClean', 'LcdClean()', '<small><b>LcdClean()</b>\n\n' +
        'Erase Display</small>'],
    ['LcdSelectFont', 'LcdSelectFont()', '<small><b>LcdSelectFont(' +
        '<span foreground="brown">FontType</span>)</b>\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">FontType</span>  0 normal\n' +
        '            1 small, bold\n' +
        '            2 large\n' +
        '            3 tiny</small>'],
    ['LcdClearDisplay', 'LcdClearDisplay()',''],
    ['LcdIcon', 'LcdIcon(,,,,)', '<small>LcdIcon(color, x, y, IconType, IconNum)</small>'],
    ['LcdUpdate', 'LcdUpdate()', ''],
    ['LcdInit', 'LcdInit()', ''],
    ['LcdExit', 'LcdExit()', ''],
    ['LineOut', 'LineOut(,,,)', '<small><b>LineOut(' +
        '<span foreground="brown">x1</span>, ' +
        '<span foreground="brown">y1</span>, ' +
        '<span foreground="brown">x2</span>, ' +
        '<span foreground="brown">y2</span>)</b></small>'],
    ['MotorBusy', 'MotorBusy()', '<small><b>MotorBusy(' +
        '<span foreground="brown">output</span>)</b>\n\n' +
        'Returns 1 if motor is busys, 0 if not.\n\n' +
        '<b>Example:</b>\n' +
        '  while(MotorBusy(OUT_B));  // wait till motor finishes</small>'],
    ['MotorRotationCount', 'MotorRotationCount()', '<small><b>MotorRotationCount(' +
        '<span foreground="brown">output</span>)</b>\n\n' +
        'This function enables the program to read the tacho count in degrees as\n' +
        'sensor input. This count is set to 0 at boot time, not at program start.\n' +
        'See also: ResetRotationCount()</small>'],
    ['MotorTachoCount', 'MotorTachoCount()', '<small><b>MotorTachoCount(' +
        '<span foreground="brown"output</span>)</b>\n\n' +
        'This function enables reading current output tacho count in degrees.\n' +
        'This count is set to 0 at program start.\n' +
        'See also: ResetTachoCount()</small>'],
    ['OutputInit', 'OutputInit()', ''],
    ['OutputExit', 'OutputExit()', ''],
    ['OnFwd', 'OnFwd(,)', '<small><b>OnFwd(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>)</b>\n\n' +
        'Run motors forward with given power.\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>   Desired output ports.\n' +
        '  <span foreground="brown">power</span>     Output power, 0 to 127.\n' +
        '            Can be negative to reverse direction.\n' +
        '<b>Example:</b>\n' +
        '  OnFwd(OUT_BC, 127);</small>'],
    ['OnFor', 'OnFor(,,)', '<small><b>OnFor(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">time</span>, <span foreground="brown">power</span>)</b>\n\n' +
        'Run motors for given time with given power.\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>   Desired output ports.\n' + 
        '  <span foreground="brown">time</span>      Desired time in milliseconds.\n' +
        '  <span foreground="brown">power</span>     Output power, 0 to 127.\n' +
        '            Can be negative to reverse direction.\n' +
        '<b>Example:</b>\n' +
        '  OnFor(OUT_BC, 1000, 50);</small>'],
    ['OnFwdEx', 'OnFwdEx(,,)', '<small><b>OnFwdEx(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>, ' +
        '<span foreground="brown">reset</span>)</b></small>'],
    ['OnFwdReg', 'OnFwdReg(,)', '<small><b>OnFwdReg(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>)</b>\n\n' +
        'Forwards with given speed</small>'],
    ['OnFwdSync', 'OnFwdSync(,)', '<small><b>OnFwdSync(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>)</b>\n\n' +
        'Run two motors synchronized forwards with given speed.</small>'],
    ['OnFwdSyncEx', 'OnFwdSyncEx(,,,)', '<small><b>OnFwdSyncEx(' +
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
        '  OnFwdSyncEx(OUT_BC, 50, 30, RESET_NONE);</small>'],
    ['OnForSync', 'OnForSync(,,)', '<small><b>OnForSync(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">time</span>, ' +
        '<span foreground="brown">speed</span>)</b></small>'],
    ['OnForSyncEx', 'OnForSyncEx(,,,,)', '<small><b>OnForSyncEx(' +
        '<span foreground="brown">Outputs</span>, ' +
        '<span foreground="brown">Time</span>, ' +
        '<span foreground="brown">Speed</span>, ' +
        '<span foreground="brown">Turn</span>, ' +
        '<span foreground="brown">Stop</span>)</b></small>'],
    ['OnRev', 'OnRev(,)', '<small><b>OnRev(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>)</b>\n\n' +
        'Run motors backwards with given power.\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>   Desired output ports.\n' +
        '  <span foreground="brown">power</span>     Output power, 0 to 127.\n' +
        '            Can be negative to reverse direction.\n' +
        '<b>Example:</b>\n' +
        '  OnRev(OUT_BC, 127);</small>'],
    ['OnRevEx', 'OnRevEx(,,)', '<small><b>OnRevEx(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>, ' +
        '<span foreground="brown">reset</span>)</b></small>'],
    ['OnRevReg', 'OnRevReg()', '<small><b>OnRevReg(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>)</b>\n\n' +
        'Backwards with given speed</small>'],
    ['OnRevSync', 'OnRevSync(,)', '<small><b>OnRevSync(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>)</b>\n\n' +
        'Run two motors synchronized backwards with given speed.\n\n</small>'],
    ['OnRevSyncEx', 'OnRevSyncEx(,,,)', '<small><b>OnRevSyncEx(' +
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
        '  OnRevSyncEx(OUT_BC, 50, 30, RESET_NONE);</small>'],
    ['OutputPower', 'OutputPower(,)', '<small><b>OutputPower(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>)</b>\n\n' +
        'This function enables setting the output percentage power on the output ports</small>'],
    ['OutputSpeed', 'OutputSpeed(,)','<small><b>OutputSpeed(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>)</b>\n\n' +
        'This function enables setting the output percentage speed on the output\n' +
        'ports. This modes automatically enables speed control, which means the\n' +
        'system will automatically adjust the power to keep the specified speed.</small>'],
    ['OutputStart', 'OutputStart()','<small><b>OutputStart(' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'This function enables starting the specified output port.</small>'],
    ['OutputStop', 'OutputStop(,)', '<small><b>OutputStop(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">useBrake</span>)</b>\n\n' +
        'This function enables stopping the specified output port.\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">useBreak</span>   0: Float, 1: Break</small>'],
    ['OutputStepSpeed','OutputStepSpeed(,,,,)','<small><b>OutputStepSpeed(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>, ' +
        '<span foreground="brown">step1</span>, ' +
        '<span foreground="brown">step2</span>, ' +
        '<span foreground="brown">step3</span>)</b>\n\n' +
        'This function enables specifying a full motor power cycle in tacho counts.\n' +
        'The system will automatically adjust the power level to the motor to keep\n' +
        'the specified output speed. Step1 specifyes the power ramp up periode in\n' +
        'tacho counts, step2 specifyes the constant power period in tacho counts,\n' +
        'step 3 specifyes the power down period in tacho counts.</small>'],
    ['OutputStepSync', 'OutputStepSync(,,,)', '<small><b>OutputStepSync(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>, ' +
        '<span foreground="brown">turn</span>, ' +
        '<span foreground="brown">step</span>)</b>\n\n' +
        'This function enables synchonizing two motors. Synchonization should be\n' +
        'used when motors should run as synchrone as possible, for example to\n' +
        'archieve a model driving straight. Duration is specified in tacho counts.\n' +
        '<span foreground="brown">turn</span>:  0  :  Motor will run with same power\n' +
        '       100:  One motor will run with specified power while the other will\n' +
        '             be close to zero\n' +
        '       200:  One motor will run with specified power forward while the other\n' +
        '             will run in the opposite direction at the same power level.\n' +
        '<span foreground="brown">step</span>:  Tacho pulses, 0 = Infinite</small>'],
    ['OutputTimePower', 'OutputTimePower(,,,,)', '<small><b>OutputTimePower(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>, ' +
        '<span foreground="brown">time1</span>, ' +
        '<span foreground="brown">time2</span>, ' +
        '<span foreground="brown">time3</span>)</b></small>'],
    ['OutputTimeSpeed', 'OutputTimeSpeed(,,,,)', '<small><b>OutputTimeSpeed(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>, ' +
        '<span foreground="brown">time1</span>, ' +
        '<span foreground="brown">time2</span>, ' +
        '<span foreground="brown">time3</span>)</b></small>'],
    ['OutputTimeSync', 'OutputTimeSync(,,,)', '<small><b>OutputTimeSync('+ 
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>, ' +
        '<span foreground="brown">turn</span>, ' +
        '<span foreground="brown">time</span>)</b></small>'],
    ['Off', 'Off()', '<small><b>Off(' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'Switch off motors</small>'],
    ['PlayTone', 'PlayTone(,)', '<small><b>PlayTone(' +
        '<span foreground="brown">frequency</span>, ' +
        '<span foreground="brown">duration</span>)</b></small>'],
    ['PlayToneEx', 'PlayToneEx(,,)', '<small><b>PlayToneEx(' +
        '<span foreground="brown">frequency</span>, ' +
        '<span foreground="brown">duration</span>, ' +
        '<span foreground="brown">volume</span>)</b></small>'],
    ['PlaySound', 'PlaySound()', '<small><b>PlaySound(' +
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
        '  PlaySound(SOUND_CLICK);</small>'],
    ['PlayTones', 'PlayTones()', '<small><b>PlayTones(tones[])</b>\n\n' +
        'Play a series of tones contained in the tones array.  Each element in\n' +
        'the array is an instance of the Tone structure, containing a frequency\n' +
        'and a duration.\n' +
        '<b>Example:</b>\n' +
        '  unsigned short melody[7][2] = {' +
        '    {TONE_D4, NOTE_QUARTER},   	// = 1000ms / 4\n' +
        '    {TONE_E4, NOTE_EIGHT},\n' +
        '    {TONE_D4, NOTE_EIGHT},\n' +
        '    {TONE_F4, NOTE_EIGHT},\n' +
        '    {TONE_D4, NOTE_EIGHT},\n' +
        '    {TONE_E4, NOTE_EIGHT},\n' +
        '    {TONE_D4, 750}\n' +
        '  };\n' +
        '  PlayTones(melody);</small>'],
    ['PointOut', 'PointOut(,)', '<small><b>PointOut(x, y)</b></small>'],
    ['RectOut', 'RectOut(,,,)', '<small><b>RectOut(x, y, w, h)</b></small>'],
    ['ResetGyro', 'ResetGyro()', '<small><b>ResetGyro()</b>\n\n' +
        'Reset the angle of the gyrosensor to 0 by changing modes back and forth.\n' +
        'This will take 2 seconds and is NOT SURE to work as expected.\n' +
        '<b>Example:</b>\n' +
        '  ResetGyro();</small>'],
    ['ResetTachoCount', 'ResetTachoCount()', '<small><b>ResetTachoCount(' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'This function enables resetting the tacho count for the individual output\n' +
        'ports. The tacho count is also resetted at program start.</small>'],
    ['ResetRotationCount', 'ResetRotationCount()', '<small><b>ResetRotationCount(' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'This function enables the program to clear the tacho count used as sensor\n' +
        'input. This rotation count is resetted at boot time, not at program start.</small>'],
    ['ResetAllTachoCounts', 'ResetAllTachoCounts()', '<small><b>ResetAllTachoCounts(' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'Resets tacho and rotation count.</small>'],
    ['RotateMotor', 'RotateMotor(,,)', '<small><b>RotateMotor(' +
        '<span foreground="brown">output</span>, ' +
        '<span foreground="brown">speed</span>, ' +
        '<span foreground="brown">angle</span>)</b>\n\n' +
        'Rotate motor with given speed for a defined angle.\n' +
        'Code stops till the angle is reached</small>'],
    ['RotateMotorEx', 'RotateMotorEx(,,,,,)', '<small><b>RotateMotorEx(' +
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
        '  RotateMotorEx(OUT_BC,50,720,200,TRUE,TRUE);   // drive pirouette</small>'],
    ['RotateMotorNoWait', 'RotateMotorNoWait(,,)', '<small><b>RotateMotorNoWait(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">speed</span>, ' +
        '<span foreground="brown">angle</span>)</b></small>'],
    ['SetPower', 'SetPower(,)', '<small><b>SetPower(' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">power</span>)</b>\n\n' +
        'Negative values forward, positive values backwards</small>'],
    ['SetSensorTouch', 'SetSensorTouch()', '<small><b>SetSensorTouch(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Allocate EV3 Touch Sensor to specified input port in TOUCH_PRESS mode.\n' +
        'Returns 0: not pressed, 1: pressed\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorTouch(IN_1);</small>'],
    ['SetSensorLight', 'SetSensorLight()', '<small><b>SetSensorLight(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Allocate EV3 Color Sensor to specified input port in COL_REFLECT mode.\n' +
        'Returns the reflected light intensities in % [0...100].\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorLight(IN_1);</small>'],
    ['SetSensorColor', 'SetSensorColor()', '<small><b>SetSensorColor(' +
        '<span foreground="brown">input</span>)</b></small>'],
    ['SetSensorUS', 'SetSensorUS()', '<small><b>SetSensorUS(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Allocate EV3 Ultrasonic Sensor to specified input port in US_DIST_CM mode.\n' +
        'Returns distance in cm [1...250].\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorUS(IN_1);</small>'],
    ['SetSensorIR', 'SetSensorIR()', '<small><b>SetSensorIR(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Allocate EV3 Infrared Sensor to specified input port in IR_PROX mode.\n' +
        'Returns distance in cm [1...250].\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorIR(IN_1);</small>'],
    ['SetSensorGyro', 'SetSensorGyro()', '<small><b>SetSensorGyro(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Allocate EV3 Gyro Sensor to specified input port in angle mode\n' +
        'The value read will return the angle in degrees from -32768 to 32767.\n\n' +
        '<b>Parameters</b>\n' +
	    '  <span foreground="brown">input</span>  The Input port to configure.\n' +
	    '<b>Example:</b>\n  SetSensorGyro(IN_1);</small>'],
    ['SetSensorNXTTouch', 'SetSensorNXTTouch()', '<small><b>SetSensorNXTTouch(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Configure the sensor on the specified port as a NXT-touch sensor.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorNXTTouch(IN_1);</small>'],
    ['SetSensorNXTLight', 'SetSensorNXTLight()', '<small><b>SetSensorNXTLight(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Configure the sensor on the specified port as a NXT-light sensor.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorNXTLight(IN_1);</small>'],
    ['SetSensorNXTSound', 'SetSensorNXTSound()', '<small><b>SetSensorNXTSound(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Configure the sensor on the specified port as a NXT-sound sensor.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">input</span>        The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorNXTSound(IN_1);</small>'],
    ['SetSensorMode', 'SetSensorMode()', '<small><b>SetSensorMode(' +
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
        '             IR_REMOTE  Controlling EV3 with Beacon</small>'],
    ['SetAllSensorMode', 'SetAllSensorMode()', 'obsolete'],
    ['SetIRBeaconCH', 'SetIRBeaconCH()', ''],
    ['SetLedPattern', 'SetLedPattern()', '<small><b>SetLedPattern(' +
        '<span foreground="brown">pattern</span>)</b></small>'],
    ['SetLedWarning', 'SetLedWarning()', '<small><b>SetLedWarning(' +
        '<span foreground="brown">value</span>)</b></small>'],
    ['ReadSensor', 'ReadSensor()', '<small><b>ReadSensor(' +
        '<span foreground="brown">input</span>)</b>\n\n' +
        'Readout of the actual sensor data</small>'],
    ['ReadSensorData', 'ReadSensorData()', ''],
    ['Wait', 'Wait()', '<small><b>Wait(<span foreground="brown">time_ms</span>)</b>\n\n' +
        'Make code sleep for specified amount of time.\n\n' + 
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">time_ms</span>   The number of milliseconds to sleep.\n' +
        '<b>Example:</b>\n' +
        '  Wait(1000);</small>']
]
