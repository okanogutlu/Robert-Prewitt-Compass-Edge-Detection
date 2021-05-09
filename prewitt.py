import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

grayImage = cv2.imread("ImageTemplate.jpg",0) #Taking image from file
cv2.imshow("grayImage2",grayImage) # showing gray image to the user

h, w = grayImage.shape #assigning height and width of the image to h&w
H = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])  #Robert mask for Horizontal
V = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])  #Robert mask for Vertical

result = np.zeros((h, w)) #creating a variable that will hold the result, size of it is [h][w]

for i in range(1, h - 1):
    for j in range(1, w - 1):
        #applying mask to the gray image.
        Hgrad = (H[0, 0] * grayImage[i - 1, j - 1])+(H[0, 1] * grayImage[i - 1, j])+\
                (H[0, 2] * grayImage[i - 1, j + 1])+(H[1, 0] * grayImage[i, j - 1]) + \
                (H[1, 1] * grayImage[i, j]) +(H[1, 2] * grayImage[i, j + 1]) +\
                (H[2, 0] * grayImage[i + 1, j - 1]) +(H[2, 1] * grayImage[i + 1, j]) + \
                (H[2, 2] * grayImage[i + 1, j + 1])

        Vgrad = (V[0, 0] * grayImage[i - 1, j - 1]) +(V[0, 1] * grayImage[i - 1, j]) +(V[0, 2] * grayImage[i - 1, j + 1]) +(V[1, 0] * grayImage[i, j - 1]) + \
                       (V[1, 1] * grayImage[i, j]) +(V[1, 2] * grayImage[i, j + 1]) +(V[2, 0] * grayImage[i + 1, j - 1]) +(V[2, 1] * grayImage[i + 1, j]) + \
                       (V[2, 2] * grayImage[i + 1, j + 1])

        temp = np.sqrt(pow(Hgrad, 2.0) + pow(Vgrad, 2.0))
        result[i - 1, j - 1] = temp

#below shows the result to the user
plt.figure()
plt.title('prewittRESULT')
plt.imshow(result, cmap='gray')
plt.show()