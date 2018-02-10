import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

plt.ion()

class plotData:

    def __init__(self):
        self.rows = 4
        self.cols = 1

        self.fig, self.ax = plt.subplots(self.rows, self.cols, sharex=True)

        self.time_history = []
        self.xref_history = []
        self.yref_history = []
        self.x_history = []
        self.y_history = []
        self.theta_history = []
        self.phi_history = []

        self.handle = []
        self.handle.append(myPlot(self.ax[0], ylabel='x(m)', title='Platform Data'))
        self.handle.append(myPlot(self.ax[1], ylabel='y(m)'))
        self.handle.append(myPlot(self.ax[2], ylabel='theta(rad)'))
        self.handle.append(myPlot(self.ax[3], xlabel='t(s)', ylabel='phi(rad)'))

    def updatePlots(self, t, reference, states, ctrl):

        self.time_history.append(t)
        self.xref_history.append(reference[0])
        self.yref_history.append(reference[1])
        self.x_history.append(states[0])
        self.y_history.append(states[1])
        self.theta_history.append(ctrl[0])
        self.phi_history.append((ctrl[1]))

        self.handle[0].updatePlot(self.time_history, [self.x_history, self.xref_history])
        self.handle[1].updatePlot(self.time_history, [self.y_history, self.yref_history])
        self.handle[2].updatePlot(self.time_history, [self.theta_history])
        self.handle[3].updatePlot(self.time_history, [self.phi_history])

class myPlot:

    def __init__(self, ax, xlabel='', ylabel='', title='', legend=None):
        self.legend = legend
        self.ax = ax
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'b']
        self.line_styles = ['-', '-', '--', '-.', ':']
        self.line = []
        self.ax.set_ylabel(ylabel)
        self.ax.set_xlabel(xlabel)
        self.ax.set_title(title)
        self.ax.grid(True)
        self.init = True

    def updatePlot(self, time, data):
        if self.init == True:
            for i in range(len(data)):
                self.line.append(Line2D(time, data[i], \
                    color=self.colors[np.mod(i, len(self.colors)-1)], \
                    ls=self.line_styles[np.mod(i, len(self.line_styles) - 1)], \
                    label=self.legend if self.legend != None else None))
                self.ax.add_line(self.line[i])
            self.init = False
            if self.legend != None:
                plt.legend(handles=self.line)
        else:
            for i in range(len(self.line)):
                self.line[i].set_xdata(time)
                self.line[i].set_ydata(data[i])
        self.ax.relim()
        self.ax.autoscale()



