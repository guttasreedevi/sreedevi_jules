# Python Calculator

A simple, beginner-friendly calculator application written in Python.

## Features

- **Basic Operations:** Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Advanced Operations:** Modulus (%), Power (^ or **)
- **Interactive Menu:** Run multiple calculations without restarting.
- **Error Handling:** Gracefully handles invalid inputs and prevents division by zero crashes.

## How to Run

Ensure you have Python installed on your system (Python 3 is recommended). No external libraries are needed.

1. Open a terminal or command prompt.
2. Navigate to the folder containing `calculator.py`.
3. Run the following command:

```bash
python calculator.py
```
*(On some systems, you might need to use `python3 calculator.py`)*

4. Follow the on-screen menu instructions to perform your calculations. Enter `7` to clear/exit the application.

## How to Run Tests

This project includes basic unit tests using Python's built-in `unittest` framework to ensure that mathematical operations are correct.

To run the tests:

1. Open a terminal or command prompt.
2. Navigate to the folder containing `test_calculator.py`.
3. Run the following command:

```bash
python -m unittest test_calculator.py
```
*(On some systems, you might need to use `python3 -m unittest test_calculator.py`)*
