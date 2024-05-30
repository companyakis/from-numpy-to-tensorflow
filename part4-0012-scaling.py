# remember our data

# (train_images, train_labels) , (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

# remember data_output_numbers = len(img_labels)

X_train = train_images.astype('float32')

X_test = test_images.astype('float32')

X_train = X_train / 255

X_test = X_test / 255

y_train = tf.keras.utils.to_categorical(train_labels, data_output_numbers)

y_test = tf.keras.utils.to_categorical(test_labels, data_output_numbers)

print(y_train[0])

print(X_train[0])

"""
[0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]

[[[0.23137255 0.24313726 0.24705882]
  [0.16862746 0.18039216 0.1764706 ]
  [0.19607843 0.1882353  0.16862746]
  ...
  [0.61960787 0.5176471  0.42352942]
  [0.59607846 0.49019608 0.4       ]
  [0.5803922  0.4862745  0.40392157]]

 [[0.0627451  0.07843138 0.07843138]
  [0.         0.         0.        ]
  [0.07058824 0.03137255 0.        ]
  ...
  [0.48235294 0.34509805 0.21568628]
  [0.46666667 0.3254902  0.19607843]
  [0.47843137 0.34117648 0.22352941]]

 [[0.09803922 0.09411765 0.08235294]
  [0.0627451  0.02745098 0.        ]
  [0.19215687 0.10588235 0.03137255]

  .....

"""
