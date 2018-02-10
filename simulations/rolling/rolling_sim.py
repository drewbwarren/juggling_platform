#!/usr/bin/env python

import matplotlib.pyplot as plt
import params as P
from dynamics import platformDynamics
from controller import platformController
from animation import platformAnimation
from plotData import plotData
from signalGenerator import signalGenerator


### Dynamics
platform = platformDynamics()

### Controller
ctrl = platformController()
dataPlot = plotData()

### Reference
def step(time, k):
    if time < 1.0:
        return 0
    else:
        return k
reference = signalGenerator(amplitude=0.1, frequency=0.1)

### Plots and Animation
animate = platformAnimation()

t = P.t_start
while t < P.t_end:

    # Get the reference input from reference
    x_ref = reference.sin(t) #step(t,.05)
    y_ref = reference.cos(t) #step(t,-.1)
    x_ref = x_ref[0]
    y_ref = y_ref[0]

    # Propogate dynamics inbetween plot samples
    t_next_plot = t + P.t_plot

    while t < t_next_plot: # update control and dynamics at faster simulation rate
        u = ctrl.u([x_ref,y_ref], platform.outputs())
        platform.propagateDynamics(u)
        t = t + P.Ts

    # Update animation
    animate.drawBall(platform.states())
    dataPlot.updatePlots(t,[x_ref,y_ref],platform.states(),u)
    plt.pause(0.0001)

print('Press key to close')
plt.waitforbuttonpress()
plt.close()
