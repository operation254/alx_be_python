# Requires Python 3.10+ for match/case

def _read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")

num1 = _read_number("Enter the first number: ")
num2 = _read_number("Enter the second number: ")
op = input("Choose the operation (+, -, *, /): ").strip()

result_text = None

match op:
    case "+":
        res = num1 + num2
        result_text = res
    case "-":
        res = num1 - num2
        result_text = res
    case "*":
        res = num1 * num2
        result_text = res
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            res = num1 / num2
            result_text = res
    case _:
        print("Unknown operation.")

if result_text is not None:
    if isinstance(result_text, float) and result_text.is_integer():
        print(f"The result is {int(result_text)}.")
    else:
        print(f"The result is {result_text}.")
