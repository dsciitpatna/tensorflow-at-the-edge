# sudo modprobe bcm2835-v4l2
#import necessary libraries
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
# import RPi.GPIO as GPIO
import time
import serial


#def errlog(code):
    #placeholder for error handler

#initialize motor gpios, servo gpios, camera, usonicsensors, etc
ser = serial.Serial('/dev/ttyACM0', 9600)
#0 stop
#1 forward
#2 backward
#3 clk
#4 aclk
#5 servo 1 low
#6 servo 1 high
#7 servo claw hold
#8 servo claw release
#9 read distance
#https://github.com/jrosebr1/imutils/blob/master/bin/range-detector
#image processing init
greenLower = (40, 75, 72)
greenUpper = (170, 184, 255)
yellowLower = (1, 0, 255)
yellowUpper = (39, 155, 255)

# if a video path was not supplied, grab the reference
# to the webcam
try:
    camera = cv2.VideoCapture(0)
except:
    errlog(1)#cam error

def reachedObject():
    ser.write(7)
    dist = 0
    while 1 :
        dist = int(ser.readline())
        if dist:
            break
    return (dist>50 and dist <100)

#scan for object in one frame
def findColRange(colLow, colHigh):
    width = camera.get(3)
    height = camera.get(4)
    ratio = height/width
    nw = 600
    nwb = int(nw/2)
    nh = nw * ratio
    nhb = int(nh/2)
    whCnt = 0
    prevX =0
    prevY =0
    #stac = np.empty(0)
    while whCnt<50:
        whCnt += 1
        ret, frame = camera.read()
        # cv2.line(frame,(300,0),(300,500),(255,0,0),5)
        frame = imutils.resize(frame, width=nw)
        # cv2.line(frame,(300,0),(300,500),(255,255,0),1)
        # cv2.line(frame,(0,nhb),(600,nhb),(255,255,0),1)
        # blurred = cv2.GaussianBlur(frame, (11, 11), 0) #blur to remove noise and retain structure
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, greenLower, greenUpper)
        mask = cv2.erode(mask, None, iterations=2) # dilations and erosions to remove any small blobs left in the mask
        mask = cv2.dilate(mask, None, iterations=2)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        if whCnt <2:
            continue
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea) #max contor area
            x1,y1,w1,h1 = cv2.boundingRect(cnt)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            centerRel = (int(M["m10"] / M["m00"]) - nwb, int(M["m01"] / M["m00"]) - nhb,radius)
            print(centerRel)
            print(radius)
            print("w: "+str(w1)+" h: "+str(h1))
            if radius > 15: #threshold sensitivity for drawing circle
                cv2.circle(frame, (int(x), int(y)), int(radius),
                    (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
                return centerRel
            elif radius < 15:
                return False
        else:
            if whCnt > 50:
                return False
        #cv2.imshow("input", frame)
        #key = cv2.waitKey(10)
        #if key == 27:
        #    break


#clkw rotation till detects green object
  #while no green object detected, rotate clockwise
  #if detected stop rotation
#steps of 5 seconds
objCoord = False
while True:
    objCoord = findColRange(greenLower,greenUpper)
    if objCoord == False:
        ser.write('3')
        time.sleep(1)
        ser.write('0')
        time.sleep(1)
    else:
        if objCoord[0] < 10:
            print('lessthan')
            ser.write('3')
            time.sleep(0.5)
        elif objCoord[0] > 10:
            print('gtthan')
            ser.write('4')
            time.sleep(0.5)
        print('found object')
        print(objCoord)
        print(objCoord[0])
        print(objCoord[1])
        ser.write('1')
        time.sleep(1)
    if objCoord[2] < 50:
        print('reached')
        break
#find green object coordinates

#align

#aligning and centering object
# if objCoord != False:
#     #ser.write('0')
#     while objCoord[0] > 10 or objCoord[0] < -10:
#     objCoord = findColRange(greenLower,greenUpper)
#     print(objCoord)
      

camera.release()
cv2.destroyAllWindows()
  
#lower arm wrap arm around the object
  #lower the arm such that claw is around the object
  #close the claw


pwm.start(5)
 
angle1=10
duty1= float(angle1)/10 + 2.5               ## Angle To Duty cycle  Conversion
 
angle2=160
duty2= float(angle2)/10 + 2.5
 
ck=0
while ck<=5:
     pwm.ChangeDutyCycle(duty1)
     time.sleep(0.8)
     pwm.ChangeDutyCycle(duty2)
     time.sleep(0.8)
     ck=ck+1
time.sleep(1)

#lift arm
  #lift the arm at the same height as before

#clkw rotaton till detects yellow base
  #while no yellow base detected, rotate clockwise
  #if detected stop rotation
baseCoord = False
while True:
    clkrot()
    sleep(5)
    stopbot()
    baseCoord = findColRange(yellowLower,yellowUpper)
    if baseCoord == False:
        continue
    else:
        break

if baseCoord != False:
    while baseCoord[0] > 15 or baseCoord[0] < -15:
        if baseCoord[0] < 0:
            cclkrot()
            sleep(1)
        elif baseCoord[0] > 0:
            clkrot()
            sleep(1)

#goes towards yellow base
  #once in direction of base, move in a straight line towards the base
  #stop when at a specific distance from the centre of the base
if baseCoord != False and baseCoord[0] < 5 and baseCoord[0] > -5:
    fwd()
#ultrasonic distance threshold

    # stopbot()

#lowers arm and opens claw
  #lower the arm such that object touches the base
  #open the claw

#lifts the arm
  #lift the arm at the same height as before

camera.release()
cv2.destroyAllWindows()
