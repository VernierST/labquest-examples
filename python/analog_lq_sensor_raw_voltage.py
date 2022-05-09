"""
Read the raw_voltage signal from ch1. 

Setting the select_sensor() argument to read raw voltage is useful for
collecting data from a non-Vernier analog sensor, or to get the uncalibrated
signal of a LabQuest sensor.

Note: The Vernier Breadboard Cable (order code: BB-BTA), provides an 
easy way to wire a custom sensor into a LabQuest device.
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors(ch1='raw_voltage')    # this reads the sensor's raw voltage - no calibration applied

lq.start(100)    # period in milliseconds. 

ch1_header = lq.enabled_sensor_info('ch1')
print(ch1_header)  

for x in range(10):
    ch1_measurement = lq.read('ch1')
    if ch1_measurement == None: 
        break 
    print(ch1_measurement)

lq.stop()
lq.close()