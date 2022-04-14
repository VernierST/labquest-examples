"""
Test the Vernier Digital Control Unit (DCU) by sending a 
pattern of 0 through 15 to control the output lines.

The DCU  provides current (up to 600 mA) for controlling 
electrical devices. It connects to the DIG channel of LabQuest or LabQuest Mini. 
Inside the DCU are LEDs that indicate the status of the six output lines. There
are 16 patterns (0 - 15) that allow you independent control of the
first three lines, D1-D3, and limited control of the remaining three lines, D3-D6. 

If you want to control 2 DCUs, configure both DIG channels, and set both outputs with 
the lq.dcu() function, as shown:

lq.select_sensors({'dig1':'dcu', 'dig2':'dcu'})
lq.dcu(x, x)
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
lq.select_sensors({'dig1':'dcu'})
lq.start()    

for x in range(16):
    print(x)
    lq.dcu(x)
    sleep(1)

lq.stop()
lq.close()



