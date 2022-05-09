"""
Combine the Vernier Digital Control Unit (DCU) with a sensor to automate your
activity or create sensor-controlled projects.

In this example the DCU is combined with a motion detector. However, using a
an analog labquest sensor would work just as well.

Modify the threshold and the logic in the data collection loop as needed.
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
# logging.basicConfig()
# logging.getLogger('labquest').setLevel(logging.DEBUG)

lq = LabQuest()
threshold = 0.5     # modify the threshold as needed

lq.open()
lq.select_sensors(dig1='dcu', dig2='motion') 
lq.start(500)

for x in range(40):
    dig2_measurement = lq.read('dig2')
    print(dig2_measurement)
    if dig2_measurement < threshold:    # modify this logic statement as needed
        print("activate dcu line 1")
        lq.dcu('dig1', 1)
    else:
        print("all dcu lines off")
        lq.dcu('dig1', 0)

lq.stop()
lq.close()