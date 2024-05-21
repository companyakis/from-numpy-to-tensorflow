from sklearn.preprocessing import MinMaxScaler

# Create a MinMaxScaler object
scaler = MinMaxScaler()

# Fit and transform the scaler on the training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform the testing data using the same scaler
X_test_scaled = scaler.transform(X_test)

print(X_train_scaled[0])

print(X_test_scaled[0])

"""
[0.2629343  0.39215686 0.07969278 0.05557312 0.02086616 0.00284412
 0.56702128 0.16207951]
 
[0.35313306 0.68627451 0.03966631 0.01916598 0.02587263 0.00300093
 0.55106383 0.18450561]

"""
