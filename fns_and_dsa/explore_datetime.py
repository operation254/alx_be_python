from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days: int):
    future_date = datetime.now() + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

if __name__ == "__main__":
    display_current_datetime()
    try:
        days = int(input("Enter the number of days to add to the current date: ").strip())
    except ValueError:
        print("Invalid number. Please enter an integer.")
    else:
        calculate_future_date(days)
