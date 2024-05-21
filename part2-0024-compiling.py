price_pred_model.compile(
    optimizer = tf.keras.optimizers.SGD(learning_rate = 0.001),
    loss = tf.keras.losses.mean_squared_error,
    metrics = [tf.keras.metrics.mean_squared_error, tf.keras.metrics.mean_absolute_error]                     
)
