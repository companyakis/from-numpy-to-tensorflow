model_2 = tf.keras.Sequential()

model_2.add(tf.keras.layers.Input(shape = (2, )))

# hidden layers

# let's add 3 hidden layers

model_2.add(tf.keras.layers.Dense(40, activation = "relu", use_bias = False))

model_2.add(tf.keras.layers.Dense(30, activation = "relu", use_bias = False))

model_2.add(tf.keras.layers.Dense(20, activation = "relu"))

# output layer

model_2.add(tf.keras.layers.Dense(1))
