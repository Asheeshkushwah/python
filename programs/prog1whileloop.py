number = int(input("Enter a number to generate its multiplication table: "))

multiplier = 1

while multiplier <= 10:
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
    multiplier += 1