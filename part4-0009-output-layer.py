img_labels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

data_output_numbers = len(img_labels)

cnn_model.add(tf.keras.layers.Dense(data_output_numbers, activation = "sigmoid"))

print(cnn_model.summary())

"""
Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 30, 30, 32)        896       
                                                                 
 max_pooling2d (MaxPooling2  (None, 15, 15, 32)        0         
 D)                                                              
                                                                 
 conv2d_1 (Conv2D)           (None, 8, 15, 64)         18496     
                                                                 
 batch_normalization (Batch  (None, 8, 15, 64)         256       
 Normalization)                                                  
                                                                 
 conv2d_2 (Conv2D)           (None, 3, 13, 64)         36928     
                                                                 
 flatten (Flatten)           (None, 2496)              0         
                                                                 
 dense (Dense)               (None, 2496)              6232512   
                                                                 
 dense_1 (Dense)             (None, 10)                24970     
                                                                 
=================================================================
Total params: 6314058 (24.09 MB)
Trainable params: 6313930 (24.09 MB)
Non-trainable params: 128 (512.00 Byte)
_________________________________________________________________

"""
