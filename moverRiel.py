#!/usr/bin/python

import sys
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(25, gpio.OUT)

StepCounter = 0
gpio.output(23, False)
gpio.output(25, False) # ENABLE

while StepCounter < 50:
    #turning the gpio on and off tells the easy driver to take one step
    gpio.output(24, True)
    time.sleep(0.033)
    gpio.output(24, False)
    StepCounter += 1
    #Wait before taking the next step...this controls rotation speed
    time.sleep(0.007)

time.sleep(5)
gpio.output(25, True)
gpio.cleanup()
gpio.setmode(gpio.BCM)
gpio.setup(25, gpio.OUT)
gpio.setup(24,gpio.OUT)
gpio.setup(24, False)
gpio.output(25, gpio.HIGH)