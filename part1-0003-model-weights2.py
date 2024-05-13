# let's keep model weights in a dictionary

# dictionary values are random

# you see random values are NOT constant

# why not use "numpy random seed"

np.random.seed(101)

model_weights = {"w0": np.array([np.random.randint(-10,10), np.random.randint(-10,10)]), "w1": np.array([np.random.randint(-10,10), np.random.randint(-10,10)]), "o": np.array([np.random.randint(-10,10), np.random.randint(-10,10)])}

print(model_weights)

"""
first print => {'w0': array([1, 7]), 'w1': array([-4,  1]), 'o': array([ 5, -1])}

second print => {'w0': array([1, 7]), 'w1': array([-4,  1]), 'o': array([ 5, -1])}

"""
