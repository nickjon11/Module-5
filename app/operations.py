from abc import ABC, abstractmethod
from app.exceptions import InvalidOperationError


class Operation(ABC):

    @abstractmethod
    def execute(self, a, b):
        pass


class Add(Operation):

    def execute(self, a, b):
        return a + b


class Subtract(Operation):

    def execute(self, a, b):
        return a - b


class Multiply(Operation):

    def execute(self, a, b):
        return a * b


class Divide(Operation):

    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError(
                "Cannot divide by zero"
            )
        return a / b


class Power(Operation):

    def execute(self, a, b):
        return a ** b


class Root(Operation):

    def execute(self, a, b):
        if b == 0:
            raise ValueError("Root degree cannot be zero")
        return a ** (1 / b)


class OperationFactory:

    operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "power": Power,
        "root": Root,
    }

    @classmethod
    def create(cls, name):

        if name not in cls.operations:
            raise InvalidOperationError(name)

        return cls.operations[name]()