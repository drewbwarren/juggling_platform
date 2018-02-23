#! /usr/bin/env python

import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():
    img = cv2.imread('paperdot.png')
    
    ret, thresh = cv2.threshold(img,127,255,0)
    #plt.imshow(thresh),plt.show()
    
    
    lower = np.array([0,0,180])
    upper = np.array([255,100,255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    
    _, contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)    
    
    
    #contours = cv2.findContours(thresh,1,2)

    cnt = contours[1]
    #M = cv2.moments(cnt)
    #print M

    #cx = int(M['m10']/M['m00'])
    #cy = int(M['m01']/M['m00'])
    
    #area = cv2.contourArea(cnt)


    epsilon = 0.05*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    print approx[0][0][0]


    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
    plt.imshow(img),plt.show()


if __name__ == '__main__':
    main()
