#!/usr/bin/env python
 
from __future__ import print_function
import time
import subprocess as sp
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

def turndown():
	subprocess.call(["shutdown", "-h", "now"])

while True:
	print ("playing!")
	p = sp.Popen(["mpg321","bubbling_water_1.mp3"], stdout=sp.PIPE)	
	print ("end sound " + p.communicate()[0])
                
	for i in range(5):
		print(i)
		time.sleep(1);
