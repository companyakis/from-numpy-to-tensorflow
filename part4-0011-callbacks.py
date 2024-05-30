cnn_model_early_stop = tf.keras.callbacks.EarlyStopping(monitor = "val_loss", verbose = 1, patience = 3)

cnn_model_checkpointer = tf.keras.callbacks.ModelCheckpoint("cnn_best_model", monitor = "val_loss", verbose = 1, save_best_only = True)

cnn_model_callbacks = [cnn_model_early_stop, cnn_model_checkpointer]
