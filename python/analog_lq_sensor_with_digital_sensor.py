"""
Collect data from a Vernier LabQuest analog sensor and digital sensor. The
dig1 sensor could be 'motion', 'rotary_motion', 'rotary_motion_high_res' 
or 'photogate_count'.
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors(ch1='lq_sensor', dig1='motion')    # Assumes motion detector. Modify as needed.
lq.start(100)    # period in milliseconds. 

ch1_header = lq.enabled_sensor_info('ch1')
dig1_header = lq.enabled_sensor_info('dig1')  
print(ch1_header, dig1_header, sep=", ") 

for x in range(10):
    ch1_measurement = lq.read('ch1')
    dig1_measurement = lq.read('dig1')
    if ch1_measurement == None or dig1_measurement == None: 
        break 
    print(ch1_measurement, dig1_measurement, sep=", ")

lq.stop()
lq.close()