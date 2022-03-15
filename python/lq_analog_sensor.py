"""
Collect data from a Vernier LabQuest analog sensor connected to CH 1.

A dictionary is used in the lq.select_sensors() argument to configure a
LabQuest sensor for data collection. In this example, the sensor is 
connected to CH 1 and the sensor's default calibration is used. LabQuest Auto-ID 
sensors may have up to 3 calibration pages stored on the sensor, allowing
data to be returned in different units. To read from the other calibration 
pages, or to read the sensor's raw voltage, modify the dictionary value. 

The dictionary Key can be:
'ch1', 'ch2', 'ch3'

If you are using a LabQuest sensor, the dictionary Values can be:
'default', 'cal0', 'cal1', 'cal2', or 'raw_voltage'. 

IF you are using a non-LabQuest sensor, the Values can be:
'raw_voltage'

For example, a Vernier temperature sensor has 3 calibration
pages. The default page (cal0) returns data in Celsius, the second calibration
page (cal1) returns data in Fahrenheit, and the third (cal2) in Kelvin. If you 
connect a Vernier temperature sensor to CH 1 and want readings in 
Celsius, a Vernier temperature sensor to CH 2 and want readings in Fahrenheit, and a
student-built temperature sensor to CH 3 and want this sensor's raw voltage 
(in order to apply your own calibration equation) - the code will be:

lq.select_sensors({'ch1':'default', 'ch2':'cal1', 'ch3':'raw_voltage'})

"""

from labquest import LabQuest
import logging

# uncomment to show debug messages from the labquest module
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

lq.open()
lq.select_sensors({'ch1':'default'})    
#lq.select_sensors()    # if the argument is left blank, the user will get prompts to set up the channels
lq.start(100)    # period in milliseconds. 
#lq.start()    # If the argument is left blank, the user will get a prompt to configure the period

column_headers = lq.enabled_sensor_info()
print(column_headers)  

for x in range(10):
    measurements = lq.read()
    if measurements == None: 
        break 
    print(measurements)

lq.stop()
lq.close()