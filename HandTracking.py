import cv2
import mediapipe as mp 
import time 
import pyautogui
import time
import random as rnd
from pynput.mouse import Button, Controller
import math
import numpy as np



class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.vop = None
        self.lol = 0
        self.mouse=Controller()
        self.camx = 350
        self.camy = 350
        self.wi = list(pyautogui.size())[0]
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.myOldLoc = np.array([0,0])
        self.myLocation = np.array([0,0])
        self.du = 2
        self.action = 0
        self.ht = list(pyautogui.size())[1]
        self.text = ''
        self.foreground = cv2.imread('keyboard.jpg')
        self.keyboard = cv2.imread('keyboard.png')
        self.alpha = 0.6
        self.keyboardon = 0

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw = False):
        imgRGB = cv2.cvtColor(img, 1)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, None)
        return img

    def findPosition(self, img, keys):
        cv2.putText(img, f'Msg: {self.text}',
                                    (10,30), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),3 )
        if self.keyboardon == 1:
            added_image = cv2.addWeighted(img[50:750,50:1050,:],self.alpha,self.foreground[0:700,0:1000,:],1-self.alpha,0)
            # Change the region with the result
            img[50:750,50:1050] = added_image
        added_image = cv2.addWeighted(img[0:40,1060:1100,:],self.alpha,self.keyboard[0:40,0:40,:],1-self.alpha,0)
        img[0:40,1060:1100] = added_image
        
        imgRGB = cv2.cvtColor(img, 1)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    x, y = int(lm.x*w), int(lm.y*h)
                    # pyautogui.moveTo(x,x)
                    if id ==8:
                        #print(str(h) +"===" +str(w))
                        cv2.circle(img, (x,y), 10, (255,0,255), cv2.FILLED)
                        for key in keys :
                            if(x > int(key[0]) and y > int(key[1]) and x < int(key[2]) and y < int(key[3]) ):
                                
                                if(self.vop == str(key[4])):
                                    self.lol = self.lol + 1
                                else:
                                    self.lol = 0


                                
                                if(self.vop != None and self.lol==20):
                                    cv2.rectangle(img, (int(key[0]), int(key[1])), (int(key[2]), int(key[3])), (0, 255, 0), 3) 
                                    if ( str(key[4]) == 'Space' ) : 
                                        key[4] = ' '
                                    elif ( str(key[4]) == 'Clear' ) :
                                        self.text =  self.text.rstrip(self.text[-1])
                                    elif (str(key[4]) == 'Keyboard'):
                                        if self.keyboardon == 0:
                                            self.keyboardon = 1
                                        else :
                                            self.keyboardon = 0
                                    else :
                                        self.text = self.text+str(key[4])

                                    self.lol = 0
                                    self.vop = None
                                self.vop = str(key[4])
            

        return img

    def mouseAction(self, img):
        imgRGB = cv2.cvtColor(img, 1)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    x, y = int(lm.x*w), int(lm.y*h)
                    
                    # if id == 8 or id == 4:
                    #     self.action = 0
                    if id == 8:
                        self.x1, self.y1 = int(lm.x*w), int(lm.y*h)
                        #cv2.circle(img, (self.x1,self.y1), 10, (255,0,255), cv2.FILLED)
                    if id==4:
                        self.x2, self.y2 = int(lm.x*w), int(lm.y*h)
                        #cv2.circle(img, (self.x2,self.y2), 10, (255,0,0), cv2.FILLED)
                    
                    if self.x1 > 0 and self.y1 > 0 and self.x2 > 0 and self.y2 > 0:
                        #cv2.line(img, (self.x1,self.y1),(self.x2,self.y2),(255,255,0),2)
                        cx=(self.x1+self.x2)/2
                        cy=(self.y1+self.y2)/2
                        cv2.circle(img, (int(cx),int(cy)),2,(0,0,255),2)
                        loc = self.myOldLoc + ((cx,cy) - self.myOldLoc)/self.du
                        mouseLoc=(self.wi-(cx*self.wi/self.camx), cy*self.ht/self.camy)
                        self.mouse.position=mouseLoc 
                        dis = distance = math.sqrt( ((self.x1-self.x2)**2)+((self.y1-self.y2)**2) )
                        # print('999999999999999999999999999999999999999')
                        print(int(dis))
                        print(self.action)
                        if self.action == 1 and int(dis) > 70:
                            print('Release')
                            self.action = 0
                            self.mouse.release(Button.left)
                        if(int(dis) < 40 and self.action==0):
                            print('click')
                            self.mouse.press(Button.left)
                            self.action = 1

                        
                            

        return img

        
