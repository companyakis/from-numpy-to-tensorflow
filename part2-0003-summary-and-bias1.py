model.summary()

"""
bias

assume our model is y = W * x + b

120 = 40 * 2 + 40

1230 = 30 * 40 + 30

620 = 20 * 30 + 20

21 = 1 * 20 + 1

...

but we don't have to use "bias" in our model

Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense (Dense)               (None, 40)                120       
                                                                 
 dense_1 (Dense)             (None, 30)                1230      
                                                                 
 dense_2 (Dense)             (None, 20)                620       
                                                                 
 dense_3 (Dense)             (None, 1)                 21        
                                                                 
=================================================================
Total params: 1991 (7.78 KB)
Trainable params: 1991 (7.78 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________

"""
