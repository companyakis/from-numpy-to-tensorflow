import tensorflow as tf

tf.random.set_seed(42)

normalization_layer = tf.keras.layers.Normalization()

hidden_layer_1 = tf.keras.layers.Dense(30, activation = "relu")

hidden_layer_2 = tf.keras.layers.Dense(20, activation = "relu")

hidden_layer_3 = tf.keras.layers.Dense(10, activation = "relu")
