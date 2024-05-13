model_first_prediction = np.dot(hidden_layer_values, model_final_weights)

print(model_first_prediction)

# remember output = np.array([real_kg]) => 85 

model_first_error = output- model_first_prediction # 1101 kilos! 
