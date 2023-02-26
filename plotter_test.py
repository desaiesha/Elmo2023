import numpy as np
import matplotlib.pyplot as plt

# Define the data as a numpy array
data = np.array([1.37224, 1.73673, 0.963077, 0.499661, 0.568556, 1.881, 
                 1.36388, 0.796418, 0.885735, 0.702188, 1.6402, -0.0128789, 
                 0.758645, 1.35675, 1.72323, 1.56734, 1.54671, 0.283912, 0.627098])

b = 20
print ("max: ", np.max(data))
print ("min: ", np.min(data))
diff = (np.max(data) -  np.min(data))
print ("diff: ", diff)
print ("avg bin size: ", diff/b)

# Create a histogram with b bins
n, bins, patches = plt.hist(data, b, color='blue')
print ("n: ",n)
print ("b: ",bins)
print ("p: ",patches)
#for i in range (0, len(data)):
#    print (data[i])
print (data)

counts, bins = np.histogram(data)
print ("count: ", counts)
print ("bins: ", bins)

# Set the x-axis limits to include negative and positive DDG values
plt.xlim([-5,5])

# Add a vertical line at 0 to indicate the cutoff for stability
plt.axvline(x=0, color='red', linestyle='--')

# Add labels and a title to the plot
plt.xlabel('DDG Value')
plt.ylabel('Frequency')
plt.title('Histogram of DDG Values')

# Add a grid to the plot
plt.grid(True)

# Display the plot
plt.show()
