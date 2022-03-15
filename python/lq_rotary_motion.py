"""
Collect data from a LabQuest rotary motion sensor connected to DIG 1.

A dictionary is used in the lq.select_sensors() argument to configure a
rotary motion sensor connected to DIG 1. Note that this can also 
be configured in the high resolution mode, also known as X4 mode, using
the dictionar value of 'rotary_motion_high_res'. This provides a 0.25 
degree resolution and a limited maximum measurable rotational velocity.

This example also shows how to stop and restart measurements with the 
counter at the same location. The lq.start() function provides that 
functionality using the reset_dig_counter argument, as shown:

lq.start(250, reset_dig_counter=False)
"""

from labquest import LabQuest
import logging

# uncomment to show debug messages from the labquest module
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()
lq.open()
lq.select_sensors({'dig1':'rotary_motion'}) 
#lq.select_sensors({'dig1':'rotary_motion_high_res'}) 

lq.start(250)    # period in milliseconds

column_headers = lq.enabled_sensor_info()  
print(column_headers)  

for x in range(20):
    measurements = lq.read()
    if measurements == None: 
        break 
    print(measurements)

lq.stop()
print('\n')
lq.start(250, reset_dig_counter=False)

for x in range(20):
    measurements = lq.read()
    if measurements == None: 
        break 
    print(measurements)

lq.stop()
lq.close()