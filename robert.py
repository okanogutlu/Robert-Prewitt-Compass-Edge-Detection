import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

GrayImage=cv2.imread('ImageTemplate.jpg',0) #Taking image from the file,making it gray tone.
h, w = GrayImage.shape #asigning the height and the width of the image to variables.
resultImage = np.zeros((h, w)) #creating a variable that will hold the result, size of it is [h][w]

V = np.array([[0, -1], [1, 0]]) #Robert mask for Vertical
H = np.array([[1, 0], [0, -1]]) #Robert mask for Horizontal

for i in range(1, h - 1):
    for j in range(1, w - 1):
        #applying the Horizontal mask to the Gray Image
        Hgrad = ((H[0, 0] * GrayImage[i, j]) +(H[0, 1] * GrayImage[i, j+1]) +\
        (H[1, 0] * GrayImage[i+1, j]) +(H[1, 1] * GrayImage[i+1, j+1]) )
        #applying the Vertical mask to the Gray Image
        Vgrad = ((V[0, 0] * GrayImage[i, j]) +(V[0, 1] * GrayImage[i, j+1]) +\
        (V[1, 0] * GrayImage[i +1, j]) +(V[1, 1] * GrayImage[i+1, j+1]) )
        
        mag = np.sqrt(pow(Hgrad, 2.0) + pow(Vgrad, 2.0))
        resultImage[i - 1, j - 1] = mag
#below shows the result to the user
plt.figure()
plt.title('RobertRESULT.png')
plt.imshow(resultImage, cmap='gray')
plt.show()