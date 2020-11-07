import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pow
nrows = 3
ncols=4
i=1
f=plt.figure()
# wczytanie obrazu
img = cv.imread('assets/board.jpg', 1)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
colored = img.copy()
sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(img)
sub.title.set_text('original')
#median
img2 = cv.medianBlur(img, 3)
sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(img2)
sub.title.set_text('median')
#gaussian

img3 = cv.GaussianBlur(img, (5,5), 1)
sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(img3)
sub.title.set_text('gaussian')
#convolution

kernel= np.array([[1,0], [0,1]])
img4 = cv.filter2D(img, -1, kernel)
sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(img4)
sub.title.set_text('convolution')
#binary
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)


kernel = np.ones((3,3), np.float32)/25


_, binary1= cv.threshold(img, 127, 255, cv.THRESH_BINARY)
sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(binary1,cmap='Greys_r')
sub.title.set_text('threshold')
#adaptive binary
binary2= cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 5, 15)
sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(binary2,cmap='Greys_r')
sub.title.set_text('adaptive thresh')
#diltion
dil = cv.dilate(binary1,kernel)
sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(dil,cmap='Greys_r')
sub.title.set_text('dilation')
#erosion
erode = cv.erode(binary1,kernel)
sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(erode,cmap='Greys_r')
sub.title.set_text('erosion')
#canny
edges = cv.Canny(img, 50, 600)
sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(edges,cmap='Greys_r')
sub.title.set_text('canny')
#affine transform
M = np.array([[1.5,0,50], [0,1.5,50]], dtype=np.float32)
transformed = cv.warpAffine(colored,M, (binary1.shape[1],binary1.shape[0]) )

sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(transformed)
sub.title.set_text('affine')

#finding points
contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cont = cv.drawContours(colored.copy(), contours, -1, (255,0,0), thickness=3)
sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(cont)
sub.title.set_text('contours')
c = contours[0]
print(c.shape, c[0][0][0], c[0][0][1])

left = c[np.argmin(c[:,0,0])][0]
rigth =c[np.argmax(c[:,0,0])][0]
up = c[np.argmin(c[:,0,1])][0]
down =c[np.argmax(c[:,0,1])][0]

#finding size of chesboard
def distance(x,y):
    return sqrt(pow((x[0]-y[0]), 2)+pow((x[1]- y[1]),2))

length = int(distance(left, up))
width = int(distance(left,down))

#perspective transform
source = np.float32([left, up, rigth, down])
destination = np.float32([[0,0],[0,width],[length,width],[length,0]])
M = cv.getPerspectiveTransform(source, destination)
warped = cv.warpPerspective(colored, M, (length, width))
sub = f.add_subplot(nrows, ncols, i)
i+=1
sub.imshow(warped)
sub.title.set_text('perspective')
# cv.imshow('perspective', warped)
# cv.waitKey(0)
plt.show()