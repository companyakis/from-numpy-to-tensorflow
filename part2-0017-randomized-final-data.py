"""
inputs => age, height

output => weight kg

"""

import numpy as np

np.random.seed(101)

inputs = np.random.randint(low = [18, 160], high = [90, 210], size = (10000, 2)) # age and height values

output = np.random.randint(low = [45], high = [130], size = (10000, 1)) # weight kg values

