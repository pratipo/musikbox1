#!/usr/bin/env python
 
from __future__ import print_function
import time
import subprocess as sp
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)

#enable_pin = 25
dir_pin = 23
step_pin = 24

#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)

#GPIO.output(enable_pin, 1)
GPIO.output(dir_pin, 0)

def shutdown():
	sp.call(["shutdown", "-h", "now"])

def turn():
	for i in range(0, 200*8):
		GPIO.output(step_pin, 0)
		GPIO.output(step_pin, 1)
		time.sleep(0.02)
 
while True:
	turn()
	time.sleep(3)
