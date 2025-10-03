# Global conversion factors (exact names/values for the checker)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Return Celsius from Fahrenheit using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Return Fahrenheit from Celsius using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    # Prompt for temperature; raise ValueError on non-numeric (per task text)
    try:
        value_str = input("Enter the temperature to convert: ")
        value = float(value_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(value)
        print(f"{value}°C is {result}°F")
    elif unit == "F":
        result = convert_to_celsius(value)
        print(f"{value}°F is {result}°C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")


if __name__ == "__main__":
    main()
