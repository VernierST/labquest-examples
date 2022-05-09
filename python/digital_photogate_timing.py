"""
Collect timing data from a LabQuest photogate connected to dig1.

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
lq.select_sensors(dig1='photogate_timing') 
lq.start()    # no sample period for photogate_timing

dig1_header = lq.enabled_sensor_info('dig1') 
print(dig1_header)

num_samples = 10
timeout = 10   # timeout is in seconds (how long it will wait for the required number of samples)
timing_measurements = lq.photogate_timing('dig1', num_samples, timeout)
print(timing_measurements)

lq.stop()
lq.close()