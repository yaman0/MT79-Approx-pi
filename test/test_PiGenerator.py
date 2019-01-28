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


def test_SerieInvCarresImparis_should_works(object):
    assert object.SerieInvCarresImparis(2) == 1.1511111111111112
    assert object.SerieInvCarresImparis(4) == 1.183864953388763


def test_SerieInvCarresImparis_with_negative_should_raise_value_error(object):
    with pytest.raises(ValueError):
        object.SerieInvCarresImparis(-1)


def test_MethodeSerieInvCarresImparis_should_works(object):
    assert object.MethodeSerieInvCarresImparis(50) == 3.135345271429545


def test_MethodeSerieInvCarresImparis_should_raise_value_error(object):
    with pytest.raises(ValueError):
        object.MethodeSerieInvCarresImparis(-1)


def test_SerieRamanujan_should_works(object):
    assert object.serieRamanujan(3) == 1103.0000268319745


def test_methodSerieRamanujan_should_work(object):
    assert object.methodSerieRamanujan(5) == 3.141592653589793


def test_tirage_should_return_array_with_10_length(object):
    result = object.tirage(10)
    assert len(result) == 10


def test_tirage_should_return_array_with_random_positions_between_0_and_1(object):
    for item in object.tirage(10):
        assert 0 < item[0] < 1
        assert 0 < item[1] < 1
