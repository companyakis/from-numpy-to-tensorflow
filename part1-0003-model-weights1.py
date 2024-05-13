# let's keep model weights in a dictionary

# dictionary values are random

model_weights = {"w0": np.array([np.random.randint(-10,10), np.random.randint(-10,10)]), "w1": np.array([np.random.randint(-10,10), np.random.randint(-10,10)]), "o": np.array([np.random.randint(-10,10), np.random.randint(-10,10)])}

print(model_weights)

# you see random values are NOT constant

"""
first print => {'w0': array([-7,  5]), 'w1': array([-10,   8]), 'o': array([3, 4])}

second print => {'w0': array([-10,   0]), 'w1': array([-10,   7]), 'o': array([ 1, -8])}

"""
