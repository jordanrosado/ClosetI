#!/usr/bin/python

import sys
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(25, gpio.OUT)

try: 
    steps = int(float(sys.argv[1]))
except:
    steps = 0

Slot = 10*(steps-1)
StepCounter = 0
Stp = 0
gpio.output(23, True)
#gpio.output(23, False)
gpio.output(25, False) # ENABLE
time.sleep(0.5)

while Stp < Slot:
    while StepCounter < 1:
    	#turning the gpio on and off tells the easy driver to take one step
    	gpio.output(24, True)
    	time.sleep(0.0005)
    	gpio.output(24, False)
    	StepCounter += 1
    	#Wait before taking the next step...this controls rotation speed
    StepCounter = 0
    Stp += 1
    time.sleep(0.1)

time.sleep(1)
gpio.output(25, True)
gpio.setup(24, False)
gpio.output(25, gpio.HIGH)
gpio.cleanup()
gpio.setmode(gpio.BCM)
#gpio.setup(25, gpio.OUT)
#gpio.setup(24,gpio.OUT)