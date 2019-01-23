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
