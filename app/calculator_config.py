import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    @staticmethod
    def get_history_file():

        filename = os.getenv(
            "HISTORY_FILE",
            "history.csv"
        )

        if not filename:
            raise ValueError(
                "History file not configured"
            )

        return filename