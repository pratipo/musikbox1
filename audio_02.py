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
	if ( GPIO.input(23) == False ):
		print "playing!"
		p = subprocess.Popen(["aplay","maderos.wav"], stdout=subprocess.PIPE)	
  		print p.communicate()[0]
                
    else:
		print(".", end="")
    sleep(0.1);
