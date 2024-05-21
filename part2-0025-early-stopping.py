early_stopping_price_pred_model = tf.keras.callbacks.EarlyStopping(
    monitor = "val_loss",
    verbose = 1,
    min_delta = 2,
    patience = 15
)
