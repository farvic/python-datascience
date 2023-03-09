import numpy as np

# random distributions
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
# puts them together as two columns
np_city = np.column_stack((height, weight))

# np_city: array of height and weights
# the mean value of pp's heights 1.7472
print(np.mean(np_city[:, 0]))

# median
print(np.median(np_city[:, 0]))

# check if width and height are correlated
print(np.corrcoef(np_city[:, 0], np_city[:, 1]))

# std deviation
print(np.std(np_city[:, 0]))
