
import cv2
import numpy as np
import imutils
from collections import deque
import HandTracking as htm
import pyautogui
import time
import random as rnd

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=32)
counter = 0
(dX, dY) = (0, 0)
direction = ""
# create an overlay image. You can use any image
foreground = cv2.imread('keyboard.jpg')

# Open the camera
cap = cv2.VideoCapture(0)
# Set initial value of weights
alpha = 0.6



lol = 0
vop = None
detector= htm.handDetector(detectionCon=0.75)
while True:
    # pyautogui.moveTo(rnd.randrange(0, wi), 
    #                  rnd.randrange(0, ht))#, duration = 0.1)
    # read the background
    ret, background = cap.read()
    #background=cv2.resize(background,(1150,950))
    background=cv2.resize(background,(350,350))
    background = cv2.flip(background,1)
    background = detector.findHands(background)
    background = detector.mouseAction(background)
    blurred = cv2.GaussianBlur(background, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    #cv2.putText(background,'alpha:{}'.format(alpha),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
 
    


    cv2.imshow('a',background)

    
    k = cv2.waitKey(10)
    # Press q to break
    if k == ord('q'):
        break
    # press a to increase alpha by 0.1
    if k == ord('a'):
        alpha +=0.1
        if alpha >=1.0:
            alpha = 1.0
    # press d to decrease alpha by 0.1
    elif k== ord('d'):
        alpha -= 0.1
        if alpha <=0.0:
            alpha = 0.0
# Release the camera and destroy all windows         
cap.release() 
