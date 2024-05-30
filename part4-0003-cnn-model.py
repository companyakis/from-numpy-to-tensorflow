cnn_model = tf.keras.Sequential()

cnn_model.add(tf.keras.layers.Conv2D(32, (3, 3), activation = "relu", input_shape = (32, 32, 3)))
