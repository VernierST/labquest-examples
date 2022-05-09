"""
Collect data from a LabQuest motion detector connected to dig1.
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors(dig1='motion')    # Configure dig1 with a motion detector
lq.start(1000)    # period in milliseconds. 

dig1_header = lq.enabled_sensor_info('dig1')
print(dig1_header)  

for x in range(10):
    dig1_measurement = lq.read('dig1')
    if dig1_measurement == None: 
        break 
    print(dig1_measurement)

lq.stop()
lq.close()