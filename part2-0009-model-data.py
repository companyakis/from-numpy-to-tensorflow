"""
inputs => age, height

output => weight kg

"""

import numpy as np

inputs = np.random.randint(low = [18, 160], high = [90, 210], size = (10000, 2)) # age and height values

output = np.random.randint(low = [45], high = [130], size = (10000, 1)) # weight kg values

print(inputs[: 5])

print(output[:5])

"""
[[ 40 205]
 [ 69 177]
 [ 22 171]
 [ 60 166]
 [ 55 204]]

 
[[ 95]
 [ 58]
 [ 82]
 [ 53]
 [110]]

"""
