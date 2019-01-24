import src.tools as tool


def test_roundless_should_works_for_float():
    number = 3.15879
    result = tool.roundless(number, 4)
    assert result == 3.1587


def test_roundless_should_works_for_int():
    number = 3.153
    result = tool.roundless(number, 0)
    assert result == 3
