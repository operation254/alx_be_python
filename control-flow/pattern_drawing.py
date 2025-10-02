size_str = input("Enter the size of the pattern: ").strip()
try:
    size = int(size_str)
except ValueError:
    print("Please enter a positive integer.")
    raise SystemExit(0)

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()
    row += 1
