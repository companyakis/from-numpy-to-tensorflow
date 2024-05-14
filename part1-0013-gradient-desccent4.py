import numpy as np

# person data

age = 32

height = 174

real_kg = 85

model_inputs = np.array([age, height])

model_output = np.array([real_kg])

# let's assign initial weights for simplicity

model_weights = np.array([8, -1])

# assume we have 10 epochs

for epoch in range(10):
  # feed forward
  predictions = np.dot(model_inputs, model_weights)

  # error
  error = model_output - predictions

  # slope partial derivative
  slope = 2 * model_inputs * error

  # model should learn => learning rate
  # let's assign an initial value
  learning_rate = 0.0001

  model_weights = model_weights - (learning_rate * slope)

  epoch_l.append(epoch + 1) # range(10) starts from zero

  model_w1_l.append(model_weights[0])

  model_w2_l.append(model_weights[1])

  error_l.append(error)
