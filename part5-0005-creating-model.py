input_layer = tf.keras.layers.Input(shape = X_train.shape[1:]) # ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

normalized = normalization_layer(input_layer)

hidden1 = hidden_layer_1(normalized)

hidden2 = hidden_layer_2(hidden1)

hidden3 = hidden_layer_3(hidden2)

concat = concatenation_layer([normalized, hidden3])

output = output_layer(concat)

model = tf.keras.Model(inputs = [input_layer], outputs = [output])

print(model.summary())

"""
Model: "model"
__________________________________________________________________________________________________
 Layer (type)                Output Shape                 Param #   Connected to                  
==================================================================================================
 input_1 (InputLayer)        [(None, 8)]                  0         []                            
                                                                                                  
 normalization (Normalizati  (None, 8)                    17        ['input_1[0][0]']             
 on)                                                                                              
                                                                                                  
 dense (Dense)               (None, 30)                   270       ['normalization[0][0]']       
                                                                                                  
 dense_1 (Dense)             (None, 30)                   930       ['dense[0][0]']               
                                                                                                  
 dense_2 (Dense)             (None, 30)                   930       ['dense_1[0][0]']             
                                                                                                  
 concatenate (Concatenate)   (None, 38)                   0         ['normalization[0][0]',       
                                                                     'dense_2[0][0]']             
                                                                                                  
 dense_3 (Dense)             (None, 1)                    39        ['concatenate[0][0]']         
                                                                                                  
==================================================================================================
Total params: 2186 (8.54 KB)
Trainable params: 2169 (8.47 KB)
Non-trainable params: 17 (72.00 Byte)
__________________________________________________________________________________________________
None


"""
