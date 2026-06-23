Module 5 - Calculator V4 Project - Enhanced Calculator Applications

The project is a command-line calculator in Python, much like Module 2-5. New additions are an History feature to store completed calculations

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
git clone <module-5 link>
cd module-5

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
