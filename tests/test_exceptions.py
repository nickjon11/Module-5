from app.exceptions import (
    CalculatorError,
    InvalidInputError,
    InvalidOperationError
)

def test_exceptions():

    assert issubclass(
        InvalidInputError,
        CalculatorError
    )

    assert issubclass(
        InvalidOperationError,
        CalculatorError
    )