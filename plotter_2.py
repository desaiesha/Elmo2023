
import numpy as np
import matplotlib.pyplot as plt
import mplcursors
import statistics
from scipy.stats import norm


# Create a numpy array from the given data
data = np.array([(1.37224,), (1.73673,), (0.963077,), (0.499661,), (0.568556,),
                 (1.881,), (1.36388,), (0.796418,), (0.885735,), (0.702188,),
                 (1.6402,), (-0.0128789,), (0.758645,), (1.35675,), (1.72323,),
                 (1.56734,), (1.54671,), (0.283912,), (0.627098,)])

# Create a histogram of the data and display it
n, bins, patches = plt.hist(data, bins=10, density=True, alpha=0.5)
data = np.random.normal(170, 5, 10)
print (data)
plt.hist(data)

#Set up the cursor to display the data point when hovering over a bar in the histogram
cursor = mplcursors.cursor(hover=True)
@cursor.connect("add")
def on_add(sel):
    index = sel.target.index
    sel.annotation.set_text(f"Data point: {data[index]}")

# Add a title to the plot
plt.title('Histogram of Data')

# Display the plot
plt.show()
