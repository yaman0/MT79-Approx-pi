from abc import abstractmethod


class View:
    def __init__(self):
        self.datas = []
        self.points = []

    def addData(self, data):
        """
        Add data to the viewer
        :param Data data: data to insert
        :return View: self
        """
        self.datas.append(data)
        return self

    def addPoints(self, points):
        """
        Add point to view
        :param list of Point points: points
        :return View: self
        """
        self.points.extend(points)
        return self

    @abstractmethod
    def view(self):
        """
        Display view
        """
        pass
