cnn_model.compile(
    optimizer = "adam",
    loss = tf.keras.losses.categorical_crossentropy,
    metrics = ["accuracy"]
)
