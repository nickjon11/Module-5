from app.exceptions import InvalidInputError


def validate_number(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        raise InvalidInputError(
            f"Invalid numeric value: {value}"
        )