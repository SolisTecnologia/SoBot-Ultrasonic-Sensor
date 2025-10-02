#!/usr/bin/python3
"""
Solis Robot - SoBot

Ultrasonic_Sensor.py: In this example, Robot Solis moves in a fenced space around side walls and possible
obstacles when detected by its ultrasonic distance sensors at pre-configured distances.

Created By   : Vinicius M. Kawakami and Rodrigo L. de Carvalho
Version      : 1.1

Company: Solis Tecnologia
"""

from time import sleep
import serial
from check_sonar import *
import sys
import signal

# Function to handle script termination signal
def handle_signal(signum, frame):
    usb.write(b"MT0 ME0")   # Disable motors
    usb.write(b"LT E0")     # Turn off Led Tap
    sys.exit(0)             # End the script

# Function registration for handling "SIGTERM" and "SIGINT" signal
signal.signal(signal.SIGTERM, handle_signal)
signal.signal(signal.SIGINT, handle_signal)


sonar_sensor = [0,0,0,0,0,0,0,0]
flag_enable = 0
flag_mv_fw = 0
count_mv_bk = 0
count_mv_lf = 0
count_mv_rd = 0

# Set serial port
usb = serial.Serial('/dev/ttyACM0', 57600, timeout=0, dsrdtr=False)
usb.flush()         # Waits data configuration

usb.write(b"LT E1 RD0 GR50 BL0")    # Turn on led tape in green
usb.write(b"MT0 MC AT100 DT100 V2") # Parameter settings for continuous mode
usb.write(b"MT0 ME1")               # Enables wheel motors on mode continuous
sleep(1)

while(flag_enable == 0):
    sonar_sensor = sonar_value()
    print(sonar_sensor)
    
    # Check front sensors
    if((sonar_sensor[LEFT_FRONT] == 0) and (sonar_sensor[FRONT] == 0) and (sonar_sensor[RIGHT_FRONT] == 0)):
    
        if(flag_mv_fw == 0):
            flag_fw = 1
            usb.write(b"LT E1 RD0 GR50 BL0")
            usb.write(b"MT0 MF")        # Moving to forward
            print("Moving to forward")
    
    # Check the front sensor only
    elif(sonar_sensor[FRONT] == 1):
        
        # Check the right side sensor is smaller
        if((sonar_sensor[RIGHT] == 1) and (sonar_sensor[LEFT] == 0)):
        
            # Check the right rear side sensor
            if(sonar_sensor[RIGHT_BACK] == 0):
                usb.write(b"LT E1 RD0 GR0 BL50")
                usb.write(b"MT0 ML")        # Moviment to left
                print("Moviment to left")

            # Check the left rear side sensor
            elif(sonar_sensor[LEFT_BACK] == 0):
                count_mv_rd = 0

                while(count_mv_rd < 12):
                    count_mv_rd+= 1
                    sonar_sensor = sonar_value()
                    if(sonar_sensor[LEFT_BACK] == 0):
                        usb.write(b"LT E1 RD0 GR30 BL10")
                        usb.write(b"MT0 MR")        # Moviment to right
                        print("Moviment to right")
                        
                    else:
                        count_mv_rd = 12

                count_mv_bk = 0
                usb.write(b"LT E1 RD50 GR0 BL0")

                while(count_mv_bk < 6):
                    count_mv_bk += 1
                    sonar_sensor = sonar_value()

                    # Checks the rear sensors
                    if((sonar_sensor[RIGHT_BACK] == 0) and (sonar_sensor[BACK] == 0) and (sonar_sensor[LEFT_BACK] == 0)):
                        usb.write(b"MT0 MB")        # Moving to back
                        print("Moviment to back")
                    else:
                        count_mv_bk = 6

            # If the two rear sides sensors are locked
            else:
                usb.write(b"MT0 MP")        # Moviment pause
                print("Pausing...")
                flag_enable = 1

        # Check the left side sensor is smaller
        elif((sonar_sensor[RIGHT] == 0) and (sonar_sensor[LEFT] == 1)):

            # Check the left rear side sensor
            if(sonar_sensor[LEFT_BACK] == 0):
                usb.write(b"LT E1 RD0 GR30 BL10")
                usb.write(b"MT0 MR")        # Moviment to right
                print("Moviment to right")

            # Check the right rear side sensor
            elif(sonar_sensor[RIGHT_BACK] == 0):
                count_mv_lf = 0

                while(count_mv_lf < 12):
                    count_mv_lf+= 1
                    sonar_sensor = sonar_value()
                    if(sonar_sensor[RIGHT_BACK] == 0):
                        usb.write(b"LT E1 RD0 GR0 BL50")
                        usb.write(b"MT0 ML")        # Moviment to left
                    else:
                        count_mv_lf = 12

                count_mv_bk = 0
                usb.write(b"LT E1 RD50 GR0 BL0")

                while(count_mv_bk < 6):
                    count_mv_bk += 1
                    sonar_sensor = sonar_value()

                    # Checks the rear sensors
                    if((sonar_sensor[RIGHT_BACK] == 0) and (sonar_sensor[BACK] == 0) and (sonar_sensor[LEFT_BACK] == 0)):
                        usb.write(b"MT0 MB")        # Moving to back
                    else:
                        count_mv_bk = 6

            # If the two rear sides sensors are locked
            else:
                usb.write(b"MT0 MP")        # Moviment pause
                flag_enable = 1
    
    # Check the left front sensor only
    elif(sonar_sensor[LEFT_FRONT] == 1):
 
        # Check the left rear side sensor
        if(sonar_sensor[LEFT_BACK] == 0):
            usb.write(b"LT E1 RD0 GR30 BL10")
            usb.write(b"MT0 MR")        # Moviment to right
     
        # Check the right rear side sensor
        elif(sonar_sensor[RIGHT_BACK] == 0):
            count_mv_lf = 0
            while(count_mv_lf < 12):
                count_mv_lf+= 1
                sonar_sensor = sonar_value()
                if(sonar_sensor[RIGHT_BACK] == 0):
                    usb.write(b"LT E1 RD0 GR0 BL50")
                    usb.write(b"MT0 ML")    # Moviment to left
                else:
                    count_mv_lf = 12
            count_mv_bk = 0
            usb.write(b"LT E1 RD50 GR0 BL0")
            while(count_mv_bk < 6):
                count_mv_bk += 1
                sonar_sensor = sonar_value()
      
                # Checks the rear sensors
                if((sonar_sensor[RIGHT_BACK] == 0) and (sonar_sensor[BACK] == 0) and (sonar_sensor[LEFT_BACK] == 0)):
                    usb.write(b"MT0 MB")        # Moving to back
                else:
                    count_mv_bk = 6

        # If the two rear sides sensors are locked
        else:
            usb.write(b"MT0 MP")        # Moviment pause
            flag_enable = 1
    
    # Check the right front sensor only
    elif(sonar_sensor[RIGHT_FRONT] == 1):

        # Check the right rear side sensor
        if(sonar_sensor[RIGHT_BACK] == 0):
            usb.write(b"LT E1 RD0 GR0 BL50")
            usb.write(b"MT0 ML")        # Moviment to left
            print("Moviment to left")
        
        # Check the left rear side sensor
        elif(sonar_sensor[LEFT_BACK] == 0):
            count_mv_rd = 0
 
            while(count_mv_rd < 12):
                count_mv_rd+= 1
                sonar_sensor = sonar_value()
                if(sonar_sensor[LEFT_BACK] == 0):
                    usb.write(b"LT E1 RD0 GR30 BL10")
                    usb.write(b"MT0 MR")        # Moviment to right
                    print("Moviment to right")

                else:
                    count_mv_rd = 12
 
            count_mv_bk = 0
            usb.write(b"LT E1 RD50 GR0 BL0")
 
            while(count_mv_bk < 6):
                count_mv_bk += 1
                sonar_sensor = sonar_value()
 
                # Checks the rear sensors
                if((sonar_sensor[RIGHT_BACK] == 0) and (sonar_sensor[BACK] == 0) and (sonar_sensor[LEFT_BACK] == 0)):
                    usb.write(b"MT0 MB")        # Moving to back
                    print("Moviment to back")

                else:
                    count_mv_bk = 6
 
        # If the two rear sides sensors are locked
        else:
            usb.write(b"MT0 MP")        # Moviment pause
            print("Pausing...")
            flag_enable = 1


usb.write(b"MT0 MP")        # Moviment pause
usb.write(b"LT E1 RD50 GR30 BL0")
sleep(4)

usb.write(b"LT E0")
usb.write(b"MT0 ME0")       # Disables wheel motors on mode continuous
