from typing import Union

def perform_operation(num1: float, num2: float, operation: str) -> Union[float, str]:
    """
    Supported operations: 'add', 'subtract', 'multiply', 'divide' (case-insensitive).
    Returns a float result, or an error string the main.py can print.
    """
    op = (operation or "").strip().lower()

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
