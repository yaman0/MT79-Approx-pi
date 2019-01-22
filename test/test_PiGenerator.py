import pytest

from src.PiGenerator import PiGenerator


@pytest.fixture()
def object():
    return PiGenerator()


def test_SerieInvCarres_should_works(object):
    assert object.SerieInvCarres(2) == 1.25
    assert object.SerieInvCarres(4) == 1.4236111111111112


def test_SerieInvCarres_with_negative_should_raise_value_error(object):
    with pytest.raises(ValueError):
        object.SerieInvCarres(-1)


def test_MethodeSerieInvCarres_should_works(object):
    assert object.MethodeSerieInvCarres(50) == 3.1226265229337264


def test_MethodeSerieInvCarres_should_raise_value_error(object):
    with pytest.raises(ValueError):
        object.MethodeSerieInvCarres(-1)