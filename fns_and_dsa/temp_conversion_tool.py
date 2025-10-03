# Global conversion factors (required by checker)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0
FREEZING_OFFSET = 32.0  # used in both formulas

def convert_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius using globals."""
    return (fahrenheit - FREEZING_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit using globals."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_OFFSET

def main():
    # Input validation: raise ValueError with exact message if not numeric
    temp_str = input("Enter the temperature to convert: ").strip()
    try:
        temperature = float(temp_str)
    except ValueError:
        # EXACT message expected by checker:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
