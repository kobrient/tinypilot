#!/usr/bin/env python3
#Briefly emulate a push of the ATX reset momentary switch via a PC817 Optoisolator on GPIO23

import gpiozero
from time import sleep

reset_sw = gpiozero.DigitalOutputDevice("GPIO23")

reset_sw.on()
sleep(0.4)
reset_sw.off()

