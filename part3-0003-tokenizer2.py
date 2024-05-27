# We will cover how to create a tokenizer later, but now let's create tf tokenizer 

tf_tokenizer = tf.keras.preprocessing.text.Tokenizer(
    num_words = 60000,
    lower = True,
    oov_token = "",
)

"""
num_words => how many unique words we want to use in our project

lower => all words are lower-case... logical? yes!

oov_token => our of vocabulary token... assume we won't use the word "bargain" etc...
"""
