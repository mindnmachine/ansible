"""
Python code to animate wave motion and view different plots as they
propagate in time.
Engineering Summer Program for Teachers (ESP4T)
July 2017, University of Wyoming
"""
# Importing required libraries 
"""import numpy and as the variable np"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# important variables in any simulation (step in seconds)
step = 0.05
numstep = 1000

# change to see the wave vary with amplitude
"""create a variable 'amp' that has a value of 1.0"""

# Defining a function to compute the y values for plotting
def data_gen():
    # time variable starting at 0 seconds
    t = 0
    # plotting 1000 points iteratively
    ctr = 0
    for ctr in range(numstep):
        # calculating the y value for each wave at a given time (1 Hz)
        """ create a variable 'y1' using the equation: y = Asin(2*pi*f + theta), wmake y1 equal to
        the equation of a wave with an amplitude of 'amp',a frequency of 1Hz, a time of 't' and
        a theta of 0"""
        
        # SHM wave with twice the frequency
        """ create a variable 'y2' using the equation: y = Asin(2*pi*f + theta), make y2 equal to
        the equation of a wave with an amplitude of 'amp',a frequency of 2Hz, a time of 't' and
        a theta of 0"""
        
        # SHM wave with a damping coefficient i.e. damped sine wave
        # (decay OR damping constant = 0.25)
        y3 = amp*np.sin(2*np.pi*1*t) * np.exp(-t*0.25)
        # moving through time in 0.05 second intervals i.e. stepping through time
        t += step
        yield t, y1, y2, y3

# create a figure with three subplots and set the size of the window
fig, (ax1, ax2, ax3) = plt.subplots(3,1,figsize=(10,20))

# initializations to set the limits for each axis and introduce a grid
for ax in [ax1, ax2, ax3]:
    ax.set_ylim(-(amp+0.2), (amp+0.2))
    # change this for a simulation of a certain number of seconds (10 as of now)
    ax.set_xlim(0, 10)
    ax.grid()
    # introducing gridlines at each number between 1 and 10
    ax.set_xticks(np.arange(1,11))

# data arrays to store the values for plotting
# time in the X axis and values of the wave in the Y axis
xdata, y1data, y2data, y3data = [], [], [], []

# intialize three line objects (one in each subplot)
"""Create a variable 'line1' equal to ax1 plot of xdata and y1data. Make the plot blue"""
"""Create a variable 'line2' equal to ax2 plot of xdata and y2data. Make the plot red"""
"""Create a variable 'line3' equal to ax3 plot of xdata and y3data. Make the plot green"""
line = [line1, line2, line3]

# setting the title for each subplot 
"""set the title of ax1 to "SHM wave with frequwncy of 1Hz" and give it a size of 10"""

"""set the title of ax2 to "SHM wave with frequency of 2 Hz" and give it a size of 10"""

"""set the title of ax3 to "Damped sine wave with decay constant of 0.25" and give it a size of 10"""

# labeling the x axis as time in seconds and setting the fontsize
ax3.set_xlabel('Time (s)', size=15)

# defining a function to obtain the data values
def calculate(data):
    # update the data
    x, y1, y2, y3 = data
    """update xdata by adding 'x' to its list"""

    """update y1data by adding 'y1' to its list"""

    """update y2data by adding 'y2' to its list"""

    """update y3data by adding 'y3' to its list"""

    # update the data of both line objects
    """update subplot 1 by filling the first spot in the line array with the updated data"""

    """update subplot 2 by filling the second spot in the line array with the updated data"""

    """update subplot 3 by filling the third spot in the line array with the updated data"""
    return line

ani = animation.FuncAnimation(fig, calculate, data_gen, blit=True, interval=50, repeat=False)
"""use 'plt.show' to make the graphs visible"""