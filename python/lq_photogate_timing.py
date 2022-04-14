"""
Collect timing data from a LabQuest photogate connected to DIG 1.

A dictionary is used in the lq.select_sensors() argument to configure a
photogate connected to DIG 1 to perform timing. 

photogate_timing (semi-period timing) returns:
blocked time, unblocked time, blocked time, unblocked time, etc..
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors({'dig1':'photogate_timing'})   
lq.start()    # no sample period for photogate_timing

column_headers = lq.enabled_sensor_info()  
print(column_headers)  

num_samples = 10
timeout = 10   # timeout is in seconds (how long it will wait for the required number of samples)
timing_measurements = lq.photogate_timing(num_samples, timeout)
print(timing_measurements)

lq.stop()
lq.close()