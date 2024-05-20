model_early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor = "val_loss",
    mode = "min",
    verbose = 1,
    min_delta = 5, 
    patience = 10
)
