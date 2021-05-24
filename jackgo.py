# -*- coding: utf-8 -*-
"""JackGO

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ewiLRwUQ-7aNVNUgvGKmrqQphec4GOmH
"""

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

np.set_printoptions(suppress=True)

# Load the model
trained_model = tensorflow.keras.models.load_model('JACKgo_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Path to image
test_image = Image.open('mango.jpg')

size = (224, 224)
test_image = ImageOps.fit(test_image, size, Image.ANTIALIAS)

test_image_array = np.asarray(test_image)

test_image.show()

normalized_test_image_array = (test_image_array.astype(np.float32) / 127.0) - 1

data[0] = normalized_test_image_array

# Print the Prediction
result = trained_model.predict(data)
if result[0][0] > 0.8:
  print("The fruit is identified as Jackfruit")
elif result[0][1] > 0.8:
  print("The fruit is identified as Mango")
else:
  print("Can't identify the fruit")