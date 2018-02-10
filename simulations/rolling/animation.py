#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import params as P

class platformAnimation:

    def __init__(self):
        self.flagInit = True
        self.fig, self.ax = plt.subplots()
        self.handle = []

        plt.axis([-.25,.25,-.25,.25])
        plt.plot([-.2,.2,.2,-.2,-.2],[-.2,-.2,.2,.2,-.2],'b')


    def drawBall(self, u):

        x = u[0]
        y = u[1]
        self.ax.axis('equal')

        if self.flagInit == True:
            print("draw circle")
            self.handle.append(mpatches.CirclePolygon((x,y), radius = P.radius, \
                resolution = 15, fc = 'cyan', ec = 'black'))
            self.ax.add_patch(self.handle[0])
            self.flagInit = False
        else:
            self.handle[0]._xy=(x,y)

if __name__ == '__main__':

    debugAnimation = platformAnimation()

    x = 0.0
    y = 0.0
    debugAnimation.drawBall([x,y])
    debugAnimation.drawBall([x,y])
    plt.show()

    print('Press key to close')
    plt.waitforbuttonpress()
    plt.close()
