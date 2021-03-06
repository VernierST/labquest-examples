"""
Control the Pulse Output line (this is line 4) of a DCU connected to dig1.

The LabQuest and LabQuest Mini have the capability of performing pulse width
modulation (pwm) output from line D4 of a DCU connected to dig1 (dig2 does not have 
this capability). The variables to control the output include the frequency(Hz)
and duty cycle(%). 

Note that you cannot change the frequency once you have started the output, but
you can modify the duty cycle (as shown in this example).
"""

from time import sleep

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

frequency_Hz = 10    # set the frequency at the beginning and do not change

lq.open()
lq.select_sensors(dig1='dcu_pwm')
lq.start()   # start() does not have a period argument

print("duty cycle = 90 %")
duty_cycle = 90
lq.dcu_pwm_dig1(frequency_Hz, duty_cycle)
sleep(4)

print("duty cycle = 10%")
duty_cycle = 10
lq.dcu_pwm_dig1(frequency_Hz, duty_cycle)
sleep(4)
    
lq.stop()
lq.close()



