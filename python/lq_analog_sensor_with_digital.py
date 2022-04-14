"""
Collect data from an analog and digital sensor, simultaneously.

Most LabQuest digital sensors send measurements at a specified period, 
just like the LabQuest analog sensors. Configure the channel dictionary
to include both analog and digital sensors, and the lq.read() function
will send back measurements from both. 

Note that photogate_count works this way, but photogate_timing does not.
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()

# various options for configuring different digital sensors
lq.select_sensors({'ch1':'default', 'dig1':'motion'}) 
#lq.select_sensors({'ch1':'default', 'dig1':'rotary_motion'})
#lq.select_sensors({'ch1':'default', 'dig1':'rotary_motion_high_res'})
#lq.select_sensors({'ch1':'default', 'dig1':'photogate_count'})

lq.start(250)    # period of 250 milliseconds

column_headers = lq.enabled_sensor_info()  
print(column_headers)  

for x in range(15):
    measurements = lq.read()
    if measurements == None: 
        break 
    print(measurements)

lq.stop()
lq.close()