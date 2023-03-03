import cv2
import matplotlib.pyplot as plt

# Muat gambar
img = cv2.imread('image/Hestogram.jpg', 0)

# Hitung histogramnya
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Gambarkan histogramnya
plt.plot(hist)

# tampilan pltnya
plt.show()
