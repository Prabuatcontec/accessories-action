
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
              [935,410,1015,530, 'Clear'], 
              [65,560,160,680, 'Number'], 
              [175,560,270,680, '.'], 
              [285,560,810,680, 'Space'], 
              [825,560,160,920, '!?'], 
              [935,560,1030,680, 'Enter']])

    



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
    background = detector.mouseAction(background, keys)
    blurred = cv2.GaussianBlur(background, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
    # mask = cv2.inRange(hsv, greenLower, greenUpper)
    # mask = cv2.erode(mask, None, iterations=2)
    # mask = cv2.dilate(mask, None, iterations=2)
	# # find contours in the mask and initialize the current
	# # (x, y) center of the ball
    # cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
    # cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    # center = None
    # # cv2.rectangle(background, (110, 270), (190, 395), (0, 255, 0), 3) 
    # if len(cnts) > 0:
    #     # find the largest contour in the mask, then use
    #     # it to compute the minimum enclosing circle and
    #     # centroid
    #     c = max(cnts, key=cv2.contourArea)
    #     ((x, y), radius) = cv2.minEnclosingCircle(c)
    #     M = cv2.moments(c)
    #     center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    #     # only proceed if the radius meets a minimum size
    #     if radius > 5:
    #     # draw the circle and centroid on the frame,
    #     # then update the list of tracked points
    #         cv2.rectangle(background,(int(x-50),int(y-50)),(int(x+50),int(y+50)),(255,0,0),2)
    #         # cv2.circle(background, (int(x), int(y)), int(radius),
    #         # (0, 255, 255), 2)
    #         cv2.circle(background, center, 5, (0, 0, 255), -1)
    #         pts.appendleft(center)
    #         for key in keys :
    #             if(x > int(key[0]) and y > int(key[1]) and x < int(key[2]) and y < int(key[3]) ):
    #                 if(vop != None and lol>30):
    #                     print(str(key[4]))
    #                     lol = 0
    #                     vop = None
    #                 vop = str(key[4])
    #                 lol = lol + 1
                
            
    # Select the region in the background where we want to add the image and add the images using cv2.addWeighted()
    #added_image = cv2.addWeighted(background[50:750,50:1050,:],alpha,foreground[0:700,0:1000,:],1-alpha,0)
    # Change the region with the result
    #background[50:750,50:1050] = added_image
    # For displaying current value of alpha(weights)
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