from app.exceptions import InvalidInputError
from app.calculator_config import Config


def validate_number(value):
    try:
        number = float(value)
    except (ValueError, TypeError):
        raise InvalidInputError(f"Invalid numeric value: {value}")

    max_value = Config.get_max_input_value()

    if abs(number) > max_value:
        raise InvalidInputError(
            f"Input value is too large. Maximum allowed value is {max_value}"
        )

    return number