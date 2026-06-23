from app.calculation_memory import CalculationMemory


def test_memory_save_and_undo():
    memory = CalculationMemory()

    memory.save_state({"a": 1})
    memory.save_state({"a": 2})

    assert memory.undo() == {"a": 1}


def test_memory_redo():
    memory = CalculationMemory()

    memory.save_state({"a": 1})
    memory.save_state({"a": 2})

    memory.undo()
    assert memory.redo() == {"a": 2}


def test_memory_undo_empty():
    memory = CalculationMemory()
    assert memory.undo() is None or memory.undo() == {}


def test_memory_redo_empty():
    memory = CalculationMemory()
    assert memory.redo() is None or memory.redo() == {}