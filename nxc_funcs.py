# -*- coding: utf-8 -*-
nxc_funcs = [
            ['Acquire', 'Acquire()', ''], 
            ['ArrayInit', 'ArrayInit()', '' ], 
            ['ArrayLen', 'ArrayLen()', ''],
            ['BluetoothStatus', 'BluetoothStatus()', ''],
            ['ButtonCount', 'ButtonCount()', ''], 
            ['ButtonLongPressCount', 'ButtonLongPressCount()', ''], 
            ['ButtonPressCount', 'ButtonPressCount()', ''], 
            ['ButtonPressed', 'ButtonPressed()', ''], 
            ['ButtonState', 'ButtonState()', ''],
            ['ClearScreen', 'ClearScreen()', ''], 
            ['ClearSensor', 'ClearSensor()', ''], 
            ['CircleOut', 'CircleOut()', ''], 
            ['Coast', 'Coast()', '<small><b>void Coast (byte <span foreground="brown">outputs</span>)</b>\n\n' +
                'Coast motors. Turn off the specified outputs, making them coast to a stop.\n\n<b>Parameters</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n<b>Examples:</b>\n' +
                '  Coast(OUT_A); // coast output A</small>'], 
            ['CurrentTick', 'CurrentTick()', ''], 
            ['CreateFile', 'CreateFile()', ''], 
            ['CloseFile', 'CloseFile()', ''],
            ['DeleteFile', 'DeleteFile()', ''],
            ['Float', 'Float()', '<small><b>void Float (byte <span foreground="brown">outputs</span>)</b>\n\n' +
                'Float motors. Make outputs float. Float is an alias for Coast.\n\n<b>Parameters</b>\n' +
                '  <span foreground="brown">outputs</span>  Desired output ports.\n<b>Examples:</b>\n' +
                '  Float(OUT_A); // float output A</small>'],
            ['GraphicOut', 'GraphicOut()', ''],
            ['LineOut', 'LineOut()', ''],
            ['MotorRotationCount', 'MotorRotationCount()', ''],
            ['NumOut', 'NumOut(.,.,.)', '<small><b>char NumOut (int <span foreground="brown">x</span>,' +
                ' int <span foreground="brown">y</span>, ' +
                'variant <span foreground="brown">value</span>)</b>\n\nDraw a numeric value on the screen at the ' +
                'specified x and y location.\nThe y value must be a multiple of 8.\n\n<b>Parameters</b>\n' +
                '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
                '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
                '  <span foreground="brown">value</span>  The value to output to the LCD screen. Any numeric type is supported.\n' +
                '<b>Examples:</b>\n  NumOut(0, LCD_LINE1, x);</small>'], 
            ['NumToStr', 'NumToStr()', ''],
            ['OnFwd', 'OnFwd(.,.)', '<small><b>void OnFwd (byte <span foreground="brown">outputs</span>,' +
                ' char <span foreground="brown">pwr</span>)</b>\n\n' +
                'Run motors forward. Set outputs to forward direction and turn them on.\n\n' +
                '<b>Parameters:</b>\n  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
                '<b>Example:</b>\n  OnFwd(OUT_A, 75);</small>'], 
            ['OnRev', 'OnRev(.,.)', '<small><b>void OnRev (byte <span foreground="brown">outputs</span>,' +
                ' char <span foreground="brown">pwr</span>)</b>\n\n' +
                'Run motors backward. Set outputs to reverse direction and turn them on.\n\n' +
                '<b>Parameters:</b>\n  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
                '<b>Example:</b>\n  OnRev(OUT_A, 75);</small>'], 
            ['OnFwdReg', 'OnFwdReg()', ''], 
            ['OnFwdRegPID', 'OnFwdRegPID()', ''], 
            ['OnFwdSync', 'OnFwdSync()', ''], 
            ['OnFwdSyncPID', 'OnFwdSyncPID()', ''],
            ['OnRevReg', 'OnRevReg()', ''], 
            ['OnRevRegPID', 'OnRevRegPID()', ''], 
            ['OnRevSync', 'OnRevSync()', ''], 
            ['OnRevSyncPID', 'OnRevSyncPID()', ''],
            ['PlayFileEx', 'PlayFileEx()', ''],
            ['PlayTone', 'PlayTone(.,.)', '<small><b>char PlayTone (unsigned int <span foreground="brown">frequency</span>,' +
                ' unsigned int <span foreground="brown">duration</span>)</b>\n\n' +
                'Play a single tone of the specified frequency and duration.\nThe frequency is in Hz.' +
                ' The duration is in 1000ths of a second.\nThe tone is played at the loudest sound level.\n\n' +
                '<b>Parameters</b>\n  <span foreground="brown">frequency</span>  The desired tone frequency, in Hz.\n' +
                '  <span foreground="brown">duration</span>   The desired tone duration, in ms.\n' + 
                '<b>Examples:</b>\n  PlayTone(440, 500);     // Play Tone A for one half second</small>'], 
	        ['PlayToneEx', 'PlayToneEx()', ''], 
	        ['PointOut', 'PointOut()', ''], 
	        ['Precedes', 'Precedes()', ''],
	        ['Random', 'Random()', '<small><b>int Random (unsigned int <span foreground="brown">n = 0</span>)</b>\n\n' +
                'Generate random number. The returned value will range between 0 and n (exclusive).\n\n' + 
                '<b>Parameters</b>\n  <span foreground="brown">n</span> The maximum unsigned value desired (optional).\n' +
                '<b>Examples:</b>\n  int x = Random(100); // unsigned int between 0..99\n' +
                '  int x = Random(); // signed int between -32767..32767</small>'], 
	        ['ReadLn', 'ReadLn()', ''], 
	        ['ReadLnString', 'ReadLnString()', ''], 
	        ['ReceiveRemoteNumber', 'ReceiveRemoteNumber()', ''], 
	        ['ReceiveRemoteString', 'ReceiveRemoteString()', ''], 
	        ['RectOut', 'RectOut()', ''],
	        ['Release', 'Release()', ''], 
	        ['RenameFile', 'RenameFile()', ''], 
	        ['ResetScreen', 'ResetScreen()', ''], 
	        ['ResetSensor', 'ResetSensor()', ''], 
	        ['ResetRotationCount', 'ResetRotationCount()', ''], 
	        ['ResetTachoCount', 'ResetTachoCount()', ''], 
	        ['ResetAllTachoCounts', 'ResetAllTachoCounts()', ''],
	        ['RotateMotor', 'RotateMotor(.,.,.)', '<small><b>void RotateMotor (byte <span foreground="brown">outputs</span>,' +
	            ' char <span foreground="brown">pwr</span>, long <span foreground="brown">angle</span>)</b>\n\n' +
		        'Rotate motor. Run the specified outputs forward for the specified number of degrees.\n\n' +
		        '<b>Parameters</b>\n  <span foreground="brown">outputs</span>  Desired output ports.\n' +
		        '  <span foreground="brown">pwr</span>      Output power, 0 to 100. Can be negative to reverse direction.\n' +
		        '  <span foreground="brown">angle</span>    Angle limit, in degree. Can be negative to reverse direction.\n' +
                '<b>Example:</b>\n  RotateMotor(OUT_A, 75, 45); // forward 45 degrees\n' +
		        '  RotateMotor(OUT_A, -75, 45); // reverse 45 degrees</small>'], 
		    ['RotateMotorEx', 'RotateMotorEx()', ''], 
	        ['RotateMotorExPID', 'RotateMotorExPID()', ''], 
	        ['RotateMotorPID', 'RotateMotorPID()', ''],
	        ['Sensor', 'Sensor()', '<small><b>unsigned int Sensor (const byte &amp; <span foreground="brown">port</span>)</b>\n' +
	            '\nReturn the processed sensor reading for a sensor on the specified port.\n\n<b>Parameters</b>\n' +
	            '  <span foreground="brown">port</span>  The sensor port.\n<b>Returns</b>\n  The sensor´s scaled value.\n' + 
	            '<b>Examples:</b>\n  x = Sensor(IN_1); // read sensor 1</small>'], 
	        ['SensorUS', 'SensorUS()', ''], 
	        ['SetSensorTouch', 'SetSensorTouch(.)', '<small><b>void SetSensorTouch (const byte &amp;' +
	            ' <span foreground="brown">port</span>)</b>\n\n' +
	            'Configure a touch sensor on the specified Input port.\n\n' +
	            '<b>Parameters</b>\n  <span foreground="brown">port</span>  The Input port to configure.\n' +
	            '<b>Examples:</b>\n  SetSensorTouch(IN_1);</small>'], 
	        ['SetSensorLight', 'SetSensorLight()', '<small><b>void SetSensorLight (const byte &amp; ' +
	            '<span foreground="brown">port</span>, bool <span foreground="brown">bActive</span> = true)</b>\n\n' +
                'Configure the sensor on the specified port as an NXT light sensor.\n\n<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>     The port to configure.\n  <span foreground="brown">bActive</span>' +
                '  A boolean flag indicating whether to configure the port\n           as an active or inactive light sensor.' +
                ' The default\n           value for this optional parameter is true.\n' +
                '<b>Examples:</b>\n  SetSensorLight(IN_1);</small>'], 
	        ['SetSensorSound', 'SetSensorSound()', '<small><b>void SetSensorSound (const byte &amp; ' +
	            '<span foreground="brown">port</span>, bool <span foreground="brown">bdBScaling</span> = true)</b>\n\n' +
                'Configure the sensor on the specified port as a sound sensor.\n\n<b>Parameters</b>\n' +
                '  <span foreground="brown">port</span>        The port to configure.\n  <span foreground="brown">bdBScaling</span>' +
                '  A boolean flag indicating whether to configure the\n              port as a sound sensor with dB or dBA scaling.\n' +
                '              The default value for this optional parameter is\n              true, meaning dB scaling.\n' +
                '<b>Examples:</b>\n  SetSensorSound(IN_1);</small>'],
	        ['SetSensorLowspeed', 'SetSensorLowspeed()', ''],
	        ['SetSensor', 'SetSensor()', ''], 
	        ['SetSensorColorFull', 'SetSensorColorFull()', ''], 
	        ['SetSensorColorBlue', 'SetSensorColorBlue()', ''], 
	        ['SetSensorColorGreen', 'SetSensorColorGreen()', ''],
	        ['SetSensorColorRed', 'SetSensorColorRed()', ''], 
	        ['SetSensorColorNone', 'SetSensorColorNone()', ''], 
	        ['SetSensorMode', 'SetSensorMode()', ''], 
	        ['SetSensorType', 'SetSensorType()', ''], 
	        ['SendRemoteNumber', 'SendRemoteNumber()', ''], 
	        ['SendRemoteString', 'SendRemoteString()', ''], 
	        ['SendResponseNumber', 'SendResponseNumber()', ''], 
	        ['SendResponseString', 'SendResponseString()', ''],
	        ['StrCat', 'StrCat()', ''], 
	        ['StrLen', 'StrLen()', ''], 
	        ['StrToNum', 'StrToNum()', ''],
            ['TextOut', 'TextOut()', '<small><b>char TextOut (int <span foreground="brown">x</span>,' +
                ' int <span foreground="brown">y</span>, ' +
                'string <span foreground="brown">str</span>)</b>\n\nDraw a text value on the screen at the ' +
                'specified x and y location.\nThe y value must be a multiple of 8.\n\n<b>Parameters</b>\n' +
                '  <span foreground="brown">x</span>      The x value for the start of the number output.\n' +
                '  <span foreground="brown">y</span>      The text line number for the number output.\n' +
                '  <span foreground="brown">str</span>  The text to output to the LCD screen.\n' +
                '<b>Examples:</b>\n  TextOut(0, LCD_LINE1, "Hello World!");</small>'],
            ['Off', 'Off(.)', '<small><b>void Off (byte <span foreground="brown">outputs</span>)</b>\n\n' +
                'Turn motors off. Turn the specified outputs off (with braking).\n\n' + 
                '<b>Parameters</b>\n  <span foreground="brown">outputs</span>  Desired output ports.\n' +
                '<b>Examples:</b>\n  Off(OUT_A); // turn off output A</small>'], 
            ['OpenFileRead', 'OpenFileRead()', ''],
            ['Wait', 'Wait(.)', '<small><b>void Wait (unsigned long <span foreground="brown">ms</span>)</b>\n\n' +
                'Make a task sleep for specified amount of time.\n\n' + 
                '<b>Parameters</b>\n  <span foreground="brown">ms</span> The number of milliseconds to sleep.\n' +
                '<b>Example:</b>\n  Wait(1000);</small>'], 
            ['WriteBytes', 'WriteBytes()', ''], 
            ['WriteLn', 'WriteLn()', ''], 
            ['WriteLnString', 'WriteLnString()', '']
            ]
