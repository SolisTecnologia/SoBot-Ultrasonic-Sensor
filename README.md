# Solis Robot - SoBot
![](https://github.com/SolisTecnologia/SoBot-Ultrasonic-Sensor/blob/master/png/SoBotSingle.png)
# Introduction

AMR (autonomous mobile robotics) platform equipped with a camera system, ultrasonic and photoelectric sensors, works with a high rate of precision and repeatability of its movements, as it uses stepper motors in its movement and navigation, the SoBot also can be termed as a research and development interface, as it facilitates the practical experimentation of algorithms from the simplest to the most complex level.

This product was developed 100% by Solis Tecnologia, and has a lot of technology employing cutting-edge concepts, such as:

The motors can be controlled simultaneously or individually.
The user can select different accessories to implement to the robot.
Several programming languages can be used to connect via API.

# Components

* Main structure in aluminum
* Removable fairing with magnetic attachment points
* Robot Control Driver
* Raspberry Pi 4B board <img align="center" height="30" width="40" src="https://github.com/devicons/devicon/blob/master/icons/raspberrypi/raspberrypi-original.svg">
* 8x Ultrasonic Distance Sensor
* 2x NEMA-23 Stepper Motors
* 2x 12V/5A battery

# Programming Example

In this example, Robot Solis moves in a fenced space around side walls and possible obstacles when detected by its ultrasonic distance sensors at pre-configured distances.

The three front sensors are used to detect obstacles and the side and rear sensors help in maneuvers indicating the best direction when a frontal obstacle is detected.

### Programming Language

* Python  <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">

## Ultrasonic Distance Sensor - [Ultrasonic_Sensor.py](https://github.com/SolisTecnologia/SoBot-Ultrasonic-Sensor/blob/master/Ultrasonic_Sensor.py)

### Required Libraries

~~~python
from time import sleep
import serial
import check_sonar
~~~

The ''time'' library is needed to generate time delays and the ''serial'' library for serial/usb Raspberry connection with the robot controller driver.
The ''check-sonar'' library has a function that sends the reading command of the ultrasonic sensors and checks the distance of each sensor with a pre-established range from the return of the command.

### Code Description

The commands used in this example to control SoBot are continuous movement commands, as follows:

~~~python
usb.write(b"MT0 MC AT100 DT100 V2") # Parameter settings for continuous mode
usb.write(b"MT0 ME1")               # Enable continuous movement
usb.write(b"MT0 ME0")               # Disable continuous movement
usb.write(b"MT0 ML")                # Move left
usb.write(b"MT0 MR")                # Move right
usb.write(b"MT0 MB")                # Move backward
usb.write(b"MT0 MF")                # Move Forward
usb.write(b"MT0 MP")                # Pause movement
~~~

Commands are also used to control the lighting of the LED tape, as follows:

~~~python
usb.write(b"LT E1 RD0 GR50 BL0")    # Turn on led tape in green
~~~

### Flowchart

![]()

## Ultrasonic Distance Sensor - [check_sonar.py](https://github.com/SolisTecnologia/SoBot-Ultrasonic-Sensor/blob/master/check_sonar.py)

### Required Libraries

~~~python
from time import sleep
import serial
~~~

The ''time'' library is needed to generate time delays and the ''serial'' library for serial/usb Raspberry connection with the robot controller driver.

### Code Description

Commands are also used to read the line sensors, as follows:
~~~python
usb.write(b"SS0")                    # Send command to read ultrasonic sensors
~~~

The command return for reading the ultrasonic sensors are stored in the Array variable **data_sonar**.

~~~python
data_sonar = usb.readline()          # Read data
~~~

For more information about the commands used, check the Robot Commands Reference Guide.

### Flowchart

![]()

# Reference Link
[SolisTecnologia website](https://solistecnologia.com/produtos/robotsingle)

# Please Contact Us
If you have any problem when using our robot after checking this tutorial, please contact us.

### Phone:
+55 1143040786

### Technical support email: 
contato@solistecnologia.com.br

![](https://github.com/SolisTecnologia/SoBot-Ultrasonic-Sensor/blob/master/png/logo.png)