model.compile(
    
    optimizer = tf.keras.optimizers.SGD(learning_rate = 0.001),
    loss = tf.keras.losses.MeanSquaredError(),
    metrics = [tf.keras.metrics.MeanSquaredError(), tf.keras.metrics.MeanAbsoluteError()]

)
