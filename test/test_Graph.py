import pytest

from src.Graph import Graph


@pytest.fixture()
def object():
    return Graph()


def test_showLegend_should_true_legend_boolean(object):
    object.showLegend()
    assert object.legend


def test_showLegend_should_return_self(object):
    result = object.showLegend()
    assert result == object


def test_addCircle1_should_true_legend_boolean(object):
    object.addCircle1()
    assert object.circle


def test_addCircle1_should_return_self(object):
    result = object.addCircle1()
    assert result == object


def test_setrange_should_self(object):
    result = object.setrange([0, 0], [0, 0])
    assert result == object

def test_setrange_should_add_good_range(object):
    x = [1,1]
    y = [0,3]
    object.setrange(x, y)
    assert object.range[0] == x
    assert object.range[1] == y
