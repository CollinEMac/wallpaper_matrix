# OpenCV Project for 401CO
# Collin MacDonald
# Alejandro Ocanas
# Mulugeta Yirga

import numpy as np
import cv2

# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html
# http://nullege.com/codes/search?cq=opencv

img = cv2.imread('b.jpg',-1)				# reading the image, default folder to look for file is desktop
cv2.imshow('Original Image',img)			# displaying the original image in its own window

sectionA = img[0 : 300, 0:400]				# we used a matrix (4 x 3) to position where the pieces of our picture will appear
							# so that it will appear on screen just how the original image is
section1 = cv2.cvtColor(sectionA, cv2.COLOR_RGB2BGR)	# we shifted the RBG values of every other window
							# this way the windows will collectively dispay the image in a checkerboard pattern

section2 = img[300 : 600, 0:400]

sectionB = img[600 : 900, 0:400]
section3 = cv2.cvtColor(sectionB, cv2.COLOR_RGB2BGR)

section4 = img[0 : 300, 400:800]

sectionC = img[300 : 600, 400:800]
section5 = cv2.cvtColor(sectionC, cv2.COLOR_RGB2BGR)

section6 = img[600 : 900, 400:800]

sectionD = img[0 : 300, 800:1200]
section7 = cv2.cvtColor(sectionD, cv2.COLOR_RGB2BGR)

section8 = img[300 : 600, 800:1200]

sectionE = img[600 : 900, 800:1200]
section9 = cv2.cvtColor(sectionE, cv2.COLOR_RGB2BGR)

section10 = img[0 : 300, 1200:1600]

sectionF = img[300 : 600, 1200:1600]
section11 = cv2.cvtColor(sectionF, cv2.COLOR_RGB2BGR)

section12 = img[600 : 900, 1200:1600]

cv2.namedWindow('window1')
cv2.imshow('window1',section1) 				# displaying image
cv2.resizeWindow('window1', 400, 300)			# we resized all of the images to 400x300 pixels
cv2.moveWindow('window1', 0,0)				# positon of our first image, (will appear in the top left corner and then so on from there)

cv2.namedWindow('window2')
cv2.imshow('window2',section2)
cv2.resizeWindow('window2', 400, 300)
cv2.moveWindow('window2', 0,300)

cv2.namedWindow('window3')
cv2.imshow('window3',section3)
cv2.resizeWindow('window3', 400, 300)
cv2.moveWindow('window3', 0, 600)

cv2.namedWindow('window4')
cv2.imshow('window4',section4)
cv2.resizeWindow('window4', 400, 300)
cv2.moveWindow('window4', 400, 0)

cv2.namedWindow('window5')
cv2.imshow('window5',section5)
cv2.resizeWindow('window5', 400, 300)
cv2.moveWindow('window5', 400, 300)

cv2.namedWindow('window6')
cv2.imshow('window6',section6)
cv2.resizeWindow('window6', 400, 300)
cv2.moveWindow('window6', 400, 600)

cv2.namedWindow('window7')
cv2.imshow('window7',section7)
cv2.resizeWindow('window7', 400, 300)
cv2.moveWindow('window7', 800, 0)

cv2.namedWindow('window8')
cv2.imshow('window8',section8)
cv2.resizeWindow('window8', 400, 300)
cv2.moveWindow('window8', 800, 300)

cv2.namedWindow('window9')
cv2.imshow('window9',section9)
cv2.resizeWindow('window9', 400, 300)
cv2.moveWindow('window9', 800, 600)

cv2.namedWindow('window10')
cv2.imshow('window10',section10)
cv2.resizeWindow('window10', 400, 300)
cv2.moveWindow('window10', 1200, 0)

cv2.namedWindow('window11')
cv2.imshow('window11',section11)
cv2.resizeWindow('window11', 400, 300)
cv2.moveWindow('window11', 1200, 300)

cv2.namedWindow('window12')
cv2.imshow('window12',section12)
cv2.resizeWindow('window12', 400, 300)
cv2.moveWindow('window12', 1200, 600)

cv2.waitKey(0)						# display until a key is pressed
cv2.destroyAllWindows()					# close windows
