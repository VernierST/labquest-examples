"""
Collect data from a LabQuest motion detector connected to DIG 1.

A dictionary is used in the lq.select_sensors() argument to configure a
motion detector connected to DIG 1. Distance measurements are returned in 
centimeters.
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
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