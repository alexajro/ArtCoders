import cv2 as cv
import numpy as np

# Read image.
img = cv.imread('Photos/lady.jpeg')

# Convert to grayscale.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15)

for (x,y,w,h) in faces_rect:
    rect = cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    #cv.imshow('rect', rect)

# Cropping an image
cropped_image = img[y:y+h, x:x+w]
gray2 = cv.cvtColor(cropped_image, cv.COLOR_BGR2GRAY)

# Blur using 3 * 3 kernel.
gray_blurred = cv.blur(gray2, (3, 3))


#Set up the detector with default parameters
detector = cv.SimpleBlobDetector_create()


#Detect blobs
keypoints = detector.detect(gray_blurred)

#print(keypoints) --> si le damos print son direcciones se tienen que acceder de alguna forma ahí y así que se vaya comparando

#Draw detected blobs as red circles
# cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv.drawKeypoints(cropped_image, keypoints, np.array([]), (0,225,0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


#Show keypoints
cv.imshow("Keypoints", im_with_keypoints)

cv.waitKey(0)
