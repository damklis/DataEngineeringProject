import pytest

from ..fixtures import add_function


def test_retry_on_exception_valid(add_function):
    expected = 2

    result = add_function(1, 1)

    assert result == expected


def test_retry_on_exception_wrong(add_function):

    with pytest.raises(TypeError):
        add_function("Test", 0.0001)
