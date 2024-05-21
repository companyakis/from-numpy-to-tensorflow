price_pred_model_history = price_pred_model.fit(
    X_train_scaled,
    y_train,
    batch_size = 64,
    epochs = 100,
    verbose = 1,
    validation_split = 0.25,
    callbacks = [early_stopping_price_pred_model]
)

"""
Epoch 1/100
182/182 [==============================] - 2s 5ms/step - loss: 1.5808 - mean_squared_error: 1.5808 - mean_absolute_error: 0.9737 - val_loss: 1.3236 - val_mean_squared_error: 1.3236 - val_mean_absolute_error: 0.8877
Epoch 2/100
182/182 [==============================] - 1s 3ms/step - loss: 1.4829 - mean_squared_error: 1.4829 - mean_absolute_error: 0.9503 - val_loss: 1.3587 - val_mean_squared_error: 1.3587 - val_mean_absolute_error: 0.8777
Epoch 3/100
182/182 [==============================] - 1s 4ms/step - loss: 1.4651 - mean_squared_error: 1.4651 - mean_absolute_error: 0.9430 - val_loss: 1.3759 - val_mean_squared_error: 1.3759 - val_mean_absolute_error: 0.8769
Epoch 4/100
182/182 [==============================] - 1s 3ms/step - loss: 1.4244 - mean_squared_error: 1.4244 - mean_absolute_error: 0.9370 - val_loss: 1.4228 - val_mean_squared_error: 1.4228 - val_mean_absolute_error: 0.8788
Epoch 5/100
182/182 [==============================] - 1s 4ms/step - loss: 1.4349 - mean_squared_error: 1.4349 - mean_absolute_error: 0.9382 - val_loss: 1.4123 - val_mean_squared_error: 1.4123 - val_mean_absolute_error: 0.8780
Epoch 6/100
182/182 [==============================] - 1s 3ms/step - loss: 1.4190 - mean_squared_error: 1.4190 - mean_absolute_error: 0.9336 - val_loss: 1.4406 - val_mean_squared_error: 1.4406 - val_mean_absolute_error: 0.8803
Epoch 7/100
182/182 [==============================] - 1s 4ms/step - loss: 1.3959 - mean_squared_error: 1.3959 - mean_absolute_error: 0.9300 - val_loss: 1.4258 - val_mean_squared_error: 1.4258 - val_mean_absolute_error: 0.8788
Epoch 8/100
182/182 [==============================] - 1s 3ms/step - loss: 1.4029 - mean_squared_error: 1.4029 - mean_absolute_error: 0.9320 - val_loss: 1.4280 - val_mean_squared_error: 1.4280 - val_mean_absolute_error: 0.8789
Epoch 9/100
182/182 [==============================] - 1s 4ms/step - loss: 1.3965 - mean_squared_error: 1.3965 - mean_absolute_error: 0.9307 - val_loss: 1.4314 - val_mean_squared_error: 1.4314 - val_mean_absolute_error: 0.8792
Epoch 10/100
182/182 [==============================] - 1s 3ms/step - loss: 1.3976 - mean_squared_error: 1.3976 - mean_absolute_error: 0.9279 - val_loss: 1.4352 - val_mean_squared_error: 1.4352 - val_mean_absolute_error: 0.8795
Epoch 11/100
182/182 [==============================] - 1s 3ms/step - loss: 1.3732 - mean_squared_error: 1.3732 - mean_absolute_error: 0.9222 - val_loss: 1.4870 - val_mean_squared_error: 1.4870 - val_mean_absolute_error: 0.8860
Epoch 12/100
182/182 [==============================] - 1s 4ms/step - loss: 1.3793 - mean_squared_error: 1.3793 - mean_absolute_error: 0.9217 - val_loss: 1.4493 - val_mean_squared_error: 1.4493 - val_mean_absolute_error: 0.8809
Epoch 13/100
182/182 [==============================] - 1s 4ms/step - loss: 1.3790 - mean_squared_error: 1.3790 - mean_absolute_error: 0.9201 - val_loss: 1.4140 - val_mean_squared_error: 1.4140 - val_mean_absolute_error: 0.8773
Epoch 14/100
182/182 [==============================] - 1s 5ms/step - loss: 1.3778 - mean_squared_error: 1.3778 - mean_absolute_error: 0.9251 - val_loss: 1.5011 - val_mean_squared_error: 1.5011 - val_mean_absolute_error: 0.8880
Epoch 15/100
182/182 [==============================] - 1s 5ms/step - loss: 1.3802 - mean_squared_error: 1.3802 - mean_absolute_error: 0.9220 - val_loss: 1.4347 - val_mean_squared_error: 1.4347 - val_mean_absolute_error: 0.8791
Epoch 16/100
182/182 [==============================] - 1s 5ms/step - loss: 1.3722 - mean_squared_error: 1.3722 - mean_absolute_error: 0.9222 - val_loss: 1.4388 - val_mean_squared_error: 1.4388 - val_mean_absolute_error: 0.8795


"""
