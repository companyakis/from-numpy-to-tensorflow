model.fit(
    inputs,
    output,
    epochs = 20,
    batch_size = 32
)

"""
batch_size = 32 => 32 * 312 + 16 = 10000

Epoch 1/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3262 - mean_squared_error: 8243.3262
Epoch 2/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3232 - mean_squared_error: 8243.3232
Epoch 3/20
313/313 [==============================] - 0s 2ms/step - loss: 8243.3281 - mean_squared_error: 8243.3281
Epoch 4/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3301 - mean_squared_error: 8243.3301
Epoch 5/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3311 - mean_squared_error: 8243.3311
Epoch 6/20
313/313 [==============================] - 1s 3ms/step - loss: 8243.3291 - mean_squared_error: 8243.3291
Epoch 7/20
313/313 [==============================] - 1s 3ms/step - loss: 8243.3301 - mean_squared_error: 8243.3301
Epoch 8/20
313/313 [==============================] - 1s 3ms/step - loss: 8243.3262 - mean_squared_error: 8243.3262
Epoch 9/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3301 - mean_squared_error: 8243.3301
Epoch 10/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3281 - mean_squared_error: 8243.3281
Epoch 11/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3301 - mean_squared_error: 8243.3301
Epoch 12/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3262 - mean_squared_error: 8243.3262
Epoch 13/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3252 - mean_squared_error: 8243.3252
Epoch 14/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3281 - mean_squared_error: 8243.3281
Epoch 15/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3301 - mean_squared_error: 8243.3301
Epoch 16/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3301 - mean_squared_error: 8243.3301
Epoch 17/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3291 - mean_squared_error: 8243.3291
Epoch 18/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3281 - mean_squared_error: 8243.3281
Epoch 19/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3291 - mean_squared_error: 8243.3291
Epoch 20/20
313/313 [==============================] - 1s 2ms/step - loss: 8243.3301 - mean_squared_error: 8243.3301
<keras.src.callbacks.History at 0x7ce5b9ab01c0>

"""
