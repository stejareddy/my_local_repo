def calculate_average(a, b, c):
    """Function to calculate the average of three numbers."""
    return (a + b + c) / 3

# Taking inputs from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calling the function and displaying the result
average = calculate_average(num1, num2, num3)
print(average)
