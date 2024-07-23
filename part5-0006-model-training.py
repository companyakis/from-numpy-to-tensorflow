optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001)

model.compile(
    loss = "mse",
    optimizer = optimizer,
    metrics = ["RootMeanSquaredError"]
)

normalization_layer.adapt(X_train)

history = model.fit(
    X_train,
    y_train,
    epochs = 25,
    validation_split = 0.2
)

"""
Epoch 16/25
387/387 [==============================] - 1s 4ms/step - loss: 0.2883 - root_mean_squared_error: 0.5369 - val_loss: 0.3359 - val_root_mean_squared_error: 0.5796
Epoch 17/25
387/387 [==============================] - 1s 3ms/step - loss: 0.2844 - root_mean_squared_error: 0.5333 - val_loss: 0.3213 - val_root_mean_squared_error: 0.5669
Epoch 18/25
387/387 [==============================] - 2s 4ms/step - loss: 0.2790 - root_mean_squared_error: 0.5282 - val_loss: 0.3228 - val_root_mean_squared_error: 0.5681
Epoch 19/25
387/387 [==============================] - 2s 5ms/step - loss: 0.2802 - root_mean_squared_error: 0.5294 - val_loss: 0.3164 - val_root_mean_squared_error: 0.5625
Epoch 20/25
387/387 [==============================] - 1s 4ms/step - loss: 0.2769 - root_mean_squared_error: 0.5262 - val_loss: 0.3113 - val_root_mean_squared_error: 0.5579
Epoch 21/25
387/387 [==============================] - 1s 3ms/step - loss: 0.2779 - root_mean_squared_error: 0.5272 - val_loss: 0.3230 - val_root_mean_squared_error: 0.5683
Epoch 22/25
387/387 [==============================] - 1s 3ms/step - loss: 0.2784 - root_mean_squared_error: 0.5277 - val_loss: 0.3484 - val_root_mean_squared_error: 0.5903
Epoch 23/25
387/387 [==============================] - 1s 3ms/step - loss: 0.2898 - root_mean_squared_error: 0.5383 - val_loss: 0.3115 - val_root_mean_squared_error: 0.5581
Epoch 24/25
387/387 [==============================] - 1s 4ms/step - loss: 0.2749 - root_mean_squared_error: 0.5243 - val_loss: 0.3292 - val_root_mean_squared_error: 0.5738
Epoch 25/25
387/387 [==============================] - 1s 3ms/step - loss: 0.2727 - root_mean_squared_error: 0.5222 - val_loss: 0.3040 - val_root_mean_squared_error: 0.5513
"""
