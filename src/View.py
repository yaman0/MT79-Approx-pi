from abc import abstractmethod


class View:
    def __init__(self):
        self.datas = []

    def addData(self, data):
        """
        Add data to the viewer
        :param Data data: data to insert
        :return View: self
        """
        self.datas.append(data)
        return self

    @abstractmethod
    def view(self):
        """
        Display view
        """
        pass
