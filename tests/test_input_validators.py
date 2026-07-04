import pytest

from app.input_validators import (
    validate_number
)

from app.exceptions import (
    InvalidInputError
)

def test_valid_number():

    assert (
        validate_number("5")
        == 5.0
    )

def test_invalid_number():

    with pytest.raises(
        Exception
    ):
        validate_number("abc")

def test_value_too_large():

    with pytest.raises(
        InvalidInputError
    ):
        validate_number("999999999999999999999")