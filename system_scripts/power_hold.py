#!/usr/bin/env python3
#Briefly emulate a HELD push of the ATX power momentary switch via a PC817 Optoisolator on GPIO24

import gpiozero
import sys
from time import sleep

power_sw = gpiozero.DigitalOutputDevice("GPIO24")

if(len(sys.argv) < 2):
    sys.exit('ERROR: Provide a hold time as command line argument')

hold_time =float(sys.argv[1])
print('Holding power switch for {hold_time} seconds...'.format(hold_time=hold_time))

if( not isinstance(hold_time, int) and not isinstance(hold_time, float)):
    sys.exit('ERROR: Bad formatting for hold_time')

if(hold_time <= 0):
    sys.exit('ERROR: hold_time must be greater than 0')

power_sw.on()
sleep(hold_time)
power_sw.off()
