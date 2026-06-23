import pytest

import pytest

from app.operations import (
    Add,
    Subtract,
    Multiply,
    Divide,
    Power,
    Root,
    OperationFactory,
    Operation,
)

from app.exceptions import InvalidOperationError


def test_operations():
    assert Add().execute(1, 2) == 3
    assert Subtract().execute(5, 2) == 3
    assert Multiply().execute(3, 4) == 12
    assert Divide().execute(10, 2) == 5
    assert Power().execute(2, 3) == 8
    assert Root().execute(9, 2) == 3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Divide().execute(1, 0)


# NEW TESTS BELOW


def test_root_degree_zero():
    with pytest.raises(ValueError):
        Root().execute(9, 0)


def test_invalid_operation():
    with pytest.raises(InvalidOperationError):
        OperationFactory.create("banana")


def test_abstract_operation():
    with pytest.raises(TypeError):
        Operation()