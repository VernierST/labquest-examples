"""
Visualize sensor data using Matplotlib

Collect and graph data from one Vernier LabQuest sensor using the 
Matplotlib library. This program uses Pyplot, which is part of MatPlotLib. 
Pyplot allows hundreds of options for graph style. See:
https://matplotlib.org/users/index.html and 
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot for information.

Note:

'sampling_period_ms'
    This value determines how fast data are sampled. Modify as needed.
    - If the sampling period is greater than 10 milliseconds, the sensor's data points are plotted 
      in realtime (point-by-point). 
    - If the sampling period is less than or equal to 10 milliseconds, then plotting of the data 
      does not occur until all samples have been collected (multi-point).
"""


from matplotlib import pyplot as plt

from labquest import LabQuest
import logging

# If troubleshooting is necessary, uncomment the 'logging' code below. If 'INFO' does 
# not provide enough feedback, change 'logging.INFO' to 'logging.DEBUG' 
#logging.basicConfig()
#logging.getLogger('labquest').setLevel(logging.INFO)

lq = LabQuest()

sampling_period_ms = 250    # if > 10 ms, samples will be collected in realtime, point-by-point. Otherwise, multipoint
num_samples = 41

period_sec = sampling_period_ms/1000
x_axis_list = []
y_axis_list = []

lq.open()
lq.select_sensors(ch1='lq_sensor')
lq.start(sampling_period_ms)  

column_header = lq.enabled_sensor_info('ch1')  

# If there is a column header (a device and sensor connected), then run the data collection code
if column_header != None:
    plt.xlabel('Time (s)')
    plt.ylabel(column_header)
    plt.title(column_header +' vs Time (s)')
    plt.grid(True)

    def single_pt_data_collection():
        for i in range(num_samples):
            measurement = lq.read('ch1')
            if measurement == None: 
                break 
            x_axis_list.append(i * period_sec)
            y_axis_list.append(measurement)
            plt.plot(x_axis_list, y_axis_list, color='r')
            plt.pause(0.01)

    def multi_pt_data_collection():
        print("wait for data...")
        y_axis_list = lq.read_multi_pt('ch1', num_samples) 
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