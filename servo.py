import sys
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(10,gpio.OUT)
gpio.setup(11,gpio.OUT)
p = gpio.PWM(10,50)
p.start(7.5)
p.ChangeDutyCycle(50)
time.sleep(0.5)
p.ChangeDutyCycle(7.5)
time.sleep(0.5)
gpio.output(11,gpio.HIGH)

