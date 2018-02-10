#!/usr/bin/evn python
import numpy as np
import params as P
import random

class platformDynamics:

    def __init__(self):
        # Initial states
        self.state = np.matrix([[P.x0],[P.y0],[P.xdot0],[P.ydot0]])

        alpha = 0.1 # uncertainty parameter
        self.m = .0027 * (1+2*alpha*np.random.rand()-alpha)
        self.g = 9.81


    def propagateDynamics(self,u):
        # Integrate ODE using RK4
        k1 = self.derivatives(self.state,u)
        k2 = self.derivatives(self.state + P.Ts/2*k1,u)
        k3 = self.derivatives(self.state + P.Ts/2*k2,u)
        k4 = self.derivatives(self.state + P.Ts*k3,u)
        self.state += (P.Ts/6) * (k1 + 2*k2 + 2*k3 + k4)


    def derivatives(self,state,u):
        '''
            Return xdot = f(x,u), the derivatives of the continuous states, as a matrix
        '''
        # Relabel states
        x = state.item(0)
        y = state.item(1)
        xdot = state.item(2)
        ydot = state.item(3)
        theta = u[0]
        phi = u[1]

        # Equations of motion
        xddot = self.g*theta
        yddot = self.g*phi

        return np.matrix([[xdot],[ydot],[xddot],[yddot]])

    def outputs(self):
        x = self.state.item(0)
        y = self.state.item(1)
        xdot = self.state.item(2)
        ydot = self.state.item(3)
        return [x,y]

    def states(self):
        return self.state.T.tolist()[0]



