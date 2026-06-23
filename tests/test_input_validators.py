import pytest

from app.input_validators import (
    validate_number
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