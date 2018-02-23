#! /usr/bin/env python

import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():
    img = cv2.imread('paperdot.png')
    
    # All of this finds the corners
    lower = np.array([0,0,180])
    upper = np.array([255,100,255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower,upper)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    
    # check for the right contour
    r_max = 0
    for c in contours:
        _, radius = cv2.minEnclosingCircle(c)
        if radius > r_max:
            r_max = radius
            cnt = c
    epsilon = 0.04*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    approx = approx.tolist()
    


    print [approx[0][0],approx[1][0],approx[2][0],approx[3][0]]
    
    # This stuff takes the corners and reprojects the image
    #pts1 = np.float32([[92,380],[440,363],[345,141,],[98,136]])
    pts1 = np.float32([approx[0][0],approx[1][0],approx[2][0],approx[3][0]])
    #pts2 = np.float32([[0,30*11],[255,30*11],[255,0],[0,0]])
    pts2 = np.float32([[0,0],[0,30*11],[255,30*11],[255,0]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    dst = cv2.warpPerspective(img,M,(255,30*11))

    # View the image
    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')
    plt.show()


if __name__ == '__main__':
    main()
