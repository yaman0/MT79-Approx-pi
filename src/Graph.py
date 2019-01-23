from abc import ABC

from src.View import View
import matplotlib.pyplot as plt


class Graph(View, ABC):
    def __init__(self):
        super(Graph, self).__init__()

    def view(self):
        for data in self.datas:
            plt.plot(data)
        plt.show()
