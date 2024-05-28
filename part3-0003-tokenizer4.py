# splitting

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    raw_data['review'],
    raw_data['sentiment_encoded'],
    test_size = 0.20,
    random_state = 101,
    stratify = raw_data['sentiment_encoded'],
)

# training 

tokenizer.fit_on_texts(X_train)
