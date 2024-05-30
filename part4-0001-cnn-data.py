import tensorflow as tf

(train_images, train_labels) , (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

print(train_images.shape)

print(test_images.shape)

print(train_labels[: 3])

print(test_labels[: 3])

"""
(50000, 32, 32, 3)

50000 -> number of examples

32 * 32 -> dimensions

3 -> RGB channels

******

(50000, 32, 32, 3)

(10000, 32, 32, 3)
[[6]
 [9]
 [9]]
 
[[3]
 [8]
 [8]]

"""
