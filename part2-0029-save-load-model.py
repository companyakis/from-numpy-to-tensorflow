price_pred_model.save("final_house_price_prediction_model")

load_price_pred_model = tf.keras.models.load_model("final_house_price_prediction_model")

print(load_price_pred_model.summary())

"""
16]
3s
price_pred_model.save("final_house_price_prediction_model")

load_price_pred_model = tf.keras.models.load_model("final_house_price_prediction_model")

print(load_price_pred_model.summary())
Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense_7 (Dense)             (None, 100)               800       
                                                                 
 dropout_5 (Dropout)         (None, 100)               0         
                                                                 
 dense_8 (Dense)             (None, 90)                9090      
                                                                 
 dropout_6 (Dropout)         (None, 90)                0         
                                                                 
 dense_9 (Dense)             (None, 80)                7280      
                                                                 
 dropout_7 (Dropout)         (None, 80)                0         
                                                                 
 dense_10 (Dense)            (None, 70)                5670      
                                                                 
 dropout_8 (Dropout)         (None, 70)                0         
                                                                 
 dense_11 (Dense)            (None, 60)                4260      
                                                                 
 dropout_9 (Dropout)         (None, 60)                0         
                                                                 
 dense_12 (Dense)            (None, 50)                3050      
                                                                 
 dense_13 (Dense)            (None, 1)                 51        
                                                                 
=================================================================
Total params: 30201 (117.97 KB)
Trainable params: 29401 (114.85 KB)
Non-trainable params: 800 (3.12 KB)
"""
