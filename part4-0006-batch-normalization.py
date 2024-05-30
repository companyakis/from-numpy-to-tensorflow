cnn_model.add(tf.keras.layers.BatchNormalization())

cnn_model.add(tf.keras.layers.Conv2D(64, (3, 3), 
                                     strides = (2, 1),
                                     kernel_initializer = tf.keras.initializers.random_normal(0.001),
                                     use_bias = True,
                                     activation = "relu"
                                     ))
