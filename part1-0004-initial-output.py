# model output

ho_val = (inputs * model_weights["w0"]).sum()

h1_val = (inputs * model_weights["w1"]).sum()

hidden_layer_val = np.array([ho_val, h1_val])

print(hidden_layer_val) # [1250   46]

output_val = (hidden_layer_val * model_weights["o"]).sum()

print(output_val) # 6204

# initial output is AWFUL

# np.random.seed()!!!!
