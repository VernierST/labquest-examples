"""
Control the Vernier Digital Control Unit (DCU) output lines by sending a 
pattern of 0 through 15.

The DCU  provides current (up to 600 mA) for controlling 
electrical devices. It connects to the dig1 or dig2 channels of LabQuest or LabQuest Mini. 
Inside the DCU are LEDs that indicate the status of the six output lines. There
are 16 patterns (0 - 15) that allow you independent control of the
first three lines, D1-D3, and limited control of the remaining three lines, D3-D6. 
"""

from time import sleep

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors(dig1='dcu')
lq.start()   # start() does not have a period argument if it's only the dcu (no sensor measurements) 

for x in range(16):
    print(x)
    lq.dcu('dig1', x)    # 'x' is the value that determines the dcu output
    sleep(1)

lq.stop()
lq.close()



