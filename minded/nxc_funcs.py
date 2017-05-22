# -*- coding: utf-8 -*-
nxc_funcs = [
            ['Acquire', 'Acquire()', '<small><b>Acquire (mutex <span foreground="brown">m</span>)</b>\n\n' +
                'Acquire the specified mutex variable. If another task already\n' +
                'has acquired the mutex then the current task will be suspended\n' +
                'until the mutex is released by the other task. This function\n' +
                'is used to ensure that the current task has exclusive access\n' +
                'to a shared resource, such as the display or a motor. After the\n' +
                'current task has finished using the shared resource the program\n' +
                'should call Release to allow other tasks to acquire the mutex.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">m</span>  The mutex to acquire.\n' +
                '<b>Examples:</b>\n' +
                '  mutex motorMutex;\n' +
                '  // ...\n' +
                '  Acquire(motorMutex); // make sure we have exclusive access\n' +
                '  // use the motors\n' +
                '  Release(motorMutex);</small>'], 
            ['ArrayInit', 'ArrayInit(,,)', '<small><b>ArrayInit (<span foreground="brown">aout[]</span>, ' +
                '<span foreground="brown">value</span>, <span foreground="brown">count</span>)</b>\n\n' +
                'Initialize an array to contain count elements with each element\n' +
                'equal to the value provided. To initialize a multi-dimensional\n' +
                'array, the value should be an array of N-1 dimensions, where N is\n' +
                'the number of dimensions in the array being initialized.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">aout</span>   The output array to initialize.\n' +
                '  <span foreground="brown">value</span>  The value to initialize each element to.\n' +
                '  <span foreground="brown">count</span>  The number of elements to create in the output array.\n' +
                '<b>Examples:</b>\n' +
                '  int myArray[];\n' +
                '  ArrayInit(myArray, 0, 10); // 10 elements == zero</small>' ], 
            ['ArrayLen', 'ArrayLen()', '<small><b>ArrayLen (<span foreground="brown">data[]</span>)</b>\n\n' +
                'Return the length of the specified array. Any type of array\n' +
                'of up to four dimensions can be passed into this function.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">data</span>  The array whose length you need to read.\n' +
                '<b>Returns</b>\n' +
                '  The length of the specified array.\n' +
                '<b>Examples:</b>\n' +
                '  x = ArrayLen(myArray);</small>'],
            ['BluetoothStatus', 'BluetoothStatus()', '<small><b>BluetoothStatus (<span foreground="brown">conn</span>)</b>\n\n' +
                'Check the status of the bluetooth subsystem for the specified\n' +
                'connection slot.\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">conn</span>    The connection slot (0..3).\n' +
                '          Connections 0 through 3 are for bluetooth connections.\n' +
                '<b>Returns</b>\n' +
                '  The bluetooth status for the specified connection.\n' +
                '<b>Examples:</b>\n' +
                '  x = BluetoothStatus(1);</small>'],
            ['ButtonCount', 'ButtonCount()', '<small><b>ButtonCount (<span foreground="brown">btn</span>, ' +
                '<span foreground="brown">resetCount</span> = false)</b>\n\n' +
                'Return the number of times the specified button has been pressed\n' +
                'since the last time the button press count was reset. Optionally\n' +
                'clear the count after reading it.\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">btn</span>           The button to check.\n' +
                '  <span foreground="brown">resetCount</span>    Whether or not to reset the press counter.\n' +
                '<b>Returns</b>\n' +
                '  The button press count.\n' +
                '<b>Examples:</b>\n' +
                '  value = ButtonCount(BTNRIGHT, true);</small>'], 
            ['ButtonLongPressCount', 'ButtonLongPressCount()', ''], 
            ['ButtonPressCount', 'ButtonPressCount()', ''], 
            ['ButtonPressed', 'ButtonPressed()', '<small><b>ButtonPressed (<span foreground="brown">btn</span>, ' +
                '<span foreground="brown">resetCount</span> = false)</b>\n\n' +
                'Check for button press. This function checks whether the specified\n' +
                'button is pressed or not. You may optionally reset the press count.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">btn</span>         The button to check. See Button name constants.\n' +
                '  <span foreground="brown">resetCount</span>  Whether or not to reset the press counter.\n' +
                '<b>Returns</b>\n' +
                '  A boolean value indicating whether the button is pressed or not.\n' +
                '<b>Examples:</b>\n' +
                '  // Wait until user presses and releases exit button before continuing loop\n' +
                '  while(!(ButtonPressed(BTNEXIT, 0)));\n' +
                '  while(ButtonPressed(BTNEXIT, 0));</small>'], 
            ['ButtonState', 'ButtonState()', '<small><b>ButtonState (<span foreground="brown">btn</span>)</b>\n\n' +
                'Get the state of the specified button.\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">btn</span>    The button to check.\n' +
                '<b>Returns</b>\n' +
                '  The button state.\n' +
                '<b>Examples:</b>\n' +
                '  value = ButtonState(BTNLEFT);</small>'],
            ['ClearScreen', 'ClearScreen()', '<small><b>ClearScreen ()</b>\n\n' +
                'Clear LCD screen. This function lets you clear\n' +
                'the NXT LCD to a blank screen.\n\n' +
                '<b>Example:</b>\n' +
                '  ClearScreen();</small>'], 
            ['ClearSensor', 'ClearSensor()', '<small><b>ClearSensor (<span foreground="brown">port</span>)</b>\n\n' +
                'Clear the value of a sensor - only affects sensors that are\n' +
                'configured to measure a cumulative quantity such as rotation\n' +
                'or a pulse count.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>  The Input port to clear.\n' +
                '<b>Examples:</b>\n' +
                '  ClearSensor(IN_1);</small>'], 
            ['CircleOut', 'CircleOut(,,)', '<small><b>CircleOut (<span foreground="brown">x</span>,' +
                ' <span foreground="brown">y</span>, <span foreground="brown">radius</span>,' +
                ' <span foreground="brown">options</span> = DRAW_OPT_NORMAL)</b>\n\n' +
                'Draw a circle on the screen with its center at the specified\n' +
                'x and y location, using the specified radius. Optionally specify\n' +
                'drawing options. If this argument is not specified it defaults\n' +
                'to DRAW_OPT_NORMAL.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">x</span>        The x value for the center of the circle.\n' +
                '  <span foreground="brown">y</span>        The y value for the center of the circle.\n' +
                '  <span foreground="brown">radius</span>   The radius of the circle.\n' +
                '  <span foreground="brown">options</span>  The optional drawing options.\n' +
                '           <b>Warning:</b> These options require the\n' +
                '           enhanced NBC/NXC firmware\n' +
                '<b>Examples:</b>\n' +
                '  CircleOut(20, 50, 20);</small>'], 
            ['Coast', 'Coast()', '<small><b>Coast (<span foreground="brown">outputs</span>)</b>\n\n' +
                'Coast motors. Turn off the specified outputs, making them coast to a stop.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '<b>Examples:</b>\n' +
                '  Coast(OUT_A); // coast output A</small>'], 
            ['CurrentTick', 'CurrentTick()', '<small><b>CurrentTick ()</b>\n\n' +
                'Read the current system tick.\n\n' +
                '<b>Returns</b>\n' +
                '  The current system tick count.\n' +
                '<b>Examples:</b>\n' +
                '  long tick;\n' +
                '  tick = CurrentTick();</small>'], 
            ['CreateFile', 'CreateFile()', ''], 
            ['CloseFile', 'CloseFile()', ''],
            ['DeleteFile', 'DeleteFile()', ''],
            ['Float', 'Float()', '<small><b>Float (<span foreground="brown">outputs</span>)</b>\n\n' +
                'Float motors. Make outputs float. Float is an alias for Coast.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '<b>Examples:</b>\n' +
                '  Float(OUT_A); // float output A</small>'],
            ['GraphicOut', 'GraphicOut(,,)', '<small><b>GraphicOut (<span foreground="brown">x</span>,' +
                ' <span foreground="brown">y</span>, <span foreground="brown">filename</span>,' +
                ' <span foreground="brown">options</span> = DRAW_OPT_NORMAL)</b>\n\n' + 
                'Draw a graphic image file on the screen at the specified\n' +
                'x and y location. Optionally specify drawing options. If\n' +
                'this argument is not specified it defaults to DRAW_OPT_NORMAL.\n\n' + 
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">x</span>         The x value for the position\n' +
                '  <span foreground="brown">y</span>         The y value for the position\n' +
                '  <span foreground="brown">filename</span>  The filename of the RIC graphic image.\n' +
                '  <span foreground="brown">options</span>   The optional drawing options.\n' +
                '            <b>Warning:</b> These options require the\n' +
                '            enhanced NBC/NXC firmware\n' +
                '<b>Examples:</b>\n' +
                '  GraphicOut(40, 40, "image.ric");</small>'],
            ['LineOut', 'LineOut(,,,)', '<small><b>LineOut (<span foreground="brown">x1</span>,' +
                ' <span foreground="brown">y1</span>, <span foreground="brown">x2</span>,' +
                ' <span foreground="brown">y2</span>, <span foreground="brown">options</span> = DRAW_OPT_NORMAL)</b>\n\n' +
                'This function lets you draw a line on the screen from x1, y1\n' +
                'to x2, y2. Optionally specify drawing options. If this argument\n' +
                'is not specified it defaults to DRAW_OPT_NORMAL.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">x1</span>       The x value for the start of the line.\n' +
                '  <span foreground="brown">y1</span>       The y value for the start of the line.\n' +
                '  <span foreground="brown">x2</span>       The x value for the end of the line.\n' +
                '  <span foreground="brown">y2</span>       The y value for the end of the line.\n' +
                '  <span foreground="brown">options</span>  The optional drawing options.\n' +
                '           <b>Warning:</b> These options require the\n' +
                '           enhanced NBC/NXC firmware\n' +
                '<b>Examples:</b>\n' +
                '    LineOut(0, 0, <span foreground="green">DISPLAY_WIDTH</span>,' +
                ' <span foreground="green">DISPLAY_HEIGHT</span>);</small>'],
            ['MotorRotationCount', 'MotorRotationCount()', '<small><b>MotorRotationCount' +
                ' (<span foreground="brown">output</span>)</b>\n\n' +
                'Get the program-relative position counter value of the specified output.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">output</span>  Desired output port. Can be OUT_A, OUT_B, OUT_C.\n' +
                '<b>Returns</b>\n' +
                '  The program-relative position counter value of the specified output.\n' +
                '<b>Examples:</b>\n' +
                '  long deg = MotorRotationCount(OUT_A);</small>'],
            ['NumOut', 'NumOut(,,)', '<small><b>NumOut (<span foreground="brown">x</span>,' +
                ' <span foreground="brown">y</span>,  <span foreground="brown">value</span>)</b>\n\n' +
                'Draw a numeric value on the screen at the ' +
                'specified x and y location.\n' +
                'The y value must be a multiple of 8.\n\n<b>Parameters</b>\n' +
                '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
                '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
                '  <span foreground="brown">value</span>  The value to output to the LCD screen. Any numeric\n' +
                '         type is supported.\n' +
                '<b>Examples:</b>\n  NumOut(0, <span foreground="green">LCD_LINE1</span>, x);</small>'], 
            ['NumToStr', 'NumToStr()', '<small><b>NumToStr (<span foreground="brown">num</span>)</b>\n\n' +
                'Return the string representation of the specified numeric value.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">num</span>   A number.\n' +
                '<b>Returns</b>\n' +
                '  The string representation of the parameter num.\n' +
                '<b>Examples:</b>\n' +
                '  msg = NumToStr(-2); // returns "-2" in a string</small>'],
            ['OnFwd', 'OnFwd(,)', '<small><b>OnFwd (<span foreground="brown">outputs</span>, ' +
                '<span foreground="brown">pwr</span>)</b>\n\n' +
                'Run motors forward. Set outputs to forward direction and turn them on.\n\n' +
                '<b>Parameters:</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '  <span foreground="brown">pwr</span>      Output power, 0 to 100.\n' +
                '       Can be negative to reverse direction.\n' +
                '<b>Example:</b>\n' +
                '  OnFwd(OUT_A, 75);</small>'], 
            ['OnRev', 'OnRev(,)', '<small><b>OnRev (<span foreground="brown">outputs</span>,' +
                ' <span foreground="brown">pwr</span>)</b>\n\n' +
                'Run motors backward. Set outputs to reverse direction and turn them on.\n\n' +
                '<b>Parameters:</b>\n  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
                '<b>Example:</b>\n' +
                '  OnRev(OUT_A, 75);</small>'], 
            ['OnFwdReg', 'OnFwdReg(,,)', '<small><b>OnFwdReg (<span foreground="brown">outputs</span>,' +
                ' <span foreground="brown">pwr</span>, <span foreground="brown">regmode</span> )</b>\n\n' +
                'Run motors forward using the specified regulation mode.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
                '  <span foreground="brown">regmode</span>  Regulation modes, can be\n' +
                '               OUT_REGMODE_IDLE   none\n'+
                '               OUT_REGMODE_SPEED  speed regulation\n' +
                '               OUT_REGMODE_SYNC   multi-motor synchronization\n' +
                '               OUT_REGMODE_POS    position regulation\n' +
                '<b>Examples:</b>\n' +
                '  OnFwdReg(OUT_A, 75, OUT_REGMODE_SPEED); // regulate speed</small>'], 
            ['OnFwdRegPID', 'OnFwdRegPID(,,,,,)', ''], 
            ['OnFwdSync', 'OnFwdSync(,,)', '<small><b>OnFwdSync (<span foreground="brown">outputs</span>,' +
                ' <span foreground="brown">pwr</span>, <span foreground="brown">turnpct</span>)</b>\n\n'+ 
                'Run motors forward with regulated synchronization using the specified turn ratio.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
                '  <span foreground="brown">turnpct</span>  Turn ratio, -100 to 100. Negative TurnRatio values shift power\n' +
                '           toward the left motor while positive values shift power toward\n' +
                '           the right motor. An absolute value of 50 results in one motor\n' +
                '           stopping. An absolute value of 100 usually results in two motors\n' +
                '           turning in opposite directions at equal power.\n' +
                '<b>Examples:</b>\n' +
                '  OnFwdSync(OUT_AB, 75, -100); // spin right</small>'], 
            ['OnFwdSyncPID', 'OnFwdSyncPID(,,,,,)', ''],
            ['OnRevReg', 'OnRevReg(,,)', '<small><b>OnRevReg ( <span foreground="brown">outputs</span>,' +
            ' <span foreground="brown">pwr</span>, <span foreground="brown">regmode</span> )</b>\n\n' +
                'Run motors reverse using the specified regulation mode.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
                '  <span foreground="brown">regmode</span>  Regulation modes, can be\n' +
                '               OUT_REGMODE_IDLE   none\n'+
                '               OUT_REGMODE_SPEED  speed regulation\n' +
                '               OUT_REGMODE_SYNC   multi-motor synchronization\n' +
                '               OUT_REGMODE_POS    position regulation\n' +
                '<b>Examples:</b>\n' +
                '  OnRevReg(OUT_A, 75, OUT_REGMODE_SPEED); // regulate speed</small>'], 
            ['OnRevRegPID', 'OnRevRegPID(,,,,,)', ''], 
            ['OnRevSync', 'OnRevSync(,,)', '<small><b>OnRevSync (<span foreground="brown">outputs</span>,' +
                ' <span foreground="brown">pwr</span>, <span foreground="brown">turnpct</span>)</b>\n\n'+ 
                'Run motors reverrse with regulated synchronization using the specified turn ratio.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
                '  <span foreground="brown">turnpct</span>  Turn ratio, -100 to 100. Negative TurnRatio values shift power\n' +
                '           toward the left motor while positive values shift power toward\n' +
                '           the right motor. An absolute value of 50 results in one motor\n' +
                '           stopping. An absolute value of 100 usually results in two motors\n' +
                '           turning in opposite directions at equal power.\n' +
                '<b>Examples:</b>\n' +
                '  OnRevSync(OUT_AB, 75, -100); // spin left</small>'], 
            ['OnRevSyncPID', 'OnRevSyncPID(,,,,,)', ''],
            ['PlayTone', 'PlayTone(,)', '<small><b>PlayTone (<span foreground="brown">frequency</span>,' +
                ' <span foreground="brown">duration</span>)</b>\n\n' +
                'Play a single tone of the specified frequency and duration.\nThe frequency is in Hz.' +
                ' The duration is in 1000ths of a second.\nThe tone is played at the loudest sound level.\n\n' +
                '<b>Parameters</b>\n  <span foreground="brown">frequency</span>  The desired tone frequency, in Hz.\n' +
                '  <span foreground="brown">duration</span>   The desired tone duration, in ms.\n' + 
                '<b>Examples:</b>\n' +
                '  PlayTone(440, 500);     // Play Tone A for one half second</small>'], 
            ['PlayTones', 'PlayTones()', ''],
            ['PlayToneEx', 'PlayToneEx()', ''],
            ['PlayFile', 'PlayFile()', '<small><b>PlayFile (<span foreground="brown">filename</span> )</b>\n\n' +
                'Play the specified file. The sound file can either be\n' +
                'an RSO file or it can be an NXT melody (RMD) file containing\n' +
                'frequency and duration values.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">filename</span>    The name of the sound or melody file to play.\n' +
                '<b>Examples:</b>\n' +
                '  PlayFile("startup.rso");</small>'],
            ['PlayFileEx', 'PlayFileEx(,,)', ''],
            ['PointOut', 'PointOut()', '<small><b>PointOut (<span foreground="brown">x</span>,' +
                ' <span foreground="brown">y</span>, <span foreground="brown">options</span>' +
                ' = DRAW_OPT_NORMAL)</b>\n\n' +
                'This function lets you draw a point on the screen at x, y.\n' +
                'Optionally specify drawing options. If this argument is not\n' +
                'specified it defaults to DRAW_OPT_NORMAL.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">x</span>        The x value for the point.\n' +
                '  <span foreground="brown">y</span>        The y value for the point.\n' +
                '  <span foreground="brown">options</span>  The optional drawing options.\n' +
                '           <b>Warning:</b> These options require the\n' +
                '           enhanced NBC/NXC firmware\n' +
                '<b>Examples:</b>\n' +
                '  PointOut(40, 40);</small>'], 
            ['Precedes', 'Precedes()', '<small><b>Precedes (<span foreground="brown">task1</span>,' +
                ' <span foreground="brown">task2</span>, ..., <span foreground="brown">taskN</span>)</b>\n\n' +
                'Schedule the listed tasks for execution once the current task has\n' +
                'completed executing. The tasks will all execute simultaneously\n' +
                'unless other dependencies prevent them from doing.\n' +
                'This statement should be used once within a task, preferably at\n' +
                'the start of the task definition. Any number of tasks may be listed\n' +
                'in the Precedes statement.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">task1</span>   The first task to start after the current task ends.\n' +
                '  <span foreground="brown">task2</span>   The second task to start after the current task ends.\n' +
                '  <span foreground="brown">taskN</span>   The last task to start after the current task ends.\n' +
                '<b>Examples:</b>\n' +
                '  Precedes(moving, drawing, playing);</small>'],
            ['Random', 'Random()', '<small><b>Random (<span foreground="brown">n = 0</span>)</b>\n\n' +
                'Generate random number. The returned value will range between 0 and n (exclusive).\n\n' + 
                '<b>Parameters</b>\n  <span foreground="brown">n</span> The maximum unsigned value desired (optional).\n' +
                '<b>Examples:</b>\n  int x = Random(100); // unsigned int between 0..99\n' +
                '  int x = Random(); // signed int between -32767..32767</small>'], 
            ['RectOut', 'RectOut(,,,)', '<small><b>RectOut (<span foreground="brown">x</span>,' +
                ' <span foreground="brown">y</span>, <span foreground="brown">width</span>,' +
                ' <span foreground="brown">height</span>, <span foreground="brown">options</span>' +
                ' = DRAW_OPT_NORMAL)</b>\n\n' +
                'This function draws a rectangle on the screen at x, y with the\n' +
                'specified width and height. Optionally specify drawing options.\n' +
                'If this argument is not specified it defaults to DRAW_OPT_NORMAL.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">x</span>        The x value for the top left corner of the rectangle.\n' +
                '  <span foreground="brown">y</span>        The y value for the top left corner of the rectangle.\n' +
                '  <span foreground="brown">width</span>    The width of the rectangle.\n' +
                '  <span foreground="brown">height</span>   The height of the rectangle.\n' +
                '  <span foreground="brown">options</span>  The optional drawing options.\n' +
                '           <b>Warning:</b> These options require the\n' +
                '           enhanced NBC/NXC firmware\n' +
                '<b>Examples:</b>\n' +
                '  RectOut(40, 40, 30, 10);</small>'],
            ['Release', 'Release()', '<small><b>Release (mutex <span foreground="brown">m</span>)</b>\n\n' +
                'Release the specified mutex variable. Use this to relinquish\n' +
                'a mutex so that it can be acquired by another task. Release\n' +
                'should always be called after a matching call to Acquire and\n' +
                'as soon as possible after a shared resource is no longer needed.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">m</span>  The mutex to release.\n' +
                '<b>Examples:</b>\n' +
                '  Acquire(motorMutex); // make sure we have exclusive access\n' +
                '  // use the motors\n' +
                '  Release(motorMutex); // release mutex for other tasks</small>'], 
            ['RenameFile', 'RenameFile()', ''], 
            ['ResetScreen', 'ResetScreen()', '<small><b>ResetScreen ()</b>\n\n'+
                'Reset LCD screen. This function lets you restore\n' +
                'the standard NXT running program screen.\n\n' +
                '<b>Examples:</b>\n' +
                '  ResetScreen();</small>'], 
            ['ResetSensor', 'ResetSensor()', ''], 
            ['ResetRotationCount', 'ResetRotationCount()', ''], 
            ['ResetTachoCount', 'ResetTachoCount()', ''], 
            ['ResetAllTachoCounts', 'ResetAllTachoCounts()', ''],
            ['RotateMotor', 'RotateMotor(,,)', '<small><b>RotateMotor (<span foreground="brown">outputs</span>,' +
                ' <span foreground="brown">pwr</span>, <span foreground="brown">angle</span>)</b>\n\n' +
                'Rotate motor. Run the specified outputs forward for the specified number of degrees.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
                '  <span foreground="brown">angle</span>    Angle limit, in degree. Can be negative to reverse direction.\n' +
                '<b>Example:</b>\n  RotateMotor(OUT_A, 75, 45);  // forward 45 degrees\n' +
                '  RotateMotor(OUT_A, -75, 45); // reverse 45 degrees</small>'], 
            ['RotateMotorEx', 'RotateMotorEx(,,,,,)', '<small><b>RotateMotorEx (<span foreground="brown">outputs</span>,' +
                ' <span foreground="brown">pwr</span>, <span foreground="brown">angle</span>,' +
                ' <span foreground="brown">turnpct</span>, <span foreground="brown">sync</span>,' +
                ' <span foreground="brown">stop</span>)</b>\n\n' +
                'Run the specified outputs forward for the specified number of degrees.\n' +
                'Also specify synchronization, turn percentage, and braking options.\n'  +
                'Use this function primarily with more than one motor specified via the\n' +
                'outputs parameter.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
                '  <span foreground="brown">angle</span>    Angle limit, in degree. Can be negative to reverse direction.\n' +
                '  <span foreground="brown">turnpct</span>  Turn ratio, -100 to 100.\n' +
                '  <span foreground="brown">sync</span>     Synchronise two motors. Should be set to true if a non-zero\n' +
                '           turn percent is specified or no turning will occur.\n' +
                '  <span foreground="brown">stop</span>     Specify whether the motor(s) should brake at the end of the\n' +
                '           rotation.\n' +
                '<b>Example</b>:\n' +
                '  RotateMotorEx(OUT_AB, 75, 360, 50, true, true);</small>'], 
            ['RotateMotorExPID', 'RotateMotorExPID()', ''], 
            ['RotateMotorPID', 'RotateMotorPID()', ''],
            ['ReadLn', 'ReadLn()', ''], 
            ['ReadLnString', 'ReadLnString()', ''], 
            ['ReceiveRemoteNumber', 'ReceiveRemoteNumber(,,)', '<small><b>ReceiveRemoteNumber ' +
                '(<span foreground="brown">queue</span>, <span foreground="brown">clear</span>, ' +
                '<span foreground="brown">val</span>)</b>\n\n' +
                'Read a numeric value from a mailbox and optionally remove it.\n' 
                'If the local mailbox is empty and this NXT is the master then\n' +
                'it attempts to poll one of its slave NXTs for a message from\n' +
                'the response mailbox that corresponds to the specified local\n' +
                'mailbox number.\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">queue</span>    The mailbox number.\n' +
                '  <span foreground="brown">clear</span>    A flag indicating whether to remove the message from\n' +
                '           the mailbox after it has been read.\n' +
                '  <span foreground="brown">val</span>      The numeric value that is read from the mailbox.\n' +
                '<b>Returns</b>\n' +
                '  A char value indicating whether the function call succeeded or not.\n' +
                '<b>Examples:</b>\n' +
                '  x = ReceiveRemoteNumber(queue, true, val);</small>'], 
            ['ReceiveRemoteString', 'ReceiveRemoteString(,,)', '<small><b>ReceiveRemoteString ' +
                '(<span foreground="brown">queue</span>, <span foreground="brown">clear</span>, ' +
                '<span foreground="brown">str</span>)</b>\n\n' +
                'Read a string value from a mailbox and optionally remove it.\n' 
                'If the local mailbox is empty and this NXT is the master then\n' +
                'it attempts to poll one of its slave NXTs for a message from\n' +
                'the response mailbox that corresponds to the specified local\n' +
                'mailbox number.\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">queue</span>    The mailbox number.\n' +
                '  <span foreground="brown">clear</span>    A flag indicating whether to remove the message from\n' +
                '           the mailbox after it has been read.\n' +
                '  <span foreground="brown">str</span>      The string value that is read from the mailbox.\n' +
                '<b>Returns</b>\n' +
                '  A char value indicating whether the function call succeeded or not.\n' +
                '<b>Examples:</b>\n' +
                '  x = ReceiveRemoteString(queue, true, strval);</small>'], 
            ['Sensor', 'Sensor()', '<small><b>Sensor (<span foreground="brown">port</span>)</b>\n\n' +
                'Return the processed sensor reading for a sensor on the specified port.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>  The sensor port.\n<b>Returns</b>\n  The sensor´s scaled value.\n' + 
                '<b>Examples:</b>\n  x = Sensor(IN_1); // read sensor 1</small>'], 
            ['SensorUS', 'SensorUS()', '<small><b>SensorUS (<span foreground="brown">port</span> )</b>\n\n' +
                'Read ultrasonic sensor value. Return the ultrasonic sensor distance value.\n' +
                'Since an ultrasonic sensor is an I2C digital sensor its value cannot be\n' +
                'read using the standard Sensor(n) value. The port must be configured as\n' +
                'a Lowspeed port before using this function.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>  The port to which the ultrasonic sensor is attached.\n' +
                '<b>Returns</b>\n' +
                '  The ultrasonic sensor distance value (0..255)\n' +
                '<b>Examples:</b>\n' +
                '  SetSensorLowspeed(IN_4);\n  x = SensorUS(IN_4); // read sensor 4</small>'], 
            ['SetSensorTouch', 'SetSensorTouch()', '<small><b>SetSensorTouch (' +
                '<span foreground="brown">port</span>)</b>\n\n' +
                'Configure a touch sensor on the specified Input port.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>  The Input port to configure.\n' +
                '<b>Examples:</b>\n  SetSensorTouch(IN_1);</small>'], 
            ['SetSensorLight', 'SetSensorLight()', '<small><b>SetSensorLight (' +
                '<span foreground="brown">port</span>, <span foreground="brown">bActive</span> = true)</b>\n\n' +
                'Configure the sensor on the specified port as an NXT light sensor.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>     The port to configure.\n' +
                '  <span foreground="brown">bActive</span>' +
                '  A boolean flag indicating whether to configure the port\n' +
                '           as an active or inactive light sensor. The default\n' +
                '           value for this optional parameter is true.\n' +
                '<b>Examples:</b>\n  SetSensorLight(IN_1);</small>'], 
            ['SetSensorSound', 'SetSensorSound()', '<small><b>SetSensorSound (' +
                '<span foreground="brown">port</span>, <span foreground="brown">bdBScaling</span> = true)</b>\n\n' +
                'Configure the sensor on the specified port as a sound sensor.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>        The port to configure.\n' +
                '  <span foreground="brown">bdBScaling</span>' +
                '  A boolean flag indicating whether to configure the\n' +
                '              port as a sound sensor with dB or dBA scaling.\n' +
                '              The default value for this optional parameter is\n' +
                '              true, meaning dB scaling.\n' +
                '<b>Examples:</b>\n  SetSensorSound(IN_1);</small>'],
            ['SetSensorLowspeed', 'SetSensorLowspeed()', '<small><b>SetSensorLowspeed (' +
                '<span foreground="brown">port</span>, <span foreground="brown">bIsPowered</span> = true)</b>\n\n' +
                'Configure an digital I2C sensor on the specified port for either\npowered (9 volt) or unpowered devices.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>         The port to configure.\n' +
                '  <span foreground="brown">bIsPowered</span>   A boolean flag indicating whether to configure\n' +
                '               the port for powered or unpowered I2C devices.\n' +
                '               Default value is true.\n' +
                '<b>Examples:</b>\n  SetSensorLowspeed(IN_1);</small>'],
            ['SetSensor', 'SetSensor()', '<small><b>SetSensor (<span foreground="brown">port</span>,' +
                ' <span foreground="brown">config</span>)</b>\n\n' +
                'Set the type and mode of the given sensor to the specified\n' +
                'configuration, which must be a special constant containing\n' +
                'both type and mode information.\n\n' +
                '<b>See Also</b>\n' +
                '  SetSensorType(), SetSensorMode(), and ResetSensor()\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>    The port to configure.\n' +
                '  <span foreground="brown">config</span>  The configuration constant containing both the type\n' +
                '          and mode: SENSOR_TOUCH, SENSOR_LIGHT, SENSOR_SOUND...\n' +
                '<b>Examples:</b>\n' +
                '  SetSensor(IN_1, SENSOR_TOUCH);</small>'], 
            ['SetSensorColorFull', 'SetSensorColorFull()', '<small><b>SetSensorColorFull (' +
                '<span foreground="brown">port</span>)</b>\n\n' +
                'Configure an NXT 2.0 full color sensor on the\n' +
                'specified port in full color mode.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>        The port to configure.\n' +
                '<b>Examples:</b>\n  SetSensorColorFull(IN_1);</small>'], 
            ['SetSensorColorBlue', 'SetSensorColorBlue()', ''], 
            ['SetSensorColorGreen', 'SetSensorColorGreen()', ''],
            ['SetSensorColorRed', 'SetSensorColorRed()', ''], 
            ['SetSensorColorNone', 'SetSensorColorNone()', ''], 
            ['SetSensorMode', 'SetSensorMode(,)', '<small><b>SetSensorMode (<span foreground="brown">port</span>,' +
                ' <span foreground="brown">mode</span>)</b>\n\n' +
                'Set a sensor\'s mode, which should be one of the predefined\n' +
                'sensor mode constants. A slope parameter for boolean conversion,\n' +
                'if desired, may be added to the mode. After changing the type\n' +
                'or the mode of a sensor port you must call ResetSensor to give\n' +
                'the firmware time to reconfigure the sensor port.\n\n' +
                '<b>See Also</b>\n' +
                '  SetSensorType(), SetSensor()\n' 
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>  The port to configure. See Input port constants.\n' +
                '  <span foreground="brown">mode</span>  The desired sensor mode. Can be:\n' +
                '          SENSOR_MODE_RAW          Raw value from 0 to 1023\n' +
                '          SENSOR_MODE_EDGE         Counts the number of boolean transitions\n' +
                '          SENSOR_MODE_PULSE        Counts the number of boolean periods\n' +
                '          SENSOR_MODE_PERCENT      Scaled value from 0 to 100\n' +
                '          SENSOR_MODE_CELSIUS      RCX temperature sensor value in degrees celcius\n' +
                '          SENSOR_MODE_FAHRENHEIT   RCX temperature sensor value in degrees fahrenheit\n' +
                '          SENSOR_MODE_ROTATION     RCX rotation sensor (16 ticks per revolution)\n' +
                '<b>Examples:</b>\n' +
                '  SetSensorMode(IN_1, SENSOR_MODE_RAW); // raw mode</small>'], 
            ['SetSensorType', 'SetSensorType()', ''], 
            ['SendRemoteNumber', 'SendRemoteNumber()', ''], 
            ['SendRemoteString', 'SendRemoteString()', ''], 
            ['SendResponseNumber', 'SendResponseNumber()', ''], 
            ['SendResponseString', 'SendResponseString()', ''],
            ['StartTask', 'StartTask()', '<small><b>StartTask (<span foreground="brown">task</span>)</b>\n\n' +
                'Start the specified task.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">task</span>   The task to start.\n' +
                '<b>Examples:</b>\n' +
                '  StartTask(sound); // start the sound task</small>'],
            ['StrCat', 'StrCat()', '<small><b>StrCat (<span foreground="brown">str1</span>,' +
                ' <span foreground="brown">str2</span>, <span foreground="brown">strN</span>)</b>\n\n' +
                'Return a string which is the result of concatenating all of the\n' +
                'string arguments together. This function accepts any number of\n' +
                'parameters which may be string variables, constants, or expressions.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">str1</span>   The first string.\n' +
                '  <span foreground="brown">str2</span>   The second string.\n' +
                '  <span foreground="brown">strN</span>   The Nth string.\n' +
                '<b>Returns</b>\n' +
                '  The concatenated string.\n' +
                '<b>Examples:</b>\n' +
                '  str1 = "Put";\n'+
                '  str2 = "me";\n' +
                '  str3 = "together";\n' +
                '  TextOut(0, LCD_LINE1, StrCat(str1, str2, str3))</small>;'], 
            ['StrLen', 'StrLen()', '<small><b>StrLen (<span foreground="brown">str</span>)</b>\n\n' +
                'Return the length of the specified string. The input string\n' +
                'parameter may be a variable, constant, or expression.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">str</span>   A string.\n' +
                '<b>Returns</b>\n' +
                '  The length of the string.\n' +
                '<b>Examples:</b>\n' +
                '  string msg = "hi there";\n' +
                '  byte x = StrLen(msg); // return the length of msg</small>'], 
            ['StrToNum', 'StrToNum()', '<small><b>StrToNum (<span foreground="brown">str</span>)</b>\n\n' +
                'Return the numeric value specified by the string passed to the\n' +
                'function. If the content of the string is not a numeric value\n' +
                'then this function returns zero. The input string parameter may\n' +
                'be a variable, constant, or expression.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">str</span>   A string.\n' +
                '<b>Returns</b>\n' +
                '  A number.\n' +
                '<b>Examples:</b>\n' +
                '  x = StrToNum(str);</small>'],
            ['TextOut', 'TextOut(,,)', '<small><b>TextOut (<span foreground="brown">x</span>,' +
                ' <span foreground="brown">y</span>, ' +
                '<span foreground="brown">str</span>)</b>\n\n' +
                'Draw a text value on the screen at the specified x and y location.\n' +
                'The y value must be a multiple of 8.\n\n' +
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
                '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
                '  <span foreground="brown">str</span>    The text to output to the LCD screen.\n' +
                '<b>Examples:</b>\n' +
                '  TextOut(0, <span foreground="green">LCD_LINE1</span>, "Hello World!");</small>'],
            ['Off', 'Off()', '<small><b>Off (<span foreground="brown">outputs</span>)</b>\n\n' +
                'Turn motors off. Turn the specified outputs off (with braking).\n\n' + 
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '<b>Examples:</b>\n' +
                '  Off(OUT_A); // turn off output A</small>'], 
            ['OpenFileRead', 'OpenFileRead()', ''],
            ['Wait', 'Wait()', '<small><b>Wait (<span foreground="brown">ms</span>)</b>\n\n' +
                'Make a task sleep for specified amount of time.\n\n' + 
                '<b>Parameters</b>\n' +
                '  <span foreground="brown">ms</span> The number of milliseconds to sleep.\n' +
                '<b>Example:</b>\n' +
                '  Wait(1000);</small>'], 
            ['WriteBytes', 'WriteBytes()', ''], 
            ['WriteLn', 'WriteLn()', ''], 
            ['WriteLnString', 'WriteLnString()', '']
            ]
