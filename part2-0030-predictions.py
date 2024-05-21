model_predictions = load_price_pred_model.predict(X_test_scaled, batch_size = 64)

print(model_predictions[: 10])

"""
81/81 [==============================] - 0s 3ms/step
[[1.8912495]
 [1.8968076]
 [1.8908713]
 [1.8896182]
 [1.8946856]
 [1.8877798]
 [1.8899809]
 [1.890444 ]
 [1.891448 ]
 [1.8912946]]
"""
