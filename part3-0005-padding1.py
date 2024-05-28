# assume wa have a matrix holding the word indexes of the given sentences

sample_word_matrix = [[1, 11], [1, 18, 48], [22, 105, 97, 99]]

padded_sample_word_matrix_1 = tf.keras.utils.pad_sequences(sample_word_matrix)

print(padded_sample_word_matrix_1)

print("-----------------------------------")

padded_sample_word_matrix_2 = tf.keras.utils.pad_sequences(sample_word_matrix, maxlen = 6)

print(padded_sample_word_matrix_2)

"""
[[  0   0   1  11]
 [  0   1  18  48]
 [ 22 105  97  99]]
-----------------------------------
[[  0   0   0   0   1  11]
 [  0   0   0   1  18  48]
 [  0   0  22 105  97  99]]

"""
