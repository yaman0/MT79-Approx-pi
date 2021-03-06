from abc import ABC

import matplotlib.pyplot as plt
import numpy as np

from src.View import View


class Graph(View, ABC):
    def __init__(self):
        super(Graph, self).__init__()
        self.legend = False
        self.range = None
        self.circle = None

    def showLegend(self):
        """
        enable the legends when you render graph
        :return Graph: self
        """
        self.legend = True
        return self

    def addCircle1(self):
        """
        add a circle witch radius=1 in the circle
        :return Graph: self
        """
        self.circle = True
        return self

    def setrange(self, xrange, yrange):
        """
        set a specifi range of view
        :param list xrange: x range
        :param list yrange: y range
        :return Graph: self
        """
        self.range = [xrange, yrange]
        return self

    def view(self):
        """
        Display view
        """
        for data in self.datas:
            if data.type == 'point':
                plt.plot(data.data, 'o', label='{}'.format(data.label))
            else:
                plt.plot(data.data, label='{}'.format(data.label))
        for point in self.points:
            plt.scatter(point.x, point.y, s=point.size, c=point.color)

        if self.circle:
            theta = np.linspace(0, 2 * np.pi, 40)
            x = np.cos(theta)
            y = np.sin(theta)
            plt.plot(x, y)

        if self.legend:
            plt.legend()

        if self.range is not None:
            plt.axis([self.range[0][0], self.range[0][1], self.range[1][0], self.range[1][1]])
        plt.show()
