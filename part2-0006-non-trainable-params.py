import tensorflow as tf

model_3 = tf.keras.Sequential()

model_3.add(tf.keras.layers.Input(shape = (2, )))

# hidden layers

# let's add 3 hidden layers

model_3.add(tf.keras.layers.Dense(40, activation = "relu", use_bias = False, trainable = False))

model_3.add(tf.keras.layers.Dense(30, activation = "relu", use_bias = False))

model_3.add(tf.keras.layers.Dense(20, activation = "relu"))

# output layer

model_3.add(tf.keras.layers.Dense(1))
