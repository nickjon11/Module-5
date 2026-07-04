Module 6 - Calculator V5 Project - Midterm Project Enhhanced Command-Line Application

The project is an extension of Module 5 calculator applications. It continues using the command-line REPL calculator developed in modules 2-5 while expanding the project with additional arithmetic operations, improved configuration management, better history management, and better error handling.

Compared to Module 5, this version adds more mathematical operations, see below, timestamped calculation history, configurable application settings using a `.env` file, improved logging, and additional input validation while keeping the Factory, Memento, and Observer design patterns introduced in Module 5

The ability to save and load history using CSV files

Implemented undo and redo functions using the memory feature

All Features:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Calculation History
6. Save History to CSV
7. Load History from CSV
8. Input Validation

Installation Instructions:
git clone <midterm_module_6 link> 
cd midterm_module_6

Activate a virtual environment:
python -m venv .venv
source .venv/bin/activate

Install Dependencies:
pip install -r requirements.txt

Run the Program:
python -m app.calculator_repl
exit to end the program

Running Tests:
python -m pytest --cov=app --cov-report=term-missing
