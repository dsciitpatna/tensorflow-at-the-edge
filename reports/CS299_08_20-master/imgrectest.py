from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import time
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
yellowLower = (1, 0, 255)
yellowUpper = (39, 155, 255)
yellowLower2 = (7, 117, 171)
yellowUpper2 = (48, 170, 255)
try:
	camera = cv2.VideoCapture(0)
except:
	print('nocam')
width = camera.get(3)
height = camera.get(4)
ratio = height/width
nw = 600
nwb = int(nw/2)
nh = nw * ratio
nhb = int(nh/2)
while True:
	ret, frame = camera.read()
	
	# cv2.line(frame,(300,0),(300,500),(255,0,0),5)
	frame = imutils.resize(frame, width=nw)
	# cv2.line(frame,(300,0),(300,500),(255,255,0),1)
	# cv2.line(frame,(0,nhb),(600,nhb),(255,255,0),1)
    # blurred = cv2.GaussianBlur(frame, (11, 11), 0) #blur to remove noise and retain structure
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, yellowLower2, yellowUpper2)
	mask = cv2.erode(mask, None, iterations=2) # dilations and erosions to remove any small blobs left in the mask
	mask = cv2.dilate(mask, None, iterations=2)

	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None

	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea) #max contor area
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		centerRel = (int(M["m10"] / M["m00"]) - nwb, -1 * (int(M["m01"] / M["m00"]) - nhb))
		print(centerRel)
		if radius > 5: #threshold sensitivity for drawing circle
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
		# break
		

	cv2.imshow("input", frame)

	key = cv2.waitKey(10)
	if key == 27:
		break

# (grabbed, frame) = camera.read()
# cv2.imshow("Frame", frame)
# time.sleep(10)
# frame = imutils.resize(frame, width=600)
# # blurred = cv2.GaussianBlur(frame, (11, 11), 0) #blur to remove noise and retain structure
# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert to the HSV color space

# # localization of the green ball 
# mask = cv2.inRange(hsv, greenLower, yellowUpper)
# mask = cv2.erode(mask, None, iterations=2) # dilations and erosions to remove any small blobs left in the mask
# mask = cv2.dilate(mask, None, iterations=2)
# # find contours in the mask and initialize the current
# # (x, y) center of the ball
# cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
#	 cv2.CHAIN_APPROX_SIMPLE)[-2]
# center = None
# cv2.imshow("Frame", frame)
# time.sleep(10)
# # only proceed if at least one contour was found
# if len(cnts) > 0:
#	 c = max(cnts, key=cv2.contourArea)
#	 ((x, y), radius) = cv2.minEnclosingCircle(c)
#	 M = cv2.moments(c)
#	 center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

#	 if radius > 5: #threshold sensitivity
#		 cv2.circle(frame, (int(x), int(y)), int(radius),
#			 (0, 255, 255), 2)
#		 cv2.circle(frame, center, 5, (0, 0, 255), -1)
	