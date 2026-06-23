from app.calculator_repl import repl


def run_repl(commands):
    """
    Helper to simulate REPL input sequence safely.
    """
    inputs = iter(commands)
    repl(input_func=lambda _: next(inputs))


# -------------------------
# CORE COMMAND TESTS
# -------------------------

def test_repl_exit():
    run_repl(["exit"])


def test_repl_help():
    run_repl(["help", "exit"])


def test_repl_history():
    run_repl(["history", "exit"])


def test_repl_clear():
    run_repl(["clear", "exit"])


def test_repl_save_load():
    run_repl(["save", "load", "exit"])


def test_repl_undo_redo():
    run_repl(["undo", "redo", "exit"])


# -------------------------
# CALCULATION PATH
# -------------------------

def test_repl_add_operation():
    run_repl(["add 1 2", "exit"])


def test_repl_subtract_operation():
    run_repl(["subtract 5 2", "exit"])


def test_repl_multiply_operation():
    run_repl(["multiply 3 4", "exit"])


def test_repl_divide_operation():
    run_repl(["divide 10 2", "exit"])


# -------------------------
# EDGE / ERROR PATH
# -------------------------

def test_repl_invalid_command():
    run_repl(["bad input here", "exit"])


def test_repl_missing_args():
    run_repl(["add 1", "exit"])


def test_repl_empty_command_handling():
    run_repl(["", "exit"])