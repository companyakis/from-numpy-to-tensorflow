import tensorflow as tf

model = tf.keras.Sequential()

# input layer

model.add(tf.keras.layers.Input(shape = (2, )))

# hidden layers

# let's change weight matrix => kernel

model.add(tf.keras.layers.Dense(40, activation = "relu", kernel_initializer = tf.keras.initializers.random_normal(stddev = 0.001), kernel_constraint = tf.keras.constraints.max_norm(4)))

model.add(tf.keras.layers.Dense(30, activation = "relu"))

model.add(tf.keras.layers.Dense(20, activation = "relu"))

# output layer

model.add(tf.keras.layers.Dense(1, activation = "relu"))
