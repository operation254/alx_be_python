FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (float(fahrenheit) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

if __name__ == "__main__":
    raw_temp = input("Enter the temperature to convert: ").strip()
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    try:
        temp_val = float(raw_temp)
    except ValueError as e:
        raise ValueError("Invalid temperature. Please enter a numeric value.") from e

    if unit == "F":
        c = convert_to_celsius(temp_val)
        print(f"{temp_val}°F is {c}°C")
    elif unit == "C":
        f = convert_to_fahrenheit(temp_val)
        print(f"{temp_val}°C is {f}°F")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
