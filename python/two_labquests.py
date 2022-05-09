"""
Connect two LabQuest and collect from multiple sensors. This example focuses on
digital sensors, but could certainly be modified for including analog sensors.

Notes:

If there is a need for the use of a second LabQuest there will need to be 
an addition argument (device=1) for the select_sensors(), enabled_sensor_info(), 
and read() functions. 

Be aware that it might not be obvious which device is device=0
and which is device=1. You might have to determine if the first device plugged into
USB is device 0 or 1. The USB port might also affect which device is 0 or 1. Do some
experimenting. In addition, if you are using a LQ Mini, when the lq.open() 
function is called, device 0's LED will turn greeen first.
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
# logging.basicConfig()
# logging.getLogger('labquest').setLevel(logging.DEBUG)

lq = LabQuest()

lq.open()
lq.select_sensors(dig1='motion', dig2='rotary_motion')
lq.select_sensors(dig1='photogate_count', device=1) 
lq.start(100)


dig1_header = lq.enabled_sensor_info('dig1')
dig2_header = lq.enabled_sensor_info('dig2') 
dig1_1_header = lq.enabled_sensor_info('dig1', device=1)
print(dig1_header, dig2_header, dig1_1_header, sep=", ")

for x in range(5):
    dig1_measurement = lq.read('dig1')
    dig2_measurement = lq.read('dig2')
    dig1_1_measurement = lq.read('dig1', device=1)
    if dig1_measurement == None or dig2_measurement == None or dig1_1_measurement == None: 
        break 
    print(dig1_measurement, dig2_measurement, dig1_1_measurement, sep=", ")

lq.stop()
lq.close()