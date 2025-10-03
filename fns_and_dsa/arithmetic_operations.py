def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation.
    operation: 'add' | 'subtract' | 'multiply' | 'divide'
    Returns the numeric result, or an error string the caller can display.
    """
    operation = (operation or "").strip().lower()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
