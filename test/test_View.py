import pytest

from src.PiGenerator import PiGenerator
from src.View import View


@pytest.fixture()
def object():
    return View()


def test_addData_must_return_self(object):
    list = [1, 2, 3]
    result = object.addData(list)
    assert result == object


def test_addData_must_be_insert_list(object):
    list = [1, 2, 3]
    object.addData(list)
    assert len(object.datas) == 1
    assert object.datas[0] == list
