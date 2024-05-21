score = load_price_pred_model.evaluate(X_test_scaled, y_test, batch_size = 64)

print(score)

"""
81/81 [==============================] - 0s 4ms/step - loss: 1.3763 - mean_squared_error: 1.3763 - mean_absolute_error: 0.8881

[1.3763047456741333, 1.3763047456741333, 0.8881480097770691]

"""
