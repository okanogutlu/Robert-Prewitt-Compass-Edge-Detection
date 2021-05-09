import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2


grayImage = cv2.imread("ImageTemplate.jpg",0) #Taking image from file
cv2.imshow("grayImage2",grayImage)# showing gray image to the user

h, w = grayImage.shape #assigning height and width of the image to h&w
Result = np.zeros((h, w)) #creating an array of zeros, size is [h][w]
degree0 = np.array([[-1, -1, -1], [+1, -2, 1], [1, 1, 1]])  #asigning Compass 0Degree masking to the variable.
degree45 = np.array([[-1, -1, 1], [-1, -2, 1], [1, 1, 1]])  #asigning Compass 45Degree masking to the variable.
degree90 = np.array([[-1, 1, 1], [-1, -2, 1], [-1, 1, 1]])  #asigning Compass 90Degree masking to the variable.
degree135 = np.array([[1, 1, 1], [-1, -2, 1], [-1, -1, 1]]) #asigning Compass 135Degree masking to the variable.
degree180 = np.array([[1, 1, 1], [1, -2, 1], [-1, -1, -1]]) #asigning Compass 180Degree masking to the variable.
degree225 = np.array([[1, 1, 1], [1, -2, -1], [1, -1, -1]]) #asigning Compass 225Degree masking to the variable.
degree270 = np.array([[1, 1, -1], [1, -2, -1], [1, 1, -1]]) #asigning Compass 270Degree masking to the variable.
degree315 = np.array([[1, -1, -1], [1, -2, -1], [1, 1, 1]]) #asigning Compass 315Degree masking to the variable.


def ImageG(grayImage,mask,i,j): #this function is used to apply the mask to the gray image.
  return    (mask[0, 0] * grayImage[i - 1, j - 1]) +(mask[0, 1] * grayImage[i - 1, j]) +(mask[0, 2] * grayImage[i - 1, j + 1]) +\
            (mask[1, 0] * grayImage[i, j - 1]) + (mask[1, 1] * grayImage[i, j]) +(mask[1, 2] * grayImage[i, j + 1]) +\
            (mask[2, 0] * grayImage[i + 1, j - 1]) +(mask[2, 1] * grayImage[i + 1, j]) + (mask[2, 2] * grayImage[i + 1, j + 1])
    



for i in range(1, h - 1):
    for j in range(1, w - 1):
       
        Result[i - 1, j - 1] = max(abs(ImageG(grayImage,degree0,i,j)),abs(ImageG(grayImage,degree45,i,j)), #Maximum of the masking result asigning to Result array.
            abs(ImageG(grayImage,degree90,i,j)),abs(ImageG(grayImage,degree135,i,j)),
            abs(ImageG(grayImage,degree180,i,j)),abs(ImageG(grayImage,degree225,i,j)),
            abs(ImageG(grayImage,degree270,i,j)),abs(ImageG(grayImage,degree315,i,j))) 
     

#Below shows the result to the user
plt.figure()
plt.title('compassRESULT')
plt.imshow(Result, cmap='gray')
plt.show()