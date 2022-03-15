"""
Fast data collection from a Vernier LabQuest analog sensor connected to CH 1.

Particular sensors and experiments benefit from faster sampling rates 
(microphone for example). In order to retrieve data at faster sampling 
rates, the data will be collected in packets. In this example, we want 
100 samples to be collected at a sampling rate of 10,000 samples/second. 
"""

from labquest import LabQuest
import logging

# uncomment to show debug messages from the labquest module
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

num_measurements_to_read = 100

lq.open()
lq.select_sensors({'ch1':'default'})  
lq.start(0.1)    # a period of 0.1 milleseconds is equal to a rate of 10,000 samples/sec

column_headers = lq.enabled_sensor_info()  
print(column_headers)  

measurements = lq.read_multi_pt(num_measurements_to_read)
print(measurements)

lq.stop()
lq.close()