import cv2
import numpy as np

# Muat gambar
img = cv2.imread('image/Average_Filter.jpg')

# Tentukan ukuran kernel
kernel_size = 5

# Buat kernelnya
kernel = np.ones((kernel_size,kernel_size),np.float32)/(kernel_size*kernel_size)

# Terapkan filter
filtered_img = cv2.filter2D(img,-1,kernel)

# Tampilkan hasilnya
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
