try:
    from colorama import Fore, Style, init
except ImportError:
    class Fore:
        GREEN = ""
        RED = ""
        YELLOW = ""

    class Style:
        RESET_ALL = ""

    def init(autoreset=True):
        pass

from app.calculation import Calculator
from app.history import History, LoggingObserver, AutoSaveObserver
from app.input_validators import validate_number
from app.calculation_memory import CalculationMemory
from app.calculator_config import Config

init(autoreset=True)


def show_help():
    print("""
Available commands:

Replace a with a number, Replace b with a number.

Operations:

add a b
subtract a b
multiply a b
divide a b
power a b
root a b
modulus a b
int_divide a b
percent a b
abs_diff a b
          
Commands:

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

    history = History()
    history.attach(LoggingObserver())
    history.attach(AutoSaveObserver(history))

    memory = CalculationMemory()

    while True:
        command = input_func("> ").strip()

        if command == "exit":
            output_func(Fore.YELLOW + "Have a nice day" + Style.RESET_ALL)
            break

        if command == "help":
            show_help()
            continue

        if command == "history":
            output_func(history.df)
            continue

        if command == "clear":
            history.clear()
            output_func(Fore.YELLOW + "History cleared" + Style.RESET_ALL)
            continue

        if command == "save":
            history.save(Config.get_history_file())
            output_func(Fore.GREEN + "Saved" + Style.RESET_ALL)
            continue

        if command == "load":
            history.load(Config.get_history_file())
            output_func(Fore.GREEN + "Loaded" + Style.RESET_ALL)
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
            result = round(result, Config.get_precision())

            history.add_record(a, b, operation, result)

            memory.save_state({
                "a": a,
                "b": b,
                "operation": operation,
                "result": result,
            })

            output_func(Fore.GREEN + str(result) + Style.RESET_ALL)

        except Exception as e:
            output_func(Fore.RED + str(e) + Style.RESET_ALL)


def main():
    print("Calculator Midterm Project")
    print("Type 'help' for a list of commands.")
    repl()


if __name__ == "__main__":
    main()