"""
Fast data collection from a Vernier LabQuest analog sensor connected to ch1.

Particular sensors and experiments benefit from faster sampling rates 
(microphone for example). In order to retrieve data at faster sampling 
rates, the data will be collected in packets. In this example, we want 
100 samples to be collected at a sampling rate of 10,000 samples/second. 
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

num_measurements_to_read = 100

lq.open()
lq.select_sensors(ch1='lq_sensor')    # Configure ch1 with a LabQuest sensor 
lq.start(0.1)    # a period of 0.1 milleseconds is equal to a rate of 10,000 samples/sec

ch1_header = lq.enabled_sensor_info('ch1')
print(ch1_header)  

# Note that the read_multi_pt() function is used instead of read(),
# and returns all of the measurements in a list.
ch1_measurements = lq.read_multi_pt('ch1', num_measurements_to_read)
print(ch1_measurements)

lq.stop()
lq.close()