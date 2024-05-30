img_labels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

import matplotlib.pyplot as plt

plt.imshow(train_images[9999])

plt.show()

print(train_labels[9999]) # [5]

print(img_labels[train_labels[9999][0]]) # dog
