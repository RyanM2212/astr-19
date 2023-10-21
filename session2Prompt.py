# This program will print the sum of two floating point numbers, the difference between two integers, and the product of a floating point number and an integer.

# Gets input values from the user
floatNum1 = float(input("Enter a floating point number: "))
floatNum2 = float(input("Enter another floating point number: "))
intNum1 = int(input("Enter an integer: "))
intNum2 = int(input("Enter another integer: "))

# Calculates the sum of 2 floating point numbers
sum = floatNum1 + floatNum2
print("Sum:", sum)
print("Data Type:", type(sum))

# Calculates the difference between 2 integers
difference = intNum1 - intNum2
print("Difference:", difference)
print("Data Type:", type(difference))

# Calculate the product of a floating point number and an integer
product = floatNum1 * intNum1
print("Product:", product)
print("Data Type:", type(product))