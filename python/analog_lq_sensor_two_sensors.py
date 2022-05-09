"""
Collect data from two Vernier LabQuest analog sensors.
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors(ch1='lq_sensor', ch2='lq_sensor')    # Configure ch1 and ch2 with a LabQuest sensor
lq.start(100)    # period in milliseconds. 

ch1_header = lq.enabled_sensor_info('ch1')
ch2_header = lq.enabled_sensor_info('ch2')  
print(ch1_header, ch2_header, sep=", ") 

for x in range(10):
    ch1_measurement = lq.read('ch1')
    ch2_measurement = lq.read('ch2')
    if ch1_measurement == None or ch2_measurement == None: 
        break 
    print(ch1_measurement, ch2_measurement, sep=", ")

lq.stop()
lq.close()