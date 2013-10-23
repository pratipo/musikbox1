#!/usr/bin/env python
 
from __future__ import print_function
import time
import subprocess as sp
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#GPIO.setup(enable_pin, GPIO.OUT)
dir_pin = 23
step_pin = 24
#enable_pin = 25

GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)

GPIO.output(enable_pin, 1)
GPIO.output(dir_pin, 0)

def spin(t):
	for r in range(0,t):
		for i in range(0, 200*8):
			GPIO.output(step_pin, 0)
			GPIO.output(step_pin, 1)
			time.sleep(0.005)

def turndown():
	sp.call("sync")
	sp.call(["shutdown", "-h", "now"])

#read music file length

while True:
	print ("playing!")
	p = sp.Popen(["ogg123","deathly.ogg"], stdout=sp.PIPE)	
    print("spining")
    spin(8);

    l = random.randint(3, 7)
	time.sleep(l);
