#!/usr/bin/python3
"""
Solis Robot - SoBot

check_sonar.py: Library with function to check the distance of the ultrasonic sensors and compare with pre-established values.

Created By   : Vinicius M. Kawakami and Rodrigo L. de Carvalho
Version      : 1.1

Company: Solis Tecnologia
"""

from time import sleep
import serial

LEFT_FRONT = 0
FRONT = 1
RIGHT_FRONT = 2
RIGHT = 3
RIGHT_BACK= 4
BACK = 5
LEFT_BACK = 6
LEFT = 7

# Set serial port
usb = serial.Serial('/dev/ttyACM0', 57600, timeout=0, dsrdtr=False)
usb.flush()     # Waits data configuration

def sonar_value():
    value = [0,0,0,0,0,0,0,0]
   
    usb.write(b"SS0")            # Send command to read sonar sensor
    sleep(0.5)                   # Wait to return datas
    data_sonar = usb.readline()  # Read data
    
    sensor = [0]*8 # Array data
    
    #Split sensor data
    split_data = data_sonar.split()
    for i in range(8):
        try:
            distance = int(split_data[(i*2)+1])
            sensor[i] = distance
            if distance < 120:
                sensor[i] = 0
            if distance > 3800:
                sensor[i] = 3800

        except:
            sensor[i] = 0

    #Finished Array 
    print("Data Sensor: ", sensor)

    # Check front sensor if it is <= 50cm
    if(sensor[FRONT] <= 500):
        value[FRONT] = 1
    else:
        value[FRONT] = 0
        
    # Check left front sensor if it is <= 45cm
    if(sensor[LEFT_FRONT] <= 450):
        value[LEFT_FRONT] = 1
    else:
        value[LEFT_FRONT] = 0
    
    # Check right front sensor if it is <= 45cm
    if(sensor[RIGHT_FRONT] <= 450):
        value[RIGHT_FRONT] = 1
    else:
        value[RIGHT_FRONT] = 0
        
    # Check which side is farthest from obstacle
    if(sensor[RIGHT] > sensor[LEFT]):
        value[RIGHT] = 0
        value[LEFT] = 1
    else:
        value[RIGHT] = 1
        value[LEFT] = 0

    # Check right back sensor if it is <= 20cm
    if(sensor[RIGHT_BACK] <= 200):
        value[RIGHT_BACK] = 1
    else:
        value[RIGHT_BACK] = 0

    # Check back sensor if it is <= 20cm
    if(sensor[BACK] <= 200):
        value[BACK] = 1
    else:
        value[BACK] = 0

    # Check left back sensor if it is <= 20cm
    if(sensor[LEFT_BACK]<= 200):
        value[LEFT_BACK] = 1
    else:
        value[LEFT_BACK] = 0

    return value