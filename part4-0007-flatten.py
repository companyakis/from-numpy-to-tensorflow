"""
example:

our_array = [[1, 2, 3], [4, 5, 6]] 
flattened_our_array = [1, 2, 3, 4, 5, 6]

"""

cnn_model.add(tf.keras.layers.Flatten())

print(cnn_model.summary()) # 2496 = 3 * 13 * 64

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
                                                                 
=================================================================
Total params: 56576 (221.00 KB)
Trainable params: 56448 (220.50 KB)
Non-trainable params: 128 (512.00 Byte)

"""
