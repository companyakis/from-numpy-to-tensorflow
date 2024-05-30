# stride -> how many rows and columns to advance

# padding -> number of dummy vectors if required

cnn_model.add(tf.keras.layers.Conv2D(64, (3, 3), activation = "relu", strides = (2, 1), padding = "same"))
