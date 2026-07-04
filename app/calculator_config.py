import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    @staticmethod
    def get_history_file():
        return os.getenv("CALCULATOR_HISTORY_FILE", "history.csv")

    @staticmethod
    def get_log_file():
        return os.getenv("CALCULATOR_LOG_FILE", "calculator.log")

    @staticmethod
    def get_log_dir():
        return os.getenv("CALCULATOR_LOG_DIR", ".")

    @staticmethod
    def get_history_dir():
        return os.getenv("CALCULATOR_HISTORY_DIR", ".")

    @staticmethod
    def get_max_history_size():
        return int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))

    @staticmethod
    def get_auto_save():
        return os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"

    @staticmethod
    def get_precision():
        return int(os.getenv("CALCULATOR_PRECISION", "2"))

    @staticmethod
    def get_max_input_value():
        return float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1000000"))

    @staticmethod
    def get_default_encoding():
        return os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")