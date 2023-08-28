import numpy as np
import cv2


image = cv2.imread("/Users/siqili/Downloads/pscf_win_2022_50ft/pscf_win_2022_10ft/90/DJI_00018.JPG_90_4765_2690_5391_2882.png")
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('Original image', image)
cv2.imshow('HSV image', hsvImage)

lower_blue = np.array([15,50,180])
upper_blue = np.array([40,255,255])

mask = cv2.inRange(hsvImage, lower_blue, upper_blue)

result = cv2.bitwise_and(image,image, mask = mask)

cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.imshow('Masked Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()