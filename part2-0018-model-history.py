model_history = model.fit(
    inputs,
    output,
    epochs = 100,
    batch_size = 32,
    verbose = 1,
    validation_split = 0.2,
    callbacks = [model_early_stopping]
)

"""
Epoch 1/100
250/250 [==============================] - 2s 5ms/step - loss: 129518152.0000 - mean_squared_error: 129518152.0000 - mean_absolute_error: 795.9416 - val_loss: 8108.6304 - val_mean_squared_error: 8108.6304 - val_mean_absolute_error: 86.5855
Epoch 2/100
250/250 [==============================] - 1s 4ms/step - loss: 8222.9854 - mean_squared_error: 8222.9854 - mean_absolute_error: 87.2875 - val_loss: 8108.6304 - val_mean_squared_error: 8108.6304 - val_mean_absolute_error: 86.5855
Epoch 3/100
250/250 [==============================] - 1s 3ms/step - loss: 8222.9854 - mean_squared_error: 8222.9854 - mean_absolute_error: 87.2875 - val_loss: 8108.6304 - val_mean_squared_error: 8108.6304 - val_mean_absolute_error: 86.5855
Epoch 4/100
250/250 [==============================] - 1s 3ms/step - loss: 8222.9854 - mean_squared_error: 8222.9854 - mean_absolute_error: 87.2875 - val_loss: 8108.6304 - val_mean_squared_error: 8108.6304 - val_mean_absolute_error: 86.5855
Epoch 5/100
250/250 [==============================] - 1s 2ms/step - loss: 8222.9873 - mean_squared_error: 8222.9873 - mean_absolute_error: 87.2875 - val_loss: 8108.6304 - val_mean_squared_error: 8108.6304 - val_mean_absolute_error: 86.5855
Epoch 6/100
250/250 [==============================] - 1s 3ms/step - loss: 8222.9873 - mean_squared_error: 8222.9873 - mean_absolute_error: 87.2875 - val_loss: 8108.6304 - val_mean_squared_error: 8108.6304 - val_mean_absolute_error: 86.5855
Epoch 7/100
250/250 [==============================] - 1s 3ms/step - loss: 8222.9873 - mean_squared_error: 8222.9873 - mean_absolute_error: 87.2875 - val_loss: 8108.6304 - val_mean_squared_error: 8108.6304 - val_mean_absolute_error: 86.5855
Epoch 8/100
250/250 [==============================] - 1s 3ms/step - loss: 8222.9893 - mean_squared_error: 8222.9893 - mean_absolute_error: 87.2875 - val_loss: 8108.6304 - val_mean_squared_error: 8108.6304 - val_mean_absolute_error: 86.5855
Epoch 9/100
250/250 [==============================] - 1s 2ms/step - loss: 8222.9873 - mean_squared_error: 8222.9873 - mean_absolute_error: 87.2875 - val_loss: 8108.6304 - val_mean_squared_error: 8108.6304 - val_mean_absolute_error: 86.5855
Epoch 10/100
250/250 [==============================] - 1s 3ms/step - loss: 8222.9844 - mean_squared_error: 8222.9844 - mean_absolute_error: 87.2875 - val_loss: 8108.6304 - val_mean_squared_error: 8108.6304 - val_mean_absolute_error: 86.5855
Epoch 11/100
250/250 [==============================] - 1s 3ms/step - loss: 8222.9873 - mean_squared_error: 8222.9873 - mean_absolute_error: 87.2875 - val_loss: 8108.6304 - val_mean_squared_error: 8108.6304 - val_mean_absolute_error: 86.5855
Epoch 11: early stopping
"""
