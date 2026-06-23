from app.operations import OperationFactory


class Calculator:

    def calculate(self, a, b, operation):

        strategy = OperationFactory.create(operation)

        return strategy.execute(a, b)