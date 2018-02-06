#!/usr/bin/evn python
import numpy as np
import param as P
import random

class platformDynamics:

    def __init__(self):
        # Initial states
        self.state = np.matrix([[P.x0],[P.y0],[P.theta0],[P.phi0],[P.xdot0],[P.ydot0],[P.thetadot0],[P.phidot0]])
        
        alpha = 0.1 # uncertainty parameter
        self.m = .0027 * (1+2*alpha*np.random.rand()-alpha)
        self.g = 9.81
        

    def propagateDynamics(self,u):
        # Integrate ODE using RK4
        k1 = self.derivatives(self.state,u)
        k2 = self.derivatives(self.state + P.Ts/2*k1,u)
        k3 = self.derivatives(self.state + P.Ts/2*k2,u)
        k4 = self.derivatives(self.state + P.Ts*k3,u)
        self.state += P.Ts/6 * (k1 + 2*k2 + 2*k3 + k4)


    def derivatives(self,state,u):
        '''
            Return xdot = f(x,u), the derivatives of the continuous states, as a matrix
        '''
        # Relabel states
        x = state.item(0)
        y = state.item(1)
        theta = state.item(2)
        phi = state.item(3)
        xdot = state.item(4)
        ydot = state.item(5)
        thetadot = state.item(6)
        phidot = state.item(7)
        tau1 = u(0)
        tau2 = u(1)

        # Equations of motion
        xddot = -self.g*theta
        yddot = -self.g*phi
        thetaddot = -self.g/x
        phiddot = -self.g/y

        return np.matrix([[xdot],[ydot],[thetadot],[phidot],[xddot],[yddot],[thetaddot],[phiddot]])

    def outputs(self):
        x = state.item(0)
        y = state.item(1)
        theta = state.item(2)
        phi = state.item(3)
        xdot = state.item(4)
        ydot = state.item(5)
        thetadot = state.item(6)
        phidot = state.item(7)
        return [x,y,theta,phi]

    def states(self):
        return self.state.T.tolist()[0]



