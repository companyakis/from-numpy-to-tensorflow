price_pred_model.fit(
    X_train_scaled,
    y_train,
    batch_size = 64,
    epochs = 4,
    verbose = 1,
    validation_split = 0.25,    
)

"""
Epoch 1/4
182/182 [==============================] - 2s 5ms/step - loss: 2.6357 - mean_squared_error: 2.6357 - mean_absolute_error: 1.2657 - val_loss: 1.3186 - val_mean_squared_error: 1.3186 - val_mean_absolute_error: 0.9185
Epoch 2/4
182/182 [==============================] - 1s 4ms/step - loss: 1.4923 - mean_squared_error: 1.4923 - mean_absolute_error: 0.9570 - val_loss: 1.3205 - val_mean_squared_error: 1.3205 - val_mean_absolute_error: 0.8897
Epoch 3/4
182/182 [==============================] - 1s 4ms/step - loss: 1.4764 - mean_squared_error: 1.4764 - mean_absolute_error: 0.9503 - val_loss: 1.3260 - val_mean_squared_error: 1.3260 - val_mean_absolute_error: 0.8854
Epoch 4/4
182/182 [==============================] - 1s 4ms/step - loss: 1.4333 - mean_squared_error: 1.4333 - mean_absolute_error: 0.9354 - val_loss: 1.3386 - val_mean_squared_error: 1.3386 - val_mean_absolute_error: 0.8805
<keras.src.callbacks.History at 0x78ea4836eb60>

"""
