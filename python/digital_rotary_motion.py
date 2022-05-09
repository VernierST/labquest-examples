"""
Collect data from a LabQuest rotary motion sensor connected to dig1.

Note that this can also be configured in the high resolution mode, also known 
as X4 mode, using the argument of 'rotary_motion_high_res' in select_sensors(). 
This provides a 0.25 degree resolution.

This example also shows how to stop and restart dig1_measurement with the 
counter at the same location. The lq.start() function provides that 
functionality using the reset_dig_counter argument, as shown:

lq.start(250, reset_dig_counter=False)
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors(dig1='rotary_motion') 
#lq.select_sensors(dig1='rotary_motion_high_res')    # use this option for X4 mode

lq.start(250)    # period in milliseconds

dig1_header = lq.enabled_sensor_info('dig1')  
print(dig1_header)  

for x in range(20):
    dig1_measurement = lq.read('dig1')
    if dig1_measurement == None: 
        break 
    print(dig1_measurement)

lq.stop()
print('\n')
lq.start(250, reset_dig_counter=False)

for x in range(20):
    dig1_measurement = lq.read('dig1')
    if dig1_measurement == None: 
        break 
    print(dig1_measurement)

lq.stop()
lq.close()