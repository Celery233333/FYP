import cv2
import numpy as np


sample_img = cv2.imread("123.jpg", cv2.IMREAD_UNCHANGED)

try:
    if sample_img.shape[2] == 4:     # we have an alpha channel
        a1 = ~sample_img[:,:,3]        # extract and invert that alpha
        sample_img = cv2.add(cv2.merge([a1,a1,a1,a1]), sample_img)   # add up values (with clipping)
        sample_img = cv2.cvtColor(sample_img, cv2.COLOR_RGBA2RGB)    # strip alpha channel
        sample_img = cv2.cvtColor(sample_img, cv2.COLOR_RGB2GRAY)
    elif sample_img.shape[2] == 3:   # no alpha channel (musicma_abaro)
        sample_img = cv2.cvtColor(sample_img, cv2.COLOR_RGB2GRAY) 
except IndexError: # 2d image
    print("ggggggggggggggggggg")
    pass
h = int(sample_img.shape[0]*0.5)
w = int(sample_img.shape[1]*0.5)
sample_img = cv2.resize(sample_img,(w,h))
sample_img = cv2.adaptiveThreshold(sample_img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,33,16)
kernel = np.ones((3,3),np.uint8)  
sample_img = cv2.dilate(sample_img,kernel,iterations = 1)
sample_img = cv2.erode(sample_img,kernel,iterations = 1)
sample_img = cv2.GaussianBlur(sample_img, (5, 5), 0) 
sample_img = cv2.bilateralFilter(sample_img,5,75,75)
sample_img = cv2.medianBlur(sample_img, 3)
cv2.imshow("q",sample_img)
cv2.waitKey()