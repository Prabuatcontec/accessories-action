

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


# Open the camera
cap = cv2.VideoCapture(0)
# Set initial value of weights


wi, ht = list(pyautogui.size())[0], list(pyautogui.size())[1]

keys = np.array([[70,125,150,250, 'Q'], 
              [165,125,245,250, 'W'], 
              [265,125,345,250, 'E'], 
              [365,125,445,250, 'R'], 
              [463,125,543,250, 'T'], 
              [561,125,641,250, 'Y'], 
              [659,125,739,250, 'U'], 
              [757,125,837,250, 'I'], 
              [855,125,935,250, 'O'], 
              [952,125,1032,250, 'P'], 
              [115,270,190,390, 'A'], 
              [210,270,295,390, 'S'], 
              [310,270,395,390, 'D'], 
              [410,270,495,390, 'F'], 
              [510,270,595,390, 'G'], 
              [610,270,695,390, 'H'], 
              [710,270,795,390, 'J'], 
              [811,270,896,390, 'K'], 
              [912,270,996,390, 'L'], 
              [65,410,160,530, 'Caps'], 
              [175,410,255,530, 'Z'], 
              [270,410,350,530, 'X'], 
              [365,410,445,530, 'C'], 
              [460,410,540,530, 'V'], 
              [555,410,635,530, 'B'], 
              [650,410,730,530, 'N'], 
              [745,410,825,530, 'M'], 
              [840,410,920,530, '$'], 
              [935,410,1035,530, 'Clear'], 
              [65,560,160,680, 'Number'], 
              [175,560,270,680, '.'], 
              [285,560,810,680, 'Space'], 
              [825,560,160,920, '!?'], 
              [935,560,1030,680, 'Enter'], 
              [1060,0,1100,40, 'Keyboard']])

    



lol = 0
vop = None
detector= htm.handDetector(detectionCon=0.75)
while True:
    
    # read the background
    ret, background = cap.read()
    background=cv2.resize(background,(1350,950))
    background = cv2.flip(background,1)
    background = detector.findHands(background)
    background = detector.findPosition(background, keys)
    blurred = cv2.GaussianBlur(background, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
 
    


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
