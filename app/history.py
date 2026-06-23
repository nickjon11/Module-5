import os
import pandas as pd


class Observer:
    def update(self, message):
        pass


class LoggerObserver(Observer):
    def update(self, message):
        print(f"LOG: {message}")


class History:

    FILE_NAME = "history.csv"

    def __init__(self):
        self.observers = []

        if os.path.exists(self.FILE_NAME):
            self.df = pd.read_csv(self.FILE_NAME)
        else:
            self.df = pd.DataFrame(
                columns=[
                    "a",
                    "b",
                    "operation",
                    "result"
                ]
            )

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def add_record(
        self,
        a,
        b,
        operation,
        result
    ):

        self.df.loc[len(self.df)] = [
            a,
            b,
            operation,
            result
        ]

        self.save(self.FILE_NAME)

        self.notify(
            f"{operation} performed"
        )

    def clear(self):

        self.df = pd.DataFrame(
            columns=[
                "a",
                "b",
                "operation",
                "result"
            ]
        )

        self.save(self.FILE_NAME)

    def save(self, filename):
        self.df.to_csv(
            filename,
            index=False
        )

    def load(self, filename):
        self.df = pd.read_csv(
            filename
        )