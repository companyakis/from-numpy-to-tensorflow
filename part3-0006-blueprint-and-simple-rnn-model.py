"""
let's create our first RNN simple model, but before we should explain out blueprint

model -> Keras Sequential
input layer -> Embedding
hidden layer(s) -> RNNs
output layer -> (positive/negative) class

"""

rnn_simple_model = tf.keras.models.Sequential()
