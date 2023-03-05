import cv2

# load the two input images
img1 = cv2.imread('image/pengurangan.jpg')
img2 = cv2.imread('image/pengurangan1.jpg')

# resize the images to have the same dimensions
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

# convert the images to grayscale
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# subtract the two images
diff_img = cv2.subtract(gray_img1, gray_img2)

# show the resulting image
cv2.imshow('Difference Image', diff_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
