"""
Connect two LabQuest and collect from multiple sensors.

If there is a need for the use of a second LabQuest, simply update the 
lq.select_sensors() argument with a second dictionary for configuring the
channels for your second device. One thing to be aware of is that you should 
plug in your dev0 device first, and then the dev1 device. This should allow 
the dev0 device to be found first. The USB port might also affect which
device is labeled dev0, so you might have to try different ports. 

In this example, dev0 has three LabQuest sensors connected, and dev1 has two.
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors({'ch1':'default', 'ch2':'default', 'ch3':'default'}, {'ch1':'default', 'ch2':'default'})
lq.start(1000)    # period in milliseconds

column_headers = lq.enabled_sensor_info()  
print(column_headers)  

for x in range(10):
    measurements = lq.read()
    if measurements == None: 
        break 
    print(measurements)

lq.stop()
lq.close()