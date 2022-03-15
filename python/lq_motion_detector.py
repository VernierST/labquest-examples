"""
Collect data from a LabQuest motion detector connected to DIG 1.

A dictionary is used in the lq.select_sensors() argument to configure a
motion detector connected to DIG 1. Distance measurements are returned in 
centimeters.
"""

from labquest import LabQuest
import logging

# uncomment to show debug messages from the labquest module
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors({'dig1':'motion'}) 
lq.start(100)

column_headers = lq.enabled_sensor_info()  
print(column_headers)  

for x in range(10):
    measurements = lq.read()
    if measurements == None: 
        break 
    print(measurements)

lq.stop()
lq.close()