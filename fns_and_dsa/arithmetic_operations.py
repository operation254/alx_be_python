"""
Arithmetic operations helper for main.py.

Function:
    perform_operation(num1: float, num2: float, operation: str) -> float | str
"""

def perform_operation(num1: float, num2: float, operation: str):
    """Return the result of add/subtract/multiply/divide on num1 and num2.
    On divide-by-zero return the message 'Error: Division by zero'.
    On invalid operation return 'Error: Invalid operation'.
    """
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
