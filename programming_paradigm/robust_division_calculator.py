# programming_paradigm/robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Divide numerator by denominator with robust error handling.

    Returns one of:
      - "The result of the division is <value>"
      - "Error: Cannot divide by zero."
      - "Error: Please enter numeric values only."
    """
    # Convert inputs to numbers
    try:
        num = float(numerator)
        den = float(denominator)
    except (TypeError, ValueError):
        return "Error: Please enter numeric values only."

    # Perform the division
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
