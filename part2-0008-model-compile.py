import tensorflow as tf

model = tf.keras.Sequential()

# input layer

model.add(tf.keras.layers.Input(shape = (2, )))

# hidden layers

# let's add 3 hidden layers

model.add(tf.keras.layers.Dense(40, activation = "relu"))

model.add(tf.keras.layers.Dense(30, activation = "relu"))

model.add(tf.keras.layers.Dense(20, activation = "relu"))

# output layer

model.add(tf.keras.layers.Dense(1, activation = "relu"))

# let's compile

model.compile(
    optimizer = "sgd",
    loss = "mean_squared_error",
    metrics = ["mean_squared_error"]
)
