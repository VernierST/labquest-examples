"""
Collect data from a Vernier LabQuest analog sensor connected to CH 1.
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors(ch1='lq_sensor')    # Configure ch1 with a LabQuest sensor
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