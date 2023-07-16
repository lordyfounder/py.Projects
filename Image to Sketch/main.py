import cv2 as cv

image = cv.imread("C:\\Users\\Chinmay\\OneDrive\\Desktop\\image\\abhi3.jpeg")
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
invert_image = cv.bitwise_not(gray_image)
blur_image = cv.GaussianBlur(invert_image, (21,21), 0)
invert_blur = cv.bitwise_not(blur_image)
sketch = cv.divide(gray_image, invert_blur, scale=256.0)
cv.imwrite("sketch3.jpg",invert_blur)