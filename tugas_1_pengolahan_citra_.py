# -*- coding: utf-8 -*-
"""Tugas 1 Pengolahan Citra .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_rp0vZi-JnNcD7DGThXYbdmyM_4g9moW
"""

#pip install numpy
import numpy as np
import imageio  as img
import matplotlib.pyplot as plt

image = img.imread("/content/doggo.png")

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

#merah, biru, hijau
imgRed = np.zeros_like(image)
imgGreen = np.zeros_like(image)
imgBlue = np.zeros_like(image)

imgRed[:,:,0] = red
imgGreen[:,:,1] = green
imgBlue[:,:,2] = blue

plt.figure(figsize=(10,10))
plt.subplot(4,1,1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(4,1,2)
plt.imshow(imgRed)
plt.title("Red Image")

plt.subplot(4,1,3)
plt.imshow(imgGreen)
plt.title("Green Image")

plt.subplot(4,1,4)
plt.imshow(imgBlue)
plt.title("Blue Image")

plt.tight_layout()

plt.show()