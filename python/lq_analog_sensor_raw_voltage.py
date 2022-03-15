"""
Collect data from a non-Vernier analog sensor, or the uncalibrated
signal of a LabQuest sensor, connected to CH 1.

If you would like to connect a non-Vernier sensor to the LabQuest
device, you would configure the channel to read raw voltage.

The dictionary Key can be:
'ch1', 'ch2', 'ch3'

The dictionary Value, for these Keys, would be:
'raw_voltage'

For example, you connect a LabQuest temperature sensor to CH 1 and 
want readings in Celsius, and a non-Vernier temperature sensor 
to CH 2 and want this sensor's raw voltage in order to
apply your own calibration equation. The code will be:

lq.select_sensors({'ch1':'default', 'ch2':'raw_voltage'})

Note: The Vernier Breadboard Cable (order code: BB-BTA), provides an 
easy way to wire a custom sensor into a LabQuest device.
"""

from labquest import LabQuest
import logging

# uncomment to show debug messages from the labquest module
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors({'ch1':'raw_voltage'})    
lq.start(100)    # period in milliseconds. 

column_headers = lq.enabled_sensor_info()  
print(column_headers)  

for x in range(10):
    measurements = lq.read()
    if measurements == None: 
        break 
    print(measurements)

lq.stop()
lq.close()