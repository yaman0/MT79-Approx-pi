import pytest

from src.Data import Data
from src.Point import Point
from src.View import View


@pytest.fixture()
def object():
    return View()


def test_addData_must_return_self(object):
    data = Data([1, 2, 3])
    result = object.addData(data)
    assert result == object


def test_addData_must_be_insert_data(object):
    data = Data([1, 2, 3])
    object.addData(data)
    assert len(object.datas) == 1
    assert object.datas[0] == data


def test_addPoints_must_return_self(object):
    data = [Point(1, 2), Point(1, 3)]
    result = object.addPoints(data)
    assert result == object


def test_addPoints_must_be_insert_data(object):
    data = [Point(1, 2), Point(1, 3)]
    object.addPoints(data)
    assert len(object.points) == 2
    assert object.points[0] == data[0]
