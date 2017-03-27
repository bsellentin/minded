 /*
 * EV3 Sensor API
 *
 * Copyright (C) 2014 Carsten Zeiffert
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/
 *
 * ----------------------------------------------------------------------------
 *
 * \author Simón Rodriguez Perez(Hochschule Aschaffenburg)
 * \date 2015-02-28
 * \version 2
 * \note Correct readout for Touch-, Sonar- and Lightsensor
 *
 * ----------------------------------------------------------------------------
 *
 * \author Simón Rodriguez Perez
 * \date 2016-04-20
 * \version 3
 * \note Correct readout for Gyroscop and Infrared Sensor
 *
 * ----------------------------------------------------------------------------
 *
 * \author Bernd Sellentin
 * \date 2017
 * \version 3.1
 * \note Added NXT-Soundsensor 
 *
 */
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include "ev3sensor.h"
#include "uart.h"
#include "iic.h"
#include "analog.h"

#include <stdint.h>

/***********************************/
// see "LEGO mindstorms ev3 firmware developer kit.pdf" chap.5 Device type list
// define of Sensor setup
// TOUCH
#define TOUCH_TYPE 16
#define TOUCH_PRESS_MODE 0 	// Press

// Light
#define COL_TYPE 29
#define COL_REFLECT_MODE 0 	// Reflect
#define COL_AMBIENT_MODE 1 	// Ambient
#define COL_COLOR_MODE 2 	// Color

// Ultrasonic
#define US_TYPE 30
#define US_DIST_CM_MODE 0 	// Dist in cm
#define US_DIST_MM_MODE 0 	// Dist in mm
#define US_DIST_IN_MODE 1 	// Dist in inch

// Gyroskop
#define GYRO_TYPE 32
#define GYRO_ANG_MODE 0 	// angle
#define GYRO_RATE_MODE 1	// rate
#define GYRO_AR_MODE 3     // angle and rate

// Infrared
#define IR_TYPE 33
#define IR_PROX_MODE 0		// Proximity
#define IR_SEEK_MODE 1		// Seek
#define IR_REMOTE_MODE 2	// Remote Control

// IIC 
#define IIC_TYPE 100
#define IIC_BYTE_MODE 0

// NXT Temperture
#define NXT_TEMP_TYPE 6
#define NXT_TEMP_C_MODE 0	// Temperature in C
#define NXT_TEMP_F_MODE 1	// Temperature in F

// NXT Sensors
#define TYPE_NXT_TOUCH 1     //!< Device is NXT touch sensor
#define TYPE_NXT_LIGHT 2     //!< Device is NXT light sensor
#define TYPE_NXT_SOUND 3     //!< Device is NXT sound sensorPort
#define NXT_SOUND_DB_MODE 0  // Decibels
#define NXT_SOUND_DBA_MODE 1 // A-Weighted Decibels
#define TYPE_NXT_COLOR 4     //!< Device is NXT color sensor
#define TYPE_NXT_IIC 123     //!< Device is NXT IIC sensor

/***********************************/

int g_uartFile = 0;
int g_iicFile = 0;
int g_analogFile = 0;
UART* g_uartSensors = 0;
IIC* g_iicSensors = 0;
ANALOG* g_analogSensors = 0;        // struct ANALOG defined in analog.h 

// Mode of inputs
int sensor_setup_NAME[INPUTS];
int ir_sensor_channel[INPUTS];

/********************************************************************************************/
/**
* Initialisation of the Sensorfunctions
* modified by: Simón Rodriguez Perez
* 		 date: 2015-02-28
*
*/
int InitSensors()
{
    g_uartFile = open("/dev/lms_uart", O_RDWR | O_SYNC);
	g_iicFile =  open("/dev/lms_iic", O_RDWR | O_SYNC);
	g_analogFile = open("/dev/lms_analog", O_RDWR | O_SYNC);

    g_uartSensors = (UART*)mmap(0, sizeof(UART), PROT_READ | PROT_WRITE,
                                MAP_FILE | MAP_SHARED, g_uartFile, 0);
    g_iicSensors = (IIC*)mmap(0, sizeof(IIC), PROT_READ | PROT_WRITE,
                              MAP_FILE | MAP_SHARED, g_iicFile, 0);
	g_analogSensors = (ANALOG*)mmap(0, sizeof(ANALOG), PROT_READ | PROT_WRITE,
									MAP_FILE | MAP_SHARED, g_analogFile, 0);
	int i;
	for (i = 0; i < INPUTS; i++)
	{
		ir_sensor_channel[i] = 0;
	}

	if (g_uartFile && g_iicFile && g_analogFile &&
		g_uartSensors && g_iicSensors && g_analogSensors)
		return 0;
	return -1;
}

/*DATA8 getSensorConnectionType(int sensorPort)
{
	if (!g_analogSensors || sensorPort < 0 || sensorPort >= INPUTS)
		return 0;
	return g_analogSensors->InConn[sensorPort];
}*/

/********************************************************************************************/
/**
* Getting the Data from a Uartport
* modified by: Simón Rodriguez Perez
* 		 date: 2015-02-28
* 		 note: Readout of Uart-Port
*
*/
void* readUartSensor(int sensorPort)
{
	if (!g_uartSensors)
		return 0;
    return g_uartSensors->Raw[sensorPort][g_uartSensors->Actual[sensorPort]];
}

void* readIicSensor(int sensorPort)
{
	if (!g_iicSensors)
		return 0;
    UWORD currentSensorSlot = g_iicSensors->Actual[sensorPort];
    return g_iicSensors->Raw[sensorPort][currentSensorSlot];
}

void* readNewDumbSensor(int sensorPort)
{
	return (void*)&(g_analogSensors->InPin6[sensorPort]);
}

void* readOldDumbSensor(int sensorPort)
{
	return (void*)&(g_analogSensors->InPin1[sensorPort]);       // DATA16
}

void* readNxtColor(int sensorPort, DATA8 index)
{
	return 0; // Not supported
/*
	DATAF result = DATAF_NAN;
	cInputCalibrateColor(g_analogSensors->NxtCol[sensorPort], g_analogSensors->NxtCol[sensorPort].SensorRaw);

	switch (g_sensorMode[sensorPort])
	{
	case 2: return cInputCalculateColor(g_analogSensors->NxtCol[sensorPort]); //NXT-COL-COL
    case 1: return g_analogSensors->NxtCol[sensorPort].ADRaw[BLANK]; // NXT-COL-AMB
    case 0: return g_analogSensors->NxtCol[sensorPort].ADRaw[RED]; // NXT-COL-RED
    case 3: return g_analogSensors->NxtCol[sensorPort].ADRaw[GREEN]; // NXT-COL-GRN
    case 4: return g_analogSensors->NxtCol[sensorPort].ADRaw[BLUE]; // NXT-COL-BLU
    case 5: return g_analogSensors->NxtCol[sensorPort].SensorRaw[Index]; // NXT-COL-RAW
	}
	return result;
*/
}

/********************************************************************************************/
/**
* Get the Data from the Sensor
* modified by: Simón Rodriguez Perez
* 		 date: 2015-02-28
* 		 note: changed for Touch-, Sonar- and Lightsensor
*
*----------------------------------------------------------------------------------
*
* modified by: Simón Rodriguez Perez
* 		 date: 2016-04-21
* 		 note: readout for Gyro and Infrared Sensor
*
*/
void* ReadSensorData(int sensorPort)
{
	if (!g_analogSensors || sensorPort < 0 || sensorPort >= INPUTS)
		return 0;


	switch (sensor_setup_NAME[sensorPort])
	{
		case CONN_NONE: 
		case CONN_ERROR: 
		case NO_SEN: 
			return 0;
		// Touchsensor
		case TOUCH_PRESS:
			return readNewDumbSensor(sensorPort);
		// Lightsensor
		case COL_REFLECT: 
			return readUartSensor(sensorPort);
		case COL_AMBIENT: 
			return readUartSensor(sensorPort);
		case COL_COLOR: 
			return readUartSensor(sensorPort);
		// Ultrasonic
		case US_DIST_CM: 
			return readUartSensor(sensorPort);
		case US_DIST_MM: 
			return readUartSensor(sensorPort);
		case US_DIST_IN: 
			return readUartSensor(sensorPort);
		// Gyroskop
		case GYRO_ANG: 
			return readUartSensor(sensorPort);
		case GYRO_RATE: 
			return readUartSensor(sensorPort);
		// Infrared
		case IR_PROX:
		    return readUartSensor(sensorPort);
		case IR_SEEK:
		    return readUartSensor(sensorPort);
		case IR_REMOTE:
			return readUartSensor(sensorPort);
		// NXT
		case NXT_IR_SEEKER:
			return readIicSensor(sensorPort);
		case NXT_TEMP_C:
			return readIicSensor(sensorPort);
		case NXT_TEMP_F:
			return readIicSensor(sensorPort);
        case NXT_SOUND_DB:
            return readOldDumbSensor(sensorPort);
        case NXT_SOUND_DBA:
            return readOldDumbSensor(sensorPort);
		default: return 0;
	}

	return 0;
}

/********************************************************************************************/
/**
* Usercall for actual value of one Sensor
* modified by: Simón Rodriguez Perez
* 		 date: 2015-02-28
* 		 note: now working for Touch-, Sonar- and Lightsensor
*			   with calculation of the correct values
*
*----------------------------------------------------------------------------------
*
* modified by: Simón Rodriguez Perez
* 		 date: 2016-04-21
* 		 note: readout for Gyroscop and Infrared Sensor
* modified by: Bernd Sellentin
*        date: 2017-01
*        note: now with NXT-Soundsensor
*/
int ReadSensor(int sensorPort)
{
	uint64_t* data = ReadSensorData(sensorPort);
	int32_t help=0;
	if (!data)
		return -1;

	switch (sensor_setup_NAME[sensorPort])
	{
		case NO_SEN:
			return -1;
		// Touchsensor
		case TOUCH_PRESS:
			help = *((DATA16*)data);
			help = help/256;
			if (help==0)
				return 0;
			else if(help==0xD)
				return 1;
			else
				return -1;
		// Lightsensor
		case COL_REFLECT:
			return *((DATA16*)data)&0x00FF;
		case COL_AMBIENT:
			return *((DATA16*)data)&0x00FF;
		case COL_COLOR:
			return *((DATA16*)data)&0x000F;
		// Ultrasonic
		case US_DIST_CM:
			return (*((DATA16*)data)&0x0FFF)/10;
		case US_DIST_MM:
			return *((DATA16*)data)&0x0FFF;
		case US_DIST_IN:
			return *((DATA16*)data)&0x0FFF;
		// Gyroskop
		case GYRO_ANG:
		    help = *((DATA16*)data)&0xFFFF;         // 1111 1111 1111 1111
		    if(help & 0x8000)                       // 1000 0000 0000 0000
			{
				help = ((help&0x7FFF) - 0x7FFF);    // 0111 1111 1111 1111
			}
			return help;
		case GYRO_RATE:
			help = *(data)&0xFFFF;
			if(help & 0x8000)
			{
				help = ((help&0x7FFF) - 0x7FFF);
			}
			return help;
		// Infrared
		case IR_PROX:
			return *((DATA16*)data)&0x00FF;
		case IR_SEEK:
			help = (*(data) >> (16*ir_sensor_channel[sensorPort]))& 0xFF;
			if(help & 0x80)
			{
				help = ((help&0x7F) - 0x7F);
			}
			return help;
		case IR_REMOTE:
			help = *(data)&0xFFFFFFFF;
			help = (help >> (8*ir_sensor_channel[sensorPort]))& 0xFF;
			return help;
		// NXT
		case NXT_IR_SEEKER:
			return *((DATA16*)data)&0x000F;
		case NXT_TEMP_C:
			help = (*data>>4) & 0x0FFF;
			if(help & 0x800)
			{
				help = ((help&0x7FF) ^ 0x7FF) + 1;
				return (-1)*(((help>>4) & 0xFF)*10 + ((help & 0xF) * 10 / 15));
			}
			return ((help>>4) & 0xFF)*10 + ((help & 0xF) * 10 / 15);
		case NXT_TEMP_F:
			help = (*data>>4) & 0x0FFF;
			if(help & 0x800)
			{
				help = ((help&0x7FF) ^ 0x7FF) + 1;
				return (-1)*(((help>>4) & 0xFF)*10 + ((help & 0xF) * 10 / 15)) * 9/5 + 320;
			}
			return (((help>>4) & 0xFF)*10 + ((help & 0xF) * 10 / 15)) * 9/5 + 320;
		case NXT_SOUND_DB:
		    /* max raw value <= 4000 
		    *  silent = max, loud = min
		    *  return percent
		    */ 
		    help = *((DATA16*)data)&0x0FFF;
		    return (100 - (help * 100/4100));   // raw_max = 4200
		    //return help;
		case NXT_SOUND_DBA:
		    help = *((DATA16*)data)&0x0FFF;
		    return (100 - (help * 100/4100));
		default: break;
	}
	return *((DATA16*)data);
}

/********************************************************************************************/
/**
* Initialisation for one Sensor 
* modified by: Simón Rodriguez Perez
* 		 date: 2015-02-28
* 		 note: Sensors are working now, but only one sensor is working at once
*
*/
int SetSensorMode(int sensorPort, int name)
{
	static DEVCON devCon;

	if (!g_analogSensors || sensorPort < 0 || sensorPort >= INPUTS)
		return -1;

	sensor_setup_NAME[sensorPort] = name;
	// Setup of Input
	switch (name)
	{
		case NO_SEN:
			break;
		// EV3-Touchsensor
		case TOUCH_PRESS:
			devCon.Connection[sensorPort] 	= CONN_INPUT_DUMB;      // in ev3_constants.h
			devCon.Type[sensorPort] 		= TOUCH_TYPE;           // here on top
			devCon.Mode[sensorPort] 		= TOUCH_PRESS_MODE;     // here on top
			break;
		// EV3-Lightsensor
		case COL_REFLECT:
			devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= COL_TYPE;
			devCon.Mode[sensorPort] 		= COL_REFLECT_MODE;
			break;
		case COL_AMBIENT:
			devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= COL_TYPE;
			devCon.Mode[sensorPort] 		= COL_AMBIENT_MODE;
			break;
		case COL_COLOR:
			devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= COL_TYPE;
			devCon.Mode[sensorPort] 		= COL_COLOR_MODE;
			break;
		// EV3-Ultrasonic
		case US_DIST_CM:
			devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= US_TYPE;
			devCon.Mode[sensorPort] 		= US_DIST_CM_MODE;
			break;
		case US_DIST_MM:
			devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= US_TYPE;
			devCon.Mode[sensorPort] 		= US_DIST_MM_MODE;
			break;
	    // EV3-Gyroskop
		case GYRO_ANG:
			devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= GYRO_TYPE;
			devCon.Mode[sensorPort] 		= GYRO_ANG_MODE;
			break;
		case GYRO_RATE:
			devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= GYRO_TYPE;
			devCon.Mode[sensorPort] 		= GYRO_RATE_MODE;
			break;
		// EV3-Infrared
		case IR_PROX:
			devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= IR_TYPE;
			devCon.Mode[sensorPort] 		= IR_PROX_MODE;
			break;
		case IR_SEEK:
			devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= IR_TYPE;
			devCon.Mode[sensorPort] 		= IR_SEEK_MODE;
			break;
		case IR_REMOTE:
			devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= IR_TYPE;
			devCon.Mode[sensorPort] 		= IR_REMOTE_MODE;
			break;
		// NXT
		case NXT_IR_SEEKER:
			devCon.Connection[sensorPort] 	= CONN_NXT_IIC;
			devCon.Type[sensorPort] 		= IIC_TYPE;
			devCon.Mode[sensorPort] 		= IIC_BYTE_MODE;
			break;
		case NXT_TEMP_C:
			devCon.Connection[sensorPort] 	= CONN_NXT_IIC;
			devCon.Type[sensorPort] 		= NXT_TEMP_TYPE;
			devCon.Mode[sensorPort] 		= NXT_TEMP_C_MODE;
			break;
		case NXT_TEMP_F:
			devCon.Connection[sensorPort] 	= CONN_NXT_IIC;
			devCon.Type[sensorPort] 		= NXT_TEMP_TYPE;
			devCon.Mode[sensorPort] 		= NXT_TEMP_F_MODE;
			break;
		case NXT_SOUND_DB:
	        devCon.Connection[sensorPort] 	= CONN_NXT_DUMB;
			devCon.Type[sensorPort] 		= TYPE_NXT_SOUND;
			devCon.Mode[sensorPort] 		= NXT_SOUND_DB_MODE;
			break;
	    case NXT_SOUND_DBA:
	        devCon.Connection[sensorPort] 	= CONN_NXT_DUMB;
			devCon.Type[sensorPort] 		= TYPE_NXT_SOUND;
			devCon.Mode[sensorPort] 		= NXT_SOUND_DBA_MODE;
			break;
		default: return -1;
	}

	return 0;
}

/** Reset the angle of the gyrosensor to 0 by changing modes back and forth
 *
 */
int ResetGyro()
{   
    static DEVCON devCon;
    int sensorPort = 0;
    int mode = 0;
    DATA8 type = 0;
    int resulta;
    int resultb;
    
    sleep(1);
    
    for(sensorPort=0; sensorPort<4; sensorPort++)
    {
        // switch to other mode
        if(sensor_setup_NAME[sensorPort] == GYRO_RATE)      // 9
        {
            //return sensorPort;  //    works
            //type = *(g_uartSensors->Raw[sensorPort][g_uartSensors->TypeData[sensorPort][1].Type]); //works not: incompatible types in return
            // g_uartSensors->Raw[sensorPort][g_uartSensors->Actual[sensorPort]];
            
            mode = GYRO_RATE;
            devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= GYRO_TYPE;        // 32
			devCon.Mode[sensorPort] 		= GYRO_ANG_MODE;    // 3
			
            break;
        }
        else if(sensor_setup_NAME[sensorPort] == GYRO_ANG)    // 8
        {
            mode = GYRO_ANG;
            devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
			devCon.Type[sensorPort] 		= GYRO_TYPE;        // 32
			devCon.Mode[sensorPort] 		= GYRO_RATE_MODE;   // 3
			
			break;
        }
    }
    
    while(!resulta){
        resulta = ReadSensor(sensorPort);
    }
    
    sleep(1);
    
    switch (mode)       // switch to old mode
    {
        case GYRO_RATE:
            devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
	        devCon.Type[sensorPort] 		= GYRO_TYPE;
	        devCon.Mode[sensorPort] 		= GYRO_RATE_MODE;
	        
	        break;
        case GYRO_ANG:
            devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
	        devCon.Type[sensorPort] 		= GYRO_TYPE;
	        devCon.Mode[sensorPort] 		= GYRO_ANG_MODE;
	        
	        break;
	    default:
	        return -1;
    }
    
    while(!resultb){
        resultb = ReadSensor(sensorPort);
    }
    sleep(1);
    return sensorPort+1;
}

/********************************************************************************************/
/**
* Initialisation of all Sensors for working parallel 
* author: Simón Rodriguez Perez
* note: the function can only be called once at the beginning
*
*/
int SetAllSensorMode(int name_1, int name_2, int name_3, int name_4)
{
	static DEVCON devCon;
	int sensorPort = 0;
	
	int name[4] = {};

	name[0] = name_1;
	name[1] = name_2;
	name[2] = name_3;
	name[3] = name_4;

	if (!g_analogSensors)
	{
		return -1;
	}
	
	// Setup of Input
	for(sensorPort=0; sensorPort<4; sensorPort++)
	{
		sensor_setup_NAME[sensorPort] = name[sensorPort];
		switch (name[sensorPort])
		{
			case NO_SEN:
				break;
			// Touchsensor
			case TOUCH_PRESS:
				devCon.Connection[sensorPort] 	= CONN_INPUT_DUMB;
				devCon.Type[sensorPort] 		= TOUCH_TYPE;
				devCon.Mode[sensorPort] 		= TOUCH_PRESS_MODE;
				break;
			// Lightsensor
			case COL_REFLECT:
				devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
				devCon.Type[sensorPort] 		= COL_TYPE;
				devCon.Mode[sensorPort] 		= COL_REFLECT_MODE;
				break;
			case COL_AMBIENT:
				devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
				devCon.Type[sensorPort] 		= COL_TYPE;
				devCon.Mode[sensorPort] 		= COL_AMBIENT_MODE;
				break;
			case COL_COLOR:
				devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
				devCon.Type[sensorPort] 		= COL_TYPE;
				devCon.Mode[sensorPort] 		= COL_COLOR_MODE;
				break;
			// Ultrasonic
			case US_DIST_CM:
				devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
				devCon.Type[sensorPort] 		= US_TYPE;
				devCon.Mode[sensorPort] 		= US_DIST_CM_MODE;
				break;
			case US_DIST_MM:
				devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
				devCon.Type[sensorPort] 		= US_TYPE;
				devCon.Mode[sensorPort] 		= US_DIST_MM_MODE;
				break;
			case US_DIST_IN:
				devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
				devCon.Type[sensorPort] 		= US_TYPE;
				devCon.Mode[sensorPort] 		= US_DIST_IN_MODE;
				break;
			// Gyroskop
			case GYRO_ANG:
				devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
				devCon.Type[sensorPort] 		= GYRO_TYPE;
				devCon.Mode[sensorPort] 		= GYRO_ANG_MODE;
				break;
			case GYRO_RATE:
				devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
				devCon.Type[sensorPort] 		= GYRO_TYPE;
				devCon.Mode[sensorPort] 		= GYRO_RATE_MODE;
				break;
			// Infrared
			case IR_PROX:
				devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
				devCon.Type[sensorPort] 		= IR_TYPE;
				devCon.Mode[sensorPort] 		= IR_PROX_MODE;
				break;
			case IR_SEEK:
				devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
				devCon.Type[sensorPort] 		= IR_TYPE;
				devCon.Mode[sensorPort] 		= IR_SEEK_MODE;
				break;
			case IR_REMOTE:
				devCon.Connection[sensorPort] 	= CONN_INPUT_UART;
				devCon.Type[sensorPort] 		= IR_TYPE;
				devCon.Mode[sensorPort] 		= IR_REMOTE_MODE;
				break;
			// NXT
			case NXT_IR_SEEKER:
				devCon.Connection[sensorPort] 	= CONN_NXT_IIC;
				devCon.Type[sensorPort] 		= IIC_TYPE;
				devCon.Mode[sensorPort] 		= IIC_BYTE_MODE;
				break;
			case NXT_TEMP_C:
				devCon.Connection[sensorPort] 	= CONN_NXT_IIC;
				devCon.Type[sensorPort] 		= NXT_TEMP_TYPE;
				devCon.Mode[sensorPort] 		= NXT_TEMP_C_MODE;
				break;
			case NXT_TEMP_F:
				devCon.Connection[sensorPort] 	= CONN_NXT_IIC;
				devCon.Type[sensorPort] 		= NXT_TEMP_TYPE;
				devCon.Mode[sensorPort] 		= NXT_TEMP_F_MODE;
				break;
			default: return -1;
		}
	}
	// Set actual device mode
	ioctl(g_uartFile, UART_SET_CONN, &devCon);
	//ioctl(g_iicFile, IIC_SET_CONN, &devCon);
	return 0;
}


/********************************************************************************************/
/**
* Selection of the Beacon channel for IR Sensor
* author: Simón Rodriguez Perez
* note: channel can be modified while running
*
*/
int SetIRBeaconCH(int sensorPort, int channel)
{
	ir_sensor_channel[sensorPort] = channel;
	
	return 0;
}



