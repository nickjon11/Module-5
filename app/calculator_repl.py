from app.calculation import Calculator
from app.history import History, LoggerObserver
from app.input_validators import validate_number
from app.calculation_memory import CalculationMemory


def show_help():
    print("""
add a b
subtract a b
multiply a b
divide a b
power a b
root a b

history
save
load
undo
redo
clear
help
exit
""")


def repl(input_func=input, output_func=print):
    calculator = Calculator()

    # STEP 2: Create fresh objects here
    history = History()
    history.attach(LoggerObserver())

    memory = CalculationMemory()

    while True:
        command = input_func("> ").strip()

        if command == "exit":
            break

        if command == "help":
            show_help()
            continue

        if command == "history":
            output_func(history.df)
            continue

        if command == "clear":
            history.clear()
            output_func("History cleared")
            continue

        if command == "save":
            history.save("history.csv")
            output_func("Saved")
            continue

        if command == "load":
            history.load("history.csv")
            output_func("Loaded")
            continue

        if command == "undo":
            output_func(memory.undo())
            continue

        if command == "redo":
            output_func(memory.redo())
            continue

        try:
            operation, a, b = command.split()

            a = validate_number(a)
            b = validate_number(b)

            result = calculator.calculate(a, b, operation)

            history.add_record(a, b, operation, result)

            memory.save_state({
                "a": a,
                "b": b,
                "operation": operation,
                "result": result
            })

            output_func(result)

        except Exception as e:
            output_func(e)

def main():
    print("Calculator V4 Project")
    print("Type 'help' for a list of commands.")
    repl()


if __name__ == "__main__":
    main()