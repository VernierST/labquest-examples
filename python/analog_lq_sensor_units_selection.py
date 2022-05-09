"""
LabQuest Auto-ID sensors may have up to 3 calibration pages stored on the sensor, 
allowing data to be returned in different units. To read from the other calibration 
pages, modify the select_sensors() argument.

In addition to retrieving measurements in different sensor units, the select_sensors()
argument can be set to read the sensor's raw_voltage. This would allow you to
apply your own custom calibration in the Python code.

To see what the calibration equation and coefficients are, go to the example called:
'analog_lq_sensor_units_info.py'
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()

# Uncomment the different options to see what units are stored on the sensor
lq.select_sensors(ch1='lq_sensor')    # this uses the default calibration page
# lq.select_sensors(ch1='lq_sensor_cal0')    # this uses the cal0 page (this is usually also the default)
# lq.select_sensors(ch1='lq_sensor_cal1')    # this uses the cal1 page
# lq.select_sensors(ch1='lq_sensor_cal2')    # this uses the cal2 page
# lq.select_sensors(ch1='raw_voltage')    # this reads the sensor's raw voltage - no calibration applied

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