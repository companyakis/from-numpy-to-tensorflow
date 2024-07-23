from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
        dataset_housing.data,
        dataset_housing.target,
        random_state=42
)

print(X_train.shape)

print(X_test.shape)

print(y_train.shape)

print(y_test.shape)

"""
(15480, 8)
(5160, 8)
(15480,)
(5160,)

"""
