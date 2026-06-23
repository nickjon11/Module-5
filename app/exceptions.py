class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass


class InvalidOperationError(CalculatorError):
    """Raised when an unsupported operation is used."""
    pass


class InvalidInputError(CalculatorError):
    """Raised when input validation fails."""
    pass