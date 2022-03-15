""" 
This example uses the sensor_info() function to get a dictionary containing information for 
a Vernier LabQuest analog sensor connected to ch1 (does not work with digital sensors)

LabQuest Auto-ID sensors store sensor information on the sensor. For example, calibration 
information such as:

"calibration_equation" - this value determines how the calibration values are used to 
convert raw voltage to proper sensor units. In most cases the calibraion equation = 1 
(1 is for a linear calibration, 2 = quadratic, 3 = power function, 4 = modified power, 
5 = logarithmic, and 12 = Steinhart-Hart).

"number_calibration_indices" - there can be up to three calibration equations stored on 
a sensor. Each one is stored with an index value, starting with 0. If the 
'number_calibration_indices' = 2, that would mean there are 3 total equations (index 0, 1, and 2)

"active_calpage" - this tells you which calibration equation is the default equation. In most 
cases the equation stored with index = 0 is the default. 

"k0", "k1", and "k2" - these values are used in the calibration equation. For example, if it is 
a linear equation, the conversion would be:    calibrated_value = raw_voltage * k1 + k0
"""

from labquest import LabQuest
import logging

# uncomment to show debug messages from the labquest module
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

ver = lq.get_version()
print("labquest module version: ", ver)
lq.open()
lq.select_sensors({'ch1':'default'})   # connect Vernier LabQuest sensor to CH 1

sensor_info = lq.sensor_info(device=0, channel=1) 
print("\n")
print("Selected channel's dictionary:")
print(sensor_info)
print("\n")
print("Sensor's long name:")
print(sensor_info["long_name"])
print("\n")

lq.close()



