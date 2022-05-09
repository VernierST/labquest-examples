""" 
Show the stored calibration information of a Vernier LabQuest analog sensor connected to ch1.

LabQuest Auto-ID sensors store up to 3 sets of calibration equations on the sensor, providing
a way to read measurments in different sensor units.

See the example called 'analog_lq_sensor_units_selection.py' for information on how to 
choose the different calibration options in your program. 
"""

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

def get_cal_equation():
    cal_eq = int(sensor_info["calibration_equation"])
    if cal_eq == 1:
        equation_type = 'linear'
        calibration_equation = 'calibrated_value = raw_voltage*K1 + K0'
    elif cal_eq == 2:
        equation_type = 'quadratic'
        calibration_equation = 'calibrated_value = K0 + (K1*raw_voltage) + K2*(raw_voltage**2)'
    elif cal_eq == 3:
        equation_type = 'power function'
        calibration_equation = 'power function; calibrated_value = (raw_voltage**K1)*K0'
    elif cal_eq == 4:
        equation_type = 'modified power'
        calibration_equation = 'calibrated_value = K0*K1**raw_voltage'
    elif cal_eq == 5:
        equation_type = 'logarithmic'
        calibration_equation = 'calibrated_value = K0+K1*(log(raw_voltage))'
    else:  # this would be the cal_eq == 12 case
        equation_type = 'Steinhart-Hart'
        calibration_equation = 'R = 15000/(5/raw_voltage-1); T = 1/(K0+(K1*log(R))+(K2*log(R)*log(R)*log(R)))-273.15'

    return equation_type, calibration_equation

def get_cal_pages(number_of_cal_pages):
    print("Calibration coefficients page 0:")
    print("    KO: ", sensor_info["cal0k0"])
    print("    K1: ", sensor_info["cal0k1"])
    print("    K2: ", sensor_info["cal0k2"])
    print("    Units: ", sensor_info["units0"])
    print("Calibration coefficients page 1:")
    print("    KO: ", sensor_info["cal1k0"])
    print("    K1: ", sensor_info["cal1k1"])
    print("    K2: ", sensor_info["cal1k2"])
    print("    Units: ", sensor_info["units1"])
    if number_of_cal_pages > 2:
        print("Calibration coefficients page 2:")
        print("    KO: ", sensor_info["cal2k0"])
        print("    K1: ", sensor_info["cal2k1"])
        print("    K2: ", sensor_info["cal2k2"])
        print("    Units: ", sensor_info["units2"])

lq.open()
lq.select_sensors(ch1='lq_sensor')   # Configure ch1 with a LabQuest sensor

# This is the call that retrieves all of the analog sensor information. The return value is 
# a dictionary. This only works for sensors connect to 'ch1', 'ch2', or 'ch3'
sensor_info = lq.sensor_info('ch1')  

print('\n')
print("Sensor: ", sensor_info["long_name"])
num_of_cal_pages = int(sensor_info["number_calibration_indices"]) + 1
print("Number of calibration pages: ", num_of_cal_pages)
print("Default calibration page: ", sensor_info["active_calpage"])
eq_type, cal_equation = get_cal_equation()
print("Calibration equation type: ", eq_type)
print("Calibration equation: ", cal_equation)
get_cal_pages(num_of_cal_pages)
print("\n")
# print("Selected channel's full dictionary:")
# print(sensor_info)

lq.close()



