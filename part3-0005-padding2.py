X_train_padded = tf.keras.utils.pad_sequences(X_train_tr, maxlen = 600)

X_test_padded = tf.keras.utils.pad_sequences(X_test_tr, maxlen = 600)
