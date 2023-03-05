# Import numpy
import numpy as np

# height_in and weight_lb are available as a regular lists
height_in = [72, 93]
weight_lb = [170, 215]

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])
