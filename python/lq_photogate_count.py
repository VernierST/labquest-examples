"""
Collect count data from a LabQuest photogate connected to DIG 1.

A dictionary is used in the lq.select_sensors() argument to configure a
photogate connected to DIG 1 to perform simple counting. The total
count (unblocked to unblocked) is returned as the measurement, at the 
configured sampling period.
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors({'dig1':'photogate_count'})  
lq.start(500)  

column_headers = lq.enabled_sensor_info()  
print(column_headers)  

for x in range(20):
    measurements = lq.read()
    if measurements == None: 
        break 
    print(measurements)

lq.stop()
lq.close()