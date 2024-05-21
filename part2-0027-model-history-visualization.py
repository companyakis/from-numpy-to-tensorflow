import matplotlib.pyplot as plt

plt.plot(price_pred_model_history.history["loss"])

plt.plot(price_pred_model_history.history["val_loss"])

plt.title("House Price Prediction Model Loss Graph")

plt.xlabel("Number of Epochs")

plt.ylabel("Loss Value")

plt.legend(["training", "validation"], loc = "upper right")

plt.show()
