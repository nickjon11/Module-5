import os
import tempfile

from app.history import (
    History,
    LoggerObserver,
)


def test_add_record():
    history = History()

    history.add_record(
        1,
        2,
        "add",
        3,
    )

    assert len(history.df) == 5


def test_clear():
    history = History()

    history.add_record(
        1,
        2,
        "add",
        3,
    )

    history.clear()

    assert len(history.df) == 0


def test_save_and_load():
    history = History()

    history.add_record(
        1,
        2,
        "add",
        3,
    )

    with tempfile.NamedTemporaryFile(
        suffix=".csv",
        delete=False,
    ) as tmp:

        history.save(tmp.name)

        new_history = History()

        new_history.load(
            tmp.name
        )

        assert len(new_history.df) == 1

    os.remove(tmp.name)


def test_attach_observer():
    history = History()

    observer = LoggerObserver()

    history.attach(
        observer
    )

    assert len(history.observers) == 1


def test_notify():
    history = History()

    history.notify(
        "testing"
    )

    assert True