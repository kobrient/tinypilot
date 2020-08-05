#!/usr/bin/env python3
#Briefly emulate a push of the ATX power momentary switch via a PC817 Optoisolator on GPIO24

import gpiozero
from time import sleep

power_sw = gpiozero.DigitalOutputDevice("GPIO24")

power_sw.on()
sleep(0.4)
power_sw.off()
