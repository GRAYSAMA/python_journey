#Create a function to calculate the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1  #factorial of 0 and 1 is always 1
    return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

# factorial(5) → 5 * factorial(4)
# factorial(4) → 4 * factorial(3)
# factorial(3) → 3 * factorial(2)
# factorial(2) → 2 * factorial(1) = 2 * 1
# factorial(1) → 1 * factorial(0) = 1
