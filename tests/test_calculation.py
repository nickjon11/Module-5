import pytest

from app.calculation import (
    Calculator
)

calculator = Calculator()

@pytest.mark.parametrize(
    "a,b,op,expected",
    [
        (1,2,"add",3),
        (5,3,"subtract",2),
        (4,5,"multiply",20),
        (10,2,"divide",5),
        (2,3,"power",8)
    ]
)
def test_calculator(
    a,
    b,
    op,
    expected
):

    assert (
        calculator.calculate(
            a,
            b,
            op
        )
        == expected
    )