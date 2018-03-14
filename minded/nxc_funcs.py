# -*- coding: utf-8 -*-
nxc_funcs = [
    ['Acquire', 'Acquire(m)', '<b>Acquire (mutex <span foreground="brown">m</span>)</b>\n\n' +
        'Acquire the specified mutex variable. If another task already\n' +
        'has acquired the mutex then the current task will be suspended\n' +
        'until the mutex is released by the other task. This function\n' +
        'is used to ensure that the current task has exclusive access\n' +
        'to a shared resource, such as the display or a motor. After the\n' +
        'current task has finished using the shared resource the program\n' +
        'should call Release to allow other tasks to acquire the mutex.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">m</span>  The mutex to acquire.\n' +
        '<b>Example:</b>\n' +
        '  mutex motorMutex;\n' +
        '  // ...\n' +
        '  Acquire(motorMutex); // make sure we have exclusive access\n' +
        '  // use the motors\n' +
        '  Release(motorMutex);','Command'], 
    ['ArrayInit', 'ArrayInit(aout, value, count)',
        '<b>ArrayInit (<span foreground="brown">aout[]</span>, ' +
        '<span foreground="brown">value</span>, ' +
        '<span foreground="brown">count</span>)</b>\n\n' +
        'Initialize an array to contain count elements with each element\n' +
        'equal to the value provided. To initialize a multi-dimensional\n' +
        'array, the value should be an array of N-1 dimensions, where N is\n' +
        'the number of dimensions in the array being initialized.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">aout</span>   The output array to initialize.\n' +
        '  <span foreground="brown">value</span>  The value to initialize each element to.\n' +
        '  <span foreground="brown">count</span>  The number of elements to create in the output array.\n' +
        '<b>Example:</b>\n' +
        '  int myArray[];\n' +
        '  ArrayInit(myArray, 0, 10); // 10 elements == zero', 'Command'], 
    ['ArrayLen', 'ArrayLen(data)', '<b>ArrayLen (<span foreground="brown">data[]</span>)</b>\n\n' +
        'Return the length of the specified array. Any type of array\n' +
        'of up to four dimensions can be passed into this function.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">data</span>  The array whose length you need to read.\n' +
        '<b>Returns</b>\n' +
        '  The length of the specified array.\n' +
        '<b>Example:</b>\n' +
        '  x = ArrayLen(myArray);', 'Command'],
    ['BluetoothStatus', 'BluetoothStatus(conn)',
        '<b>BluetoothStatus (<span foreground="brown">conn</span>)</b>\n\n' +
        'Check the status of the bluetooth subsystem for the specified\n' +
        'connection slot.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">conn</span>    The connection slot (0..3).\n' +
        '          Connections 0 through 3 are for bluetooth connections.\n' +
        '<b>Returns</b>\n' +
        '  The bluetooth status for the specified connection.\n' +
        '<b>Example:</b>\n' +
        '  x = BluetoothStatus(1);', 'Communication'],
    ['ButtonCount', 'ButtonCount(btn)',
        '<b>ButtonCount (<span foreground="brown">btn</span>, ' +
        '<span foreground="brown">resetCount</span> = false)</b>\n\n' +
        'Return the number of times the specified button has been pressed\n' +
        'since the last time the button press count was reset. Optionally\n' +
        'clear the count after reading it.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">btn</span>           The button to check.\n' +
        '  <span foreground="brown">resetCount</span>    Whether or not to reset the press counter.\n' +
        '<b>Returns</b>\n' +
        '  The button press count.\n' +
        '<b>Example:</b>\n' +
        '  value = ButtonCount(BTNRIGHT, true);', 'Button'], 
    ['ButtonLongPressCount', 'ButtonLongPressCount(btn)',
        'ButtonLongPressCount(btn)', 'Button'], 
    ['ButtonPressCount', 'ButtonPressCount(btn)',
        '<b>ButtonPressCount (' +
        '<span foreground="brown">btn</span>)</b>\n\n' +
        'Get the press count of the specified button.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">btn</span>    The button to check.\n' +
        '<b>Returns</b>\n' +
        '  The button press count.\n' +
        '<b>Example:</b>\n' +
        '  value = ButtonPressCount(BTN1);', 'Button'], 
    ['ButtonPressed', 'ButtonPressed(btn, resetCount)',
        '<b>ButtonPressed (' +
        '<span foreground="brown">btn</span>, ' +
        '<span foreground="brown">resetCount</span> = false)</b>\n\n' +
        'Check for button press. This function checks whether the specified\n' +
        'button is pressed or not. You may optionally reset the press count.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">btn</span>         The button to check. See Button name constants.\n' +
        '  <span foreground="brown">resetCount</span>  Whether or not to reset the press counter.\n' +
        '<b>Returns</b>\n' +
        '  A boolean value indicating whether the button is pressed or not.\n' +
        '<b>Example:</b>\n' +
        '  // Wait until user presses and releases exit button before continuing loop\n' +
        '  while(!(ButtonPressed(BTNEXIT, 0)));\n' +
        '  while(ButtonPressed(BTNEXIT, 0));', 'Button'], 
    ['ButtonState', 'ButtonState(btn)',
        '<b>ButtonState (<span foreground="brown">btn</span>)</b>\n\n' +
        'Get the state of the specified button.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">btn</span>    The button to check.\n' +
        '<b>Returns</b>\n' +
        '  The button state.\n' +
        '<b>Example:</b>\n' +
        '  value = ButtonState(BTNLEFT);', 'Button'],
    ['ClearScreen', 'ClearScreen()',
        '<b>ClearScreen ()</b>\n\n' +
        'Clear LCD screen. This function lets you clear\n' +
        'the NXT LCD to a blank screen.\n\n' +
        '<b>Example:</b>\n' +
        '  ClearScreen();', 'Display'], 
    ['ClearSensor', 'ClearSensor(port)',
        '<b>ClearSensor (<span foreground="brown">port</span>)</b>\n\n' +
        'Clear the value of a sensor - only affects sensors that are\n' +
        'configured to measure a cumulative quantity such as rotation\n' +
        'or a pulse count.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>  The Input port to clear.\n' +
        '<b>Example:</b>\n' +
        '  ClearSensor(IN_1);', 'Input'],
    ['CircleOut', 'CircleOut(x, y, radius)',
        '<b>CircleOut (' +
        '<span foreground="brown">x</span>, ' +
        '<span foreground="brown">y</span>, ' +
        '<span foreground="brown">radius</span>, ' +
        '<span foreground="brown">options</span> = DRAW_OPT_NORMAL)</b>\n\n' +
        'Draw a circle on the screen with its center at the specified\n' +
        'x and y location, using the specified radius. Optionally specify\n' +
        'drawing options. If this argument is not specified it defaults\n' +
        'to DRAW_OPT_NORMAL.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">x</span>        The x value for the center of the circle.\n' +
        '  <span foreground="brown">y</span>        The y value for the center of the circle.\n' +
        '  <span foreground="brown">radius</span>   The radius of the circle.\n' +
        '  <span foreground="brown">options</span>  The optional drawing options.\n' +
        '           <b><span foreground="red">Warning:</span></b> These options require the\n' +
        '           enhanced NBC/NXC firmware\n\n' +
        '<b>Example:</b>\n' +
        '  CircleOut(20, 50, 20, DRAW_OPT_SHAPE_FILL);', 'Display'], 
    ['Coast', 'Coast(outputs)',
        '<b>Coast (<span foreground="brown">outputs</span>)</b>\n\n' +
        'Coast motors. Turn off the specified outputs, making them coast to a stop.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
        '<b>Example:</b>\n' +
        '  Coast(OUT_A); // coast output A', 'Output'], 
    ['CurrentTick', 'CurrentTick()', '<b>CurrentTick ()</b>\n\n' +
        'Read the current system tick.\n\n' +
        '<b>Returns</b>\n' +
        '  The current system tick count.\n' +
        '<b>Example:</b>\n' +
        '  long tick;\n' +
        '  tick = CurrentTick();', 'Command'], 
    ['CreateFile', 'CreateFile(fname, fsize, handle)',
        'CreateFile(fname, fsize, handle)\n\n' +
        '<b>Example:</b>\n' +
        '  result = CreateFile("data.txt", 1024, handle);', 'Loader'], 
    ['CloseFile', 'CloseFile(handle)',
        'CloseFile(handle)\n\n' +
        '<b>Example:</b>\n' +
        '  result = CloseFile(handle);', 'Loader'],
    ['DeleteFile', 'DeleteFile(fname)', 'DeleteFile(fname)\n\n' +
        '<b>Example:</b>\n' +
        '  result = DeleteFile("data.txt");', 'Loader'],
    ['Float', 'Float(outputs)',
        '<b>Float (<span foreground="brown">outputs</span>)</b>\n\n' +
        'Float motors. Make outputs float. Float is an alias for Coast.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
        '<b>Example:</b>\n' +
        '  Float(OUT_A); // float output A', 'Output'],
    ['GraphicOut', 'GraphicOut(x, y, filename)',
        '<b>GraphicOut (' +
        '<span foreground="brown">x</span>, ' +
        '<span foreground="brown">y</span>, ' +
        '<span foreground="brown">filename</span>, ' +
        '<span foreground="brown">options</span> = DRAW_OPT_NORMAL)</b>\n\n' + 
        'Draw a graphic image file on the screen at the specified\n' +
        'x and y location. Optionally specify drawing options. If\n' +
        'this argument is not specified it defaults to DRAW_OPT_NORMAL.\n\n' + 
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">x</span>         The x value for the position\n' +
        '  <span foreground="brown">y</span>         The y value for the position\n' +
        '  <span foreground="brown">filename</span>  The filename of the RIC graphic image.\n' +
        '  <span foreground="brown">options</span>   The optional drawing options.\n' +
        '            <b>Warning:</b> These options require the\n' +
        '            enhanced NBC/NXC firmware\n\n' +
        '<b>Example:</b>\n' +
        '  GraphicOut(40, 40, "image.ric");', 'Display'],
    ['LineOut', 'LineOut(x1, y1, x2, y2)',
        '<b>LineOut (' +
        '<span foreground="brown">x1</span>, ' +
        '<span foreground="brown">y1</span>, ' +
        '<span foreground="brown">x2</span>, ' +
        '<span foreground="brown">y2</span>, ' +
        '<span foreground="brown">options</span> = DRAW_OPT_NORMAL)</b>\n\n' +
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
        '           enhanced NBC/NXC firmware\n\n' +
        '<b>Example:</b>\n' +
        '    LineOut(0, 0, <span foreground="green">DISPLAY_WIDTH</span>,' +
        ' <span foreground="green">DISPLAY_HEIGHT</span>);', 'Display'],
    ['MotorRotationCount', 'MotorRotationCount(output)',
        '<b>MotorRotationCount' +
        ' (<span foreground="brown">output</span>)</b>\n\n' +
        'Get the program-relative position counter value of the specified output.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">output</span>  Desired output port. Can be OUT_A, OUT_B, OUT_C.\n' +
        '<b>Returns</b>\n' +
        '  The program-relative position counter value of the specified output.\n' +
        '<b>Example:</b>\n' +
        '  long deg = MotorRotationCount(OUT_A);', 'Output'],
    ['NumOut', 'NumOut(x, y, value)',
        '<b>NumOut (<span foreground="brown">x</span>, ' +
        '<span foreground="brown">y</span>, ' +
        '<span foreground="brown">value</span>)</b>\n\n' +
        'Draw a numeric value on the screen at the ' +
        'specified x and y location.\n' +
        'The y value must be a multiple of 8.\n\n<b>Parameters</b>\n' +
        '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
        '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
        '  <span foreground="brown">value</span>  The value to output to the LCD screen. Any numeric\n' +
        '         type is supported.\n' +
        '<b>Example:</b>\n  NumOut(0, <span foreground="green">LCD_LINE1</span>, x);', 'Display'], 
    ['NumToStr', 'NumToStr(num)',
        '<b>NumToStr (<span foreground="brown">num</span>)</b>\n\n' +
        'Return the string representation of the specified numeric value.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">num</span>   A number.\n' +
        '<b>Returns</b>\n' +
        '  The string representation of the parameter num.\n' +
        '<b>Example:</b>\n' +
        '  msg = NumToStr(-2); // returns "-2" in a string', 'C API'],
    ['OnFwd', 'OnFwd(outputs, pwr)',
        '<b>OnFwd (<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">pwr</span>)</b>\n\n' +
        'Run motors forward. Set outputs to forward direction and turn them on.\n\n' +
        '<b>Parameters:</b>\n' +
        '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
        '  <span foreground="brown">pwr</span>      Output power, 0 to 100.\n' +
        '       Can be negative to reverse direction.\n' +
        '<b>Example:</b>\n' +
        '  OnFwd(OUT_A, 75);', 'Output'], 
    ['OnRev', 'OnRev(outputs, pwr)',
        '<b>OnRev (<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">pwr</span>)</b>\n\n' +
        'Run motors backward. Set outputs to reverse direction and turn them on.\n\n' +
        '<b>Parameters:</b>\n' +
        '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
        '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
        '<b>Example:</b>\n' +
        '  OnRev(OUT_A, 75);', 'Output'], 
    ['OnFwdReg', 'OnFwdReg(outputs, pwr, regmode)',
        '<b>OnFwdReg (<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">pwr</span>, ' +
        '<span foreground="brown">regmode</span> )</b>\n\n' +
        'Run motors forward using the specified regulation mode.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
        '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
        '  <span foreground="brown">regmode</span>  Regulation modes, can be\n' +
        '               OUT_REGMODE_IDLE   none\n'+
        '               OUT_REGMODE_SPEED  speed regulation\n' +
        '               OUT_REGMODE_SYNC   multi-motor synchronization\n' +
        '               OUT_REGMODE_POS    position regulation\n' +
        '<b>Example:</b>\n' +
        '  OnFwdReg(OUT_A, 75, OUT_REGMODE_SPEED); // regulate speed', 'Output'], 
    ['OnFwdRegPID', 'OnFwdRegPID(outputs, pwr, regmode, p, i, d)',
        'OnFwdRegPID(outputs, pwr, regmode, p, i, d)', 'Output'], 
    ['OnFwdSync', 'OnFwdSync(outputs, pwr, turnpct)',
        '<b>OnFwdSync (<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">pwr</span>, ' +
        '<span foreground="brown">turnpct</span>)</b>\n\n'+ 
        'Run motors forward with regulated synchronization using the specified turn ratio.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
        '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
        '  <span foreground="brown">turnpct</span>  Turn ratio, -100 to 100. Negative TurnRatio values shift power\n' +
        '           toward the left motor while positive values shift power toward\n' +
        '           the right motor. An absolute value of 50 results in one motor\n' +
        '           stopping. An absolute value of 100 usually results in two motors\n' +
        '           turning in opposite directions at equal power.\n' +
        '<b>Example:</b>\n' +
        '  OnFwdSync(OUT_AB, 75, -100); // spin right', 'Output'], 
    ['OnFwdSyncPID', 'OnFwdSyncPID(outputs, pwr, turnpct, p, i, d)',
        'OnFwdSyncPID(outputs, pwr, turnpct, p, i, d)', 'Output'],
    ['OnRevReg', 'OnRevReg(outputs, pwr, regmode)',
        '<b>OnRevReg ( <span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">pwr</span>, ' +
        '<span foreground="brown">regmode</span> )</b>\n\n' +
        'Run motors reverse using the specified regulation mode.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
        '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
        '  <span foreground="brown">regmode</span>  Regulation modes, can be\n' +
        '               OUT_REGMODE_IDLE   none\n'+
        '               OUT_REGMODE_SPEED  speed regulation\n' +
        '               OUT_REGMODE_SYNC   multi-motor synchronization\n' +
        '               OUT_REGMODE_POS    position regulation\n' +
        '<b>Example:</b>\n' +
        '  OnRevReg(OUT_A, 75, OUT_REGMODE_SPEED); // regulate speed', 'Output'], 
    ['OnRevRegPID', 'OnRevRegPID(outputs, pwr, regmode, p, i, d)',
        'OnRevRegPID(outputs, pwr, regmode, p, i, d)', 'Output'], 
    ['OnRevSync', 'OnRevSync(outputs, pwr, turnpct)', 
        '<b>OnRevSync (<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">pwr</span>, ' +
        '<span foreground="brown">turnpct</span>)</b>\n\n'+ 
        'Run motors reverrse with regulated synchronization using the specified turn ratio.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
        '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
        '  <span foreground="brown">turnpct</span>  Turn ratio, -100 to 100. Negative TurnRatio values shift power\n' +
        '           toward the left motor while positive values shift power toward\n' +
        '           the right motor. An absolute value of 50 results in one motor\n' +
        '           stopping. An absolute value of 100 usually results in two motors\n' +
        '           turning in opposite directions at equal power.\n' +
        '<b>Example:</b>\n' +
        '  OnRevSync(OUT_AB, 75, -100); // spin left', 'Output'], 
    ['OnRevSyncPID', 'OnRevSyncPID(outputs, pwr, turnpct, p, i, d)',
        'OnRevSyncPID(outputs, pwr, turnpct, p, i, d)', 'Output'],
    ['PlayTone', 'PlayTone(frequency, duration)',
        '<b>PlayTone (<span foreground="brown">frequency</span>,' +
        ' <span foreground="brown">duration</span>)</b>\n\n' +
        'Play a single tone of the specified frequency and duration.\n' +
        'The frequency is in Hz. The duration is in 1000ths of a second.\n' +
        'The tone is played at the loudest sound level.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">frequency</span>  The desired tone frequency, in Hz.\n' +
        '  <span foreground="brown">duration</span>   The desired tone duration, in ms.\n' + 
        '<b>Example:</b>\n' +
        '  PlayTone(440, 500);     // Play Tone A for one half second', 'Sound'], 
    ['PlayTones', 'PlayTones(tones)',
        '<b>PlayTones (<span foreground="brown">tones[]</span>)</b>\n\n' +
        'Play a series of tones contained in the tones array. Each element\n' +
        'in the array is an instance of the Tone  structure, containing a \n' +
        'frequency and a duration.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">tones[]</span>    The array of tones to play.\n' +
        '<b>Example:</b>\n' +
        '  Tone sweepUp[] = {\n' +
        '  TONE_C4, MS_50, \n' +
        '  TONE_E4, MS_50, \n' +
        '  TONE_G4, MS_50,\n' +
        '  TONE_C5, MS_50, \n' +
        '  TONE_E5, MS_50, \n' +
        '  TONE_G5, MS_50, \n' +
        '  TONE_C6, MS_200\n' +
        '};\n' +
        'task main(){\n' +
        '  PlayTones(sweepUp);\n' +
        '  Wait(SEC_1);\n' +
        '}', 'Sound'],
    ['PlayToneEx', 'PlayToneEx(frequency, duration, volume, loop)',
        'PlayToneEx(frequency, duration, volume, loop)\n\n', 'Sound'],
    ['PlayFile', 'PlayFile(filename)',
        '<b>PlayFile (<span foreground="brown">filename</span> )</b>\n\n' +
        'Play the specified file. The sound file can either be\n' +
        'an RSO file or it can be an NXT melody (RMD) file containing\n' +
        'frequency and duration values.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">filename</span>    The name of the sound or melody file to play.\n' +
        '<b>Example:</b>\n' +
        '  PlayFile("startup.rso");', 'Sound'],
    ['PlayFileEx', 'PlayFileEx(filename, volume, loop)',
        '<b>PlayFileEx(filename, volume, loop)</b>\n\n' +
        '<b>Example:</b>\n' +
        '  PlayFileEx("startup.rso", 3, true);', 'Sound'],
    ['PointOut', 'PointOut(x, y)',
        '<b>PointOut (<span foreground="brown">x</span>, ' +
        '<span foreground="brown">y</span>, ' +
        '<span foreground="brown">options</span> = DRAW_OPT_NORMAL)</b>\n\n' +
        'This function lets you draw a point on the screen at x, y.\n' +
        'Optionally specify drawing options. If this argument is not\n' +
        'specified it defaults to DRAW_OPT_NORMAL.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">x</span>        The x value for the point.\n' +
        '  <span foreground="brown">y</span>        The y value for the point.\n' +
        '  <span foreground="brown">options</span>  The optional drawing options.\n' +
        '           <b>Warning:</b> These options require the\n' +
        '           enhanced NBC/NXC firmware\n\n' +
        '<b>Example:</b>\n' +
        '  PointOut(40, 40);', 'Display'], 
    ['Precedes', 'Precedes(tasks)',
        '<b>Precedes (' +
        '<span foreground="brown">task1</span>, ' +
        '<span foreground="brown">task2</span>, ' +
        '..., <span foreground="brown">taskN</span>)</b>\n\n' +
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
        '<b>Example:</b>\n' +
        '  Precedes(moving, drawing, playing);', 'Command'],
    ['Random', 'Random()',
        '<b>Random (<span foreground="brown">n = 0</span>)</b>\n\n' +
        'Generate random number. The returned value will range\n' +
        'between 0 and n (exclusive).\n\n' + 
        '<b>Parameters</b>\n  <span foreground="brown">n</span> The maximum unsigned value desired (optional).\n' +
        '<b>Example:</b>\n' +
        '  int x = Random(100); // unsigned int between 0..99\n' +
        '  int x = Random(); // signed int between -32767..32767', 'C API'], 
    ['RectOut', 'RectOut(x, y, width, height)',
        '<b>RectOut (<span foreground="brown">x</span>,' +
        ' <span foreground="brown">y</span>, ' +
        '<span foreground="brown">width</span>, ' +
        '<span foreground="brown">height</span>, ' +
        '<span foreground="brown">options</span>' +
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
        '           enhanced NBC/NXC firmware\n\n' +
        '<b>Example:</b>\n' +
        '  RectOut(40, 40, 30, 10);', 'Display'],
    ['Release', 'Release(m)', '<b>Release (mutex <span foreground="brown">m</span>)</b>\n\n' +
        'Release the specified mutex variable. Use this to relinquish\n' +
        'a mutex so that it can be acquired by another task. Release\n' +
        'should always be called after a matching call to Acquire and\n' +
        'as soon as possible after a shared resource is no longer needed.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">m</span>  The mutex to release.\n' +
        '<b>Example:</b>\n' +
        '  Acquire(motorMutex); // make sure we have exclusive access\n' +
        '  // use the motors\n' +
        '  Release(motorMutex); // release mutex for other tasks', 'Command'], 
    ['RenameFile', 'RenameFile(oldname, newname)',
        'RenameFile(oldname, newname)', 'Loader'], 
    ['ResetScreen', 'ResetScreen()',
        '<b>ResetScreen ()</b>\n\n'+
        'Reset LCD screen. This function lets you restore\n' +
        'the standard NXT running program screen.\n\n' +
        '<b>Example:</b>\n' +
        '  ResetScreen();', 'Display'], 
    ['ResetSensor', 'ResetSensor(port)',
        '<b>ResetSensor (<span foreground="brown">port</span>)</b>\n\n' +
        'Reset the sensor port. Sets the invalid data flag on the specified\n' +
        'port and waits for it to become valid again. After changing the type\n' +
        'or the mode of a sensor port you must call this function to give the\n' +
        'firmware time to reconfigure the sensor port.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>     The port to reset.\n' +
        '<b>Example:</b>\n' +
        '  ResetSensor(S1);', 'Input'], 
    ['ResetRotationCount', 'ResetRotationCount(outputs)',
        '<b>ResetRotationCount (' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'Reset the program-relative position counter for the specified outputs.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>    Desired output ports.\n' +
        '<b>Example:</b>\n' +
        '  ResetRotationCount(OUT_AB);', 'Output'], 
    ['ResetTachoCount', 'ResetTachoCount(outputs)',
        '<b>ResetTachoCount (' +
        '<span foreground="brown">outputs</span>)</b>\n\n' +
        'Reset the tachometer count and tachometer limit goal for the\n' +
        'specified outputs.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>    Desired output ports.\n' +
        '<b>Example:</b>\n' +
        '  ResetTachoCount(OUT_AB);', 'Output'], 
    ['ResetAllTachoCounts', 'ResetAllTachoCounts(outputs)',
        'ResetAllTachoCounts(outputs)\n\n' +
        '<b>Example:</b>\n' +
        '  ResetAllTachoCounts(OUT_AB);', 'Output'],
    ['RotateMotor', 'RotateMotor(outputs, pwr, angle)',
        '<b>RotateMotor (' +
        '<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">pwr</span>, ' +
        '<span foreground="brown">angle</span>)</b>\n\n' +
        'Rotate motor. Run the specified outputs forward for the specified number of degrees.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
        '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
        '  <span foreground="brown">angle</span>    Angle limit, in degree. Can be negative to reverse direction.\n' +
        '<b>Example:</b>\n  RotateMotor(OUT_A, 75, 45);  // forward 45 degrees\n' +
        '  RotateMotor(OUT_A, -75, 45); // reverse 45 degrees', 'Output'], 
    ['RotateMotorEx', 'RotateMotorEx(outputs, pwr, angle, turnpct, sync, stop)',
        '<b>RotateMotorEx (<span foreground="brown">outputs</span>, ' +
        '<span foreground="brown">pwr</span>, ' +
        '<span foreground="brown">angle</span>, ' +
        '<span foreground="brown">turnpct</span>, ' +
        '<span foreground="brown">sync</span>, ' +
        '<span foreground="brown">stop</span>)</b>\n\n' +
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
        '<b>Example:</b>:\n' +
        '  RotateMotorEx(OUT_AB, 75, 360, 50, true, true);', 'Output'], 
    ['RotateMotorPID', 'RotateMotorPID(outputs, pwr, angle, p, i, d)',
        'RotateMotorPID(outputs, pwr, angle, p, i, d)\n\n' +
        '<b>Example:</b>:\n' +
        '  RotateMotorPID(OUT_A, 75, 45, 20, 40, 100);', 'Output'],
    ['RotateMotorExPID', 'RotateMotorExPID(outputs, pwr, angle, turnpct, sync, stop, p, i, d)',
        'RotateMotorExPID(outputs, pwr, angle, turnpct, sync, stop, p, i, d)', 'Output'], 
    ['ReadLn', 'ReadLn(handle, value)',
        'ReadLn(handle, value)\n\n' +
        '<b>Example:</b>:\n' +
        '  result = ReadLn(handle, value);', 'Loader'], 
    ['ReadLnString', 'ReadLnString(handle, output)',
        'ReadLnString(handle, output)', 'Loader'], 
    ['ReceiveRemoteNumber', 'ReceiveRemoteNumber(queue, clear, val)',
        '<b>ReceiveRemoteNumber (' +
        '<span foreground="brown">queue</span>, ' +
        '<span foreground="brown">clear</span>, ' +
        '<span foreground="brown">val</span>)</b>\n\n' +
        'Read a numeric value from a mailbox and optionally remove it.\n' 
        'If the local mailbox is empty and this NXT is the master then\n' +
        'it attempts to poll one of its slave NXTs for a message from\n' +
        'the response mailbox that corresponds to the specified local\n' +
        'mailbox number.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">queue</span>    The mailbox number.\n' +
        '  <span foreground="brown">clear</span>    A flag indicating whether to remove the message from\n' +
        '           the mailbox after it has been read.\n' +
        '  <span foreground="brown">val</span>      The numeric value that is read from the mailbox.\n' +
        '<b>Returns</b>\n' +
        '  A char value indicating whether the function call succeeded or not.\n' +
        '<b>Example:</b>\n' +
        '  x = ReceiveRemoteNumber(queue, true, val);', 'Communication'], 
    ['ReceiveRemoteString', 'ReceiveRemoteString(queue, clear, str)',
        '<b>ReceiveRemoteString (' +
        '<span foreground="brown">queue</span>, ' +
        '<span foreground="brown">clear</span>, ' +
        '<span foreground="brown">str</span>)</b>\n\n' +
        'Read a string value from a mailbox and optionally remove it.\n' 
        'If the local mailbox is empty and this NXT is the master then\n' +
        'it attempts to poll one of its slave NXTs for a message from\n' +
        'the response mailbox that corresponds to the specified local\n' +
        'mailbox number.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">queue</span>    The mailbox number.\n' +
        '  <span foreground="brown">clear</span>    A flag indicating whether to remove the message from\n' +
        '           the mailbox after it has been read.\n' +
        '  <span foreground="brown">str</span>      The string value that is read from the mailbox.\n' +
        '<b>Returns</b>\n' +
        '  A char value indicating whether the function call succeeded or not.\n' +
        '<b>Example:</b>\n' +
        '  x = ReceiveRemoteString(queue, true, strval);', 'Communication'], 
    ['Sensor', 'Sensor(port)',
        '<b>Sensor (<span foreground="brown">port</span>)</b>\n\n' +
        'Return the processed sensor reading for a sensor on the specified port.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>  The sensor port.\n' +
        '<b>Returns</b>\n' +
        '  The sensor´s scaled value.\n' + 
        '<b>Example:</b>\n  x = Sensor(IN_1); // read sensor 1', 'Input'], 
    ['SensorUS', 'SensorUS(port)',
        '<b>SensorUS (<span foreground="brown">port</span> )</b>\n\n' +
        'Read ultrasonic sensor value. Return the ultrasonic sensor distance value.\n' +
        'Since an ultrasonic sensor is an I2C digital sensor its value cannot be\n' +
        'read using the standard Sensor(n) value. The port must be configured as\n' +
        'a Lowspeed port before using this function.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>  The port to which the ultrasonic sensor is attached.\n' +
        '<b>Returns</b>\n' +
        '  The ultrasonic sensor distance value (0..255)\n' +
        '<b>Example:</b>\n' +
        '  SetSensorLowspeed(IN_4);\n  x = SensorUS(IN_4); // read sensor 4', 'Input'], 
    ['SetSensorTouch', 'SetSensorTouch(port)',
        '<b>SetSensorTouch (' +
        '<span foreground="brown">port</span>)</b>\n\n' +
        'Configure a touch sensor on the specified Input port.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>  The Input port to configure.\n' +
        '<b>Example:</b>\n  SetSensorTouch(IN_1);', 'Input'], 
    ['SetSensorLight', 'SetSensorLight(port)',
        '<b>SetSensorLight (' +
        '<span foreground="brown">port</span>, ' +
        '<span foreground="brown">bActive</span> = true)</b>\n\n' +
        'Configure the sensor on the specified port as an NXT light sensor.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>     The port to configure.\n' +
        '  <span foreground="brown">bActive</span>' +
        '  A boolean flag indicating whether to configure the port\n' +
        '           as an active or inactive light sensor. The default\n' +
        '           value for this optional parameter is true.\n' +
        '<b>Example:</b>\n  SetSensorLight(IN_1);', 'Input'], 
    ['SetSensorSound', 'SetSensorSound(port)',
        '<b>SetSensorSound (' +
        '<span foreground="brown">port</span>, ' +
        '<span foreground="brown">bdBScaling</span> = true)</b>\n\n' +
        'Configure the sensor on the specified port as a sound sensor.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>        The port to configure.\n' +
        '  <span foreground="brown">bdBScaling</span>' +
        '  A boolean flag indicating whether to configure the\n' +
        '              port as a sound sensor with dB or dBA scaling.\n' +
        '              The default value for this optional parameter is\n' +
        '              true, meaning dB scaling.\n' +
        '<b>Example:</b>\n  SetSensorSound(IN_1);', 'Input'],
    ['SetSensorLowspeed', 'SetSensorLowspeed(port)',
        '<b>SetSensorLowspeed (' +
        '<span foreground="brown">port</span>, ' +
        '<span foreground="brown">bIsPowered</span> = true)</b>\n\n' +
        'Configure an digital I2C sensor on the specified port for either\n' +
        'powered (9 volt) or unpowered devices.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>         The port to configure.\n' +
        '  <span foreground="brown">bIsPowered</span>   A boolean flag indicating whether to configure\n' +
        '               the port for powered or unpowered I2C devices.\n' +
        '               Default value is true.\n' +
        '<b>Example:</b>\n  SetSensorLowspeed(IN_1);', 'Input'],
    ['SetSensor', 'SetSensor(port, config)',
        '<b>SetSensor (' +
        '<span foreground="brown">port</span>, ' +
        '<span foreground="brown">config</span>)</b>\n\n' +
        'Set the type and mode of the given sensor to the specified\n' +
        'configuration, which must be a special constant containing\n' +
        'both type and mode information.\n\n' +
        '<b>See Also</b>\n' +
        '  SetSensorType(), SetSensorMode(), and ResetSensor()\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>    The port to configure.\n' +
        '  <span foreground="brown">config</span>  The configuration constant containing both the type\n' +
        '          and mode: SENSOR_TOUCH, SENSOR_LIGHT, SENSOR_SOUND...\n' +
        '<b>Example:</b>\n' +
        '  SetSensor(IN_1, SENSOR_TOUCH);', 'Input'], 
    ['SetSensorColorFull', 'SetSensorColorFull(port)',
        '<b>SetSensorColorFull (' +
        '<span foreground="brown">port</span>)</b>\n\n' +
        'Configure an NXT 2.0 full color sensor on the specified\n' +
        'port in full color mode.\n\n' +
        '<b><span foreground="red">Warning</span></b>\n'
        '  This function requires an NXT 2.0 compatible firmware.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>        The port to configure.\n' +
        '<b>Example:</b>\n  SetSensorColorFull(IN_1);', 'Input'], 
    ['SetSensorColorBlue', 'SetSensorColorBlue(port)',
        '<b>SetSensorColorBlue (' +
        '<span foreground="brown">port</span>)</b>\n\n' +
        'Configure an NXT 2.0 full color sensor on the specified\n' +
        'port in blue light mode.\n\n' +
        '<b><span foreground="red">Warning</span></b>\n' +
        '  This function requires an NXT 2.0 compatible firmware.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>    The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorColorBlue(IN_1);', 'Input'], 
    ['SetSensorColorGreen', 'SetSensorColorGreen(port)',
        '<b>SetSensorColorGreen (' +
        '<span foreground="brown">port</span>)</b>\n\n' +
        'Configure an NXT 2.0 full color sensor on the specified\n' +
        'port in green light mode.\n\n' +
        '<b><span foreground="red">Warning</span></b>\n' +
        '  This function requires an NXT 2.0 compatible firmware.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>    The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorColorGreen(IN_1);', 'Input'],
    ['SetSensorColorRed', 'SetSensorColorRed(port)',
        '<b>SetSensorColorRed (' +
        '<span foreground="brown">port</span>)</b>\n\n' +
        'Configure an NXT 2.0 full color sensor on the specified\n' +
        'port in red light mode.\n\n' +
        '<b><span foreground="red">Warning</span></b>\n' +
        '  This function requires an NXT 2.0 compatible firmware.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>    The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorColorRed(IN_1);', 'Input'], 
    ['SetSensorColorNone', 'SetSensorColorNone(port)',
        '<b>SetSensorColorNone (' +
        '<span foreground="brown">port</span>)</b>\n\n' +
        'Configure an NXT 2.0 full color sensor on the specified\n' +
        'port in no light mode.\n\n' +
        '<b><span foreground="red">Warning</span></b>\n' +
        '  This function requires an NXT 2.0 compatible firmware.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>    The port to configure.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorColorNone(IN_1);', 'Input'], 
    ['SetSensorMode', 'SetSensorMode(port, mode)',
        '<b>SetSensorMode (' +
        '<span foreground="brown">port</span>, ' +
        '<span foreground="brown">mode</span>)</b>\n\n' +
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
        '<b>Example:</b>\n' +
        '  SetSensorMode(IN_1, SENSOR_MODE_RAW); // raw mode', 'Input'], 
    ['SetSensorType', 'SetSensorType(port, type)',
        '<b>SetSensorType (' +
        '<span foreground="brown">port</span>, ' +
        '<span foreground="brown">type</span>)</b>\n\n'+
        'Set a sensor\'s type, which must be one of the predefined sensor\n' +
        'type constants. After changing the type or the mode of a sensor port\n' +
        'you must call ResetSensor to give the firmware time to reconfigure\n' +
        'the sensor port.\n\n' +
        '<b>See Also</b>\n' +
        '  SetSensorMode(), SetSensor()\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">port</span>    The port to configure.\n' +
        '  <span foreground="brown">type</span>    The desired sensor type.\n' +
        '<b>Example:</b>\n' +
        '  SetSensorType(S1, SENSOR_TYPE_TOUCH);', 'Input'], 
    ['SendRemoteNumber', 'SendRemoteNumber(conn, queue, val)',
        '<b>SendRemoteNumber (' +
        '<span foreground="brown">conn</span>, ' +
        '<span foreground="brown">queue</span>, ' +
        '<span foreground="brown">val</span>)</b>\n\n' +
        'Send a numeric value on the specified connection to the specified\n' +
        'remote mailbox number. Use RemoteConnectionIdle to determine when\n' +
        'this write request is completed.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">conn</span>     The connection slot (0..4). Connections 0 through 3 are\n' +
        '           for bluetooth connections. Connection 4 refers to the RS485\n' +
        '           hi-speed port.\m' +
        '  <span foreground="brown">queue</span>    The mailbox number.\n' +
        '  <span foreground="brown">val</span>      The numeric value to send.\n' +
        '<b>Returns</b>\n' +
        '  A char value indicating whether the function call succeeded or not.\n' +
        '<b>Example:</b>\n' +
        '  x = SendRemoteNumber(1, MAILBOX1, 123);', 'Communication'], 
    ['SendRemoteString', 'SendRemoteString(conn, queue, str)',
        '<b>SendRemoteString (' +
        '<span foreground="brown">conn</span>, ' +
        '<span foreground="brown">queue</span>, ' +
        '<span foreground="brown">str</span>)</b>\n\n' +
        'Send a string value on the specified connection to the specified\n' +
        'remote mailbox number. Use RemoteConnectionIdle to determine when\n' +
        'this write request is completed.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">conn</span>     The connection slot (0..4). Connections 0 through 3 are\n' +
        '           for bluetooth connections. Connection 4 refers to the RS485\n' +
        '           hi-speed port.\m' +
        '  <span foreground="brown">queue</span>    The mailbox number.\n' +
        '  <span foreground="brown">str</span>      The string value to send.\n' +
        '<b>Returns</b>\n' +
        '  A char value indicating whether the function call succeeded or not.\n' +
        '<b>Example:</b>\n' +
        '  x = SendRemoteString(1, MAILBOX1, "hello world");', 'Communication'], 
    ['SendResponseNumber', 'SendResponseNumber(queue, val)',
        '<b>SendResponseNumber (' +
        '<span foreground="brown">queue</span>, ' +
        '<span foreground="brown">val</span>)</b>\n\n' +
        'Write a numeric value to a response mailbox (the mailbox number + 10).\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">queue</span>    The mailbox number. This function shifts the specified\n' +
        '           value into the range of response mailbox numbers by adding 10.\n' +
        '  <span foreground="brown">val</span>      The numeric value to write.\n' +
        '<b>Returns</b>\n' +
        '  A char value indicating whether the function call succeeded or not.\n' +
        '<b>Example:</b>\n' +
        '  x = SendResponseNumber(MAILBOX1, 123);', 'Communication'], 
    ['SendResponseString', 'SendResponseString(queue, str)',
        '<b>SendResponseString (' +
        '<span foreground="brown">queue</span>, ' +
        '<span foreground="brown">str</span>)</b>\n\n' +
        'Write a string value to a response mailbox (the mailbox number + 10).\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">queue</span>    The mailbox number. This function shifts the specified\n' +
        '           value into the range of response mailbox numbers by adding 10.\n' +
        '  <span foreground="brown">str</span>      The string value to write.\n' +
        '<b>Returns</b>\n' +
        '  A char value indicating whether the function call succeeded or not.\n' +
        '<b>Example:</b>\n' +
        '  x = SendResponseString(MAILBOX1, "hello world");', 'Communication'],
    ['StartTask', 'StartTask(task)',
        '<b>StartTask (' +
        '<span foreground="brown">task</span>)</b>\n\n' +
        'Start the specified task.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">task</span>   The task to start.\n' +
        '<b>Example:</b>\n' +
        '  StartTask(sound); // start the sound task', 'Command'],
    ['StrCat', 'StrCat(str1, str2, strN)',
        '<b>StrCat (' +
        '<span foreground="brown">str1</span>, ' +
        '<span foreground="brown">str2</span>, ' +
        '<span foreground="brown">strN</span>)</b>\n\n' +
        'Return a string which is the result of concatenating all of the\n' +
        'string arguments together. This function accepts any number of\n' +
        'parameters which may be string variables, constants, or expressions.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">str1</span>   The first string.\n' +
        '  <span foreground="brown">str2</span>   The second string.\n' +
        '  <span foreground="brown">strN</span>   The Nth string.\n' +
        '<b>Returns</b>\n' +
        '  The concatenated string.\n' +
        '<b>Example:</b>\n' +
        '  str1 = "Put";\n'+
        '  str2 = "me";\n' +
        '  str3 = "together";\n' +
        '  TextOut(0, LCD_LINE1, StrCat(str1, str2, str3));', 'C API'], 
    ['StrLen', 'StrLen(str)',
        '<b>StrLen (' +
        '<span foreground="brown">str</span>)</b>\n\n' +
        'Return the length of the specified string. The input string\n' +
        'parameter may be a variable, constant, or expression.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">str</span>   A string.\n' +
        '<b>Returns</b>\n' +
        '  The length of the string.\n' +
        '<b>Example:</b>\n' +
        '  string msg = "hi there";\n' +
        '  byte x = StrLen(msg); // return the length of msg', 'C API'], 
    ['StrToNum', 'StrToNum(str)',
        '<b>StrToNum (<span foreground="brown">str</span>)</b>\n\n' +
        'Return the numeric value specified by the string passed to the\n' +
        'function. If the content of the string is not a numeric value\n' +
        'then this function returns zero. The input string parameter may\n' +
        'be a variable, constant, or expression.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">str</span>   A string.\n' +
        '<b>Returns</b>\n' +
        '  A number.\n' +
        '<b>Example:</b>\n' +
        '  x = StrToNum(str);', 'C API'],
    ['TextOut', 'TextOut(x, y, str)',
        '<b>TextOut (' +
        '<span foreground="brown">x</span>, ' +
        '<span foreground="brown">y</span>, ' +
        '<span foreground="brown">str</span>)</b>\n\n' +
        'Draw a text value on the screen at the specified x and y location.\n' +
        'The y value must be a multiple of 8.\n\n' +
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
        '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
        '  <span foreground="brown">str</span>    The text to output to the LCD screen.\n' +
        '<b>Example:</b>\n' +
        '  TextOut(0, <span foreground="green">LCD_LINE1</span>, "Hello World!");', 'Display'],
    ['Off', 'Off(outputs)',
        '<b>Off (<span foreground="brown">outputs</span>)</b>\n\n' +
        'Turn motors off. Turn the specified outputs off (with braking).\n\n' + 
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">outputs</span>  Desired output ports.\n' +
        '<b>Example:</b>\n' +
        '  Off(OUT_A); // turn off output A', 'Output'], 
    ['OpenFileRead', 'OpenFileRead(fname, fsize, handle)',
        'OpenFileRead(fname, fsize, handle)\n\n' +
        '<b>Example:</b>\n' +
        '  result = OpenFileRead("data.txt", fsize, handle);', 'Loader'],
    ['Wait', 'Wait(ms)', '<b>Wait (<span foreground="brown">ms</span>)</b>\n\n' +
        'Make a task sleep for specified amount of time.\n\n' + 
        '<b>Parameters</b>\n' +
        '  <span foreground="brown">ms</span> The number of milliseconds to sleep.\n' +
        '<b>Example:</b>\n' +
        '  Wait(1000);', 'Command'], 
    ['WriteBytes', 'WriteBytes(handle, buf, cnt)',
        'WriteBytes(handle, buf, cnt)', 'Loader'], 
    ['WriteLn', 'WriteLn(handle, value)',
        'WriteLn(handle, value)', 'Loader'], 
    ['WriteLnString', 'WriteLnString(handle, str, cnt)',
        'WriteLnString(handle, str, cnt)', 'Loader']
]

nxc_consts = [
    ['BTNEXIT','BTNEXIT'],
    ['BTNRIGHT', 'BTNRIGHT'],
    ['BTNLEFT', 'BTNLEFT'],
    ['BTNCENTER', 'BTNCENTER'],
    ['BTN1', 'BTN1'],
    ['BTN2', 'BTN2'],
    ['BTN3', 'BTN3'],
    ['BTN4', 'BTN4'],
    ['DISPLAY_WIDTH', 'DISPLAY_WIDTH'],
    ['DISPLAY_HEIGHT', 'DISPLAY_HEIGHT'],
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
    ['SOUND_UP', 'SOUND_UP']
]

