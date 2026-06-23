from app.calculator_config import Config

def test_get_history_file():

    assert isinstance(
        Config.get_history_file(),
        str
    )