#! /usr/bin/env python

import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():
    img = cv2.imread('paperdot.png')
    rows, cols, ch = img.shape

    pts1 = np.float32([[92,380],[440,363],[345,141,],[98,136]])
    pts2 = np.float32([[0,300],[300,300],[300,0],[0,0]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    dst = cv2.warpPerspective(img,M,(300,300))

    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')

    #plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    main()
