from abc import ABC

import matplotlib.pyplot as plt

from src.View import View


class Graph(View, ABC):
    def __init__(self):
        super(Graph, self).__init__()
        self.legend = False

    def showLegend(self):
        """
        enable the legends when you render graph
        :return Graph: Self
        """
        self.legend = True
        return self

    def view(self):
        """
        Display view
        """
        for data in self.datas:
            plt.plot(data.data, label='{}'.format(data.label))
        for point in self.points:
            plt.scatter(point.x, point.y, s=point.size, c=point.color)
        if self.legend:
            plt.legend()
        plt.show()
