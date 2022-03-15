"""
Visualize sensor data using Matplotlib

Collect and graph data from one Vernier LabQuest sensor using the 
Matplotlib library. This program uses Pyplot, which is part of MatPlotLib. 
Pyplot allows hundreds of options for graph style. See:
https://matplotlib.org/users/index.html and 
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot for information.

Notes:

'sampling_period_ms'
    This value determines how fast data are sampled. Modify as needed.
    - If the sampling period is greater than 10 milliseconds, the sensor's data points are plotted 
      in realtime (point-by-point). 
    - If the sampling period is less than or equal to 10 milliseconds, then plotting of the data 
      does not occur until all samples have been collected (multi-point).

{'ch1':'default'}
    This value is used to configure your LabQuest sensor. Modify as needed.
    For analog sensors:
        - If your LabQuest sensor is connected to CH 2 or CH 3, then simply change 'ch1' to 'ch2' or 'ch3'.
        - If you would like to read from a different calibration page than the 'default', then simply change
          'default' to 'cal0', 'cal1', 'cal2', or 'raw_voltage'.  
    For digital sensors:
        - If your LabQuest digital sensor is connected to DIG 1 or DIG 2, change 'ch1' to 'dig1' or 'dig2'.
        - Change 'default' to either 'motion', 'rotary_motion', 'rotary_motion_high_res', or 'photogate_count'.

"""


from matplotlib import pyplot as plt

from labquest import LabQuest
import logging

# uncomment to show debug messages from the labquest module
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

sampling_period_ms = 250    # if > 10 ms, samples will be collected in realtime, point-by-point. Otherwise, multipoint
num_samples = 41

period_sec = sampling_period_ms/1000
x_axis_list = []
y_axis_list = []

lq.open()
lq.select_sensors({'ch1':'default'})   # configure based on the channel and sensor 
lq.start(sampling_period_ms)  

column_headers = lq.enabled_sensor_info()  

# If there is a column header (a device and sensor connected), then run the data collection code
if column_headers != None:
    plt.xlabel('Time (s)')
    plt.ylabel(column_headers)
    plt.title(column_headers +' vs Time (s)')
    plt.grid(True)

    def single_pt_data_collection():
        for i in range(num_samples):
            measurements = lq.read()
            if measurements == None: 
                break 
            x_axis_list.append(i * period_sec)
            y_axis_list.append(measurements)
            plt.plot(x_axis_list, y_axis_list, color='r')
            plt.pause(0.01)

    def multi_pt_data_collection():
        print("wait for data...")
        y_axis_list = lq.read_multi_pt(num_samples) 
        for x in range(num_samples):
            x_axis_list.append(x * period_sec)
        plt.plot(x_axis_list, y_axis_list, color='r')

    if sampling_period_ms <= 10:
        multi_pt_data_collection()
    else:  
        single_pt_data_collection() 

lq.stop()
lq.close()

plt.show()