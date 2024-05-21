price_pred_model = tf.keras.Sequential()

shape = X_train_scaled.shape[1] # X_train_scaled.shape => (15480, 8)

# input 
price_pred_model.add(tf.keras.layers.Input(shape = (shape, )))

# hiddens and dropouts

price_pred_model.add(tf.keras.layers.Dense(100, activation = "relu", use_bias = False, trainable = False)) # Why not:) We can change if we want...

price_pred_model.add(tf.keras.layers.Dropout(0.1))

price_pred_model.add(tf.keras.layers.Dense(90, activation = "relu", kernel_initializer = tf.keras.initializers.RandomNormal(stddev = 0.001), kernel_constraint = tf.keras.constraints.MaxNorm(5)))

price_pred_model.add(tf.keras.layers.Dropout(0.15))

price_pred_model.add(tf.keras.layers.Dense(80, activation = "relu", bias_initializer = tf.keras.initializers.Ones()))

price_pred_model.add(tf.keras.layers.Dropout(0.2))

price_pred_model.add(tf.keras.layers.Dense(70, activation = "relu"))

price_pred_model.add(tf.keras.layers.Dropout(0.1))

price_pred_model.add(tf.keras.layers.Dense(60, activation = "relu"))

price_pred_model.add(tf.keras.layers.Dropout(0.1))

price_pred_model.add(tf.keras.layers.Dense(50, activation = "relu"))

# output

price_pred_model.add(tf.keras.layers.Dense(1, activation = "relu"))
