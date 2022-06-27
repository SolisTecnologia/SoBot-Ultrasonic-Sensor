#!/usr/bin/python3
"""
Solis Robot - SoBot

check_sonar.py: Library with function to check the distance of the ultrasonic sensors and compare with pre-established values.

Created By   : Vinicius M. Kawakami
Version      : 1.0

Company: Solis Tecnologia
"""

from time import sleep
import serial

data_sonar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

Zero = 48
Um = 49
Dois = 50
Tres = 51
Quatro = 52
Cinco = 53
Seis = 54
Sete = 55
Oito = 56
Nove = 57

# Set serial port
usb = serial.Serial('/dev/ttyACM0', 57600, timeout=0, dsrdtr=False)
usb.flush()     # Waits data configuration

def sonar_value():
    value = [0,0,0,0,0,0,0,0]
    usb.write(b"SS0")            # Send command to read sonar sensor
    sleep(0.5)                   # Wait to return datas
    data_sonar = usb.readline()  # Read data
    print(data_sonar)
    # Check front sensor if it is <= 50cm
    if((data_sonar[13] == Zero) and (((data_sonar[14] == Cinco) and (data_sonar[15] <= Zero)) or (data_sonar[14] <= Quatro))):
        value[1] = 1
    else:
        value[1] = 0
    # Check left front sensor if it is <= 45cm
    if((data_sonar[4] == Zero) and (((data_sonar[5] == Quatro) and (data_sonar[6] <= Cinco)) or (data_sonar[5] <= Tres))):
        value[0] = 1
    else:
        value[0] = 0
    # Check right front sensor if it is <= 45cm
    if((data_sonar[22] == Zero) and (((data_sonar[23] == Quatro) and (data_sonar[24] <= Cinco)) or (data_sonar[23] <= Tres))):
        value[2] = 1
    else:
        value[2] = 0
    # Check which side is farthest from obstacle
    if(data_sonar[31] == data_sonar[67]):
        if(data_sonar[32] == data_sonar[68]):
            if(data_sonar[33] == data_sonar[69]):
                # Check Right sensor is greater
                if(data_sonar[34] > data_sonar[70]):
                    value[3] = 0
                    value[7] = 1
                else:
                    value[3] = 1
                    value[7] = 0
            else:
                # Check Right sensor is greater
                if(data_sonar[33] > data_sonar[69]):
                    value[3] = 0
                    value[7] = 1
                else:
                    value[3] = 1
                    value[7] = 0
        else:
            # Check Right sensor is greater
            if(data_sonar[32] > data_sonar[68]):
                value[3] = 0
                value[7] = 1
            else:
                value[3] = 1
                value[7] = 0
    else:
        # Check Right sensor is greater
        if(data_sonar[31] > data_sonar[67]):
            value[3] = 0
            value[7] = 1
        else:
            value[3] = 1
            value[7] = 0
    # Check right back sensor if it is <= 15cm
    if((data_sonar[40] == Zero) and (((data_sonar[41] == Um) and (data_sonar[42] <= Cinco)) or (data_sonar[41] == Zero))):
        value[4] = 1
    else:
        value[4] = 0

    # Check back sensor if it is <= 15cm
    if((data_sonar[49] == Zero) and (((data_sonar[50] == Um) and (data_sonar[51] <= Cinco)) or (data_sonar[50] == Zero))):
        value[5] = 1
    else:
        value[5] = 0
    # Check left back sensor if it is <= 15cm
    if((data_sonar[58] == Zero) and (((data_sonar[59] == Um) and (data_sonar[60] <= Cinco)) or (data_sonar[59] == Zero))):
        value[6] = 1
    else:
        value[6] = 0

    return value