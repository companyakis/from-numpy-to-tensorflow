word_index = tokenizer.word_index

print(type(word_index)) # <class 'dict'>

rnn_simple_model.add(tf.keras.layers.Embedding(
    len(word_index),
    500, # number of columns our matrix has
    input_length = 600 # maxlen
))

