import pytest

from app.operations import (
    Add,
    Subtract,
    Multiply,
    Divide,
    Power,
    Root,
    Modulus,
    IntegerDivide,
    Percentage,
    AbsoluteDifference,
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
    assert Modulus().execute(10, 3) == 1
    assert IntegerDivide().execute(10, 3) == 3
    assert Percentage().execute(25, 100) == 25
    assert AbsoluteDifference().execute(10, 25) == 15


def test_operation_factory():
    assert isinstance(OperationFactory.create("add"), Add)
    assert isinstance(OperationFactory.create("subtract"), Subtract)
    assert isinstance(OperationFactory.create("multiply"), Multiply)
    assert isinstance(OperationFactory.create("divide"), Divide)
    assert isinstance(OperationFactory.create("power"), Power)
    assert isinstance(OperationFactory.create("root"), Root)
    assert isinstance(OperationFactory.create("modulus"), Modulus)
    assert isinstance(OperationFactory.create("int_divide"), IntegerDivide)
    assert isinstance(OperationFactory.create("percent"), Percentage)
    assert isinstance(OperationFactory.create("abs_diff"), AbsoluteDifference)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Divide().execute(1, 0)


def test_modulus_by_zero():
    with pytest.raises(ZeroDivisionError):
        Modulus().execute(10, 0)


def test_integer_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        IntegerDivide().execute(10, 0)


def test_percentage_by_zero():
    with pytest.raises(ZeroDivisionError):
        Percentage().execute(10, 0)


def test_root_degree_zero():
    with pytest.raises(ValueError):
        Root().execute(9, 0)


def test_invalid_operation():
    with pytest.raises(InvalidOperationError):
        OperationFactory.create("banana")


def test_abstract_operation():
    with pytest.raises(TypeError):
        Operation()