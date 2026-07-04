import os
import logging
from datetime import datetime

import pandas as pd

from app.calculator_config import Config


class Observer:
    def update(self, message):
        pass


class LoggingObserver(Observer):

    def __init__(self):
        log_dir = Config.get_log_dir()
        os.makedirs(log_dir, exist_ok=True)

        log_path = os.path.join(log_dir, Config.get_log_file())

        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def update(self, message):
        logging.info(message)


class LoggerObserver(LoggingObserver):
    pass


class AutoSaveObserver(Observer):

    def __init__(self, history):
        self.history = history

    def update(self, message):
        if Config.get_auto_save():
            self.history.save(self.history.file_name)


class History:

    COLUMNS = [
        "a",
        "b",
        "operation",
        "result",
        "timestamp",
    ]

    FILE_NAME = Config.get_history_file()

    def __init__(self, filename=None):
        self.observers = []
        self.file_name = filename or self.FILE_NAME

        if os.path.exists(self.file_name):
            try:
                self.df = pd.read_csv(self.file_name)

                for column in self.COLUMNS:
                    if column not in self.df.columns:
                        self.df[column] = ""

                self.df = self.df[self.COLUMNS]

            except pd.errors.ParserError:
                self.df = pd.DataFrame(columns=self.COLUMNS)
        else:
            self.df = pd.DataFrame(columns=self.COLUMNS)

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def add_record(self, a, b, operation, result):
        self.df.loc[len(self.df)] = [
            a,
            b,
            operation,
            result,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ]

        max_size = Config.get_max_history_size()

        if len(self.df) > max_size:
            self.df = self.df.tail(max_size).reset_index(drop=True)

        self.notify(f"{operation} performed with {a} and {b}. Result: {result}")

    def clear(self):
        self.df = pd.DataFrame(columns=self.COLUMNS)
        self.save(self.file_name)

    def save(self, filename):
        self.df.to_csv(filename, index=False)

    def load(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"History file not found: {filename}")

        self.df = pd.read_csv(filename)

        for column in self.COLUMNS:
            if column not in self.df.columns:
                self.df[column] = ""

        self.df = self.df[self.COLUMNS]