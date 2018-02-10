#!/usr/bin/env python

import params as P
from PDControl import PDControl

class platformController:

    def __init__(self):
        self.xCtrl = PDControl(P.kp, P.kd, P.theta_max, P.beta, P.Ts)
        self.yCtrl = PDControl(P.kp, P.kd, P.phi_max, P.beta, P.Ts)

    def u(self, ref, state):
        # ref is the input
        # state is the current state

        x_r = ref[0]
        x = state[0]
        y_r = ref[1]
        y = state[1]

        theta = self.xCtrl.PD(x_r, x, flag=False)
        phi = self.yCtrl.PD(y_r, y, flag=False)

        return [theta, phi]
