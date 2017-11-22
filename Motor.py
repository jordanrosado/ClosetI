#!/usr/bin/env python
import sys
import RPi.GPIO as gpio 
import time
import os

class piMotor(object):

    def __init__(self):
	gpio.setmode(gpio.BCM)
	gpio.setup(23, gpio.OUT)
	gpio.setup(24, gpio.OUT)
	gpio.setup(25, gpio.OUT)
	
    
    def foto(self):
	gpio.output(23, True)
	gpio.output(25, False) # ENABLE
	StepCounter = 0
	while StepCounter < 50:
    		gpio.output(24, True)
    		time.sleep(0.03)
    		gpio.output(24, False)
    		StepCounter += 1
    		time.sleep(0.007)
	time.sleep(0.1)
	gpio.output(25, True)
	gpio.cleanup()
	gpio.setmode(gpio.BCM)
	gpio.setup(25, gpio.OUT)
	gpio.setup(24,gpio.OUT)
	gpio.setup(24, False)
	gpio.output(25, gpio.HIGH)
	return 1	
        
  
