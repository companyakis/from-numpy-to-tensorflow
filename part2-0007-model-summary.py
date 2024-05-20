model_3.summary()

"""
Total params: 1921 and Trainable params: 1841

80 = 40 * 2
1200 = 40 * 30
620 = 20 * 30 + 20 => bias = 20
21 = 1 * 20 + 1 => bias = 1

1921 - 80 = 1841 => non_trainable_params = 80

--------------------------------------------------------------------

Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense (Dense)               (None, 40)                80        
                                                                 
 dense_1 (Dense)             (None, 30)                1200      
                                                                 
 dense_2 (Dense)             (None, 20)                620       
                                                                 
 dense_3 (Dense)             (None, 1)                 21        
                                                                 
=================================================================
Total params: 1921 (7.50 KB)
Trainable params: 1841 (7.19 KB)
Non-trainable params: 80 (320.00 Byte)
_________________________________________________________________

"""
