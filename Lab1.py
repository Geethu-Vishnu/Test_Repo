
# Defining a function

def factorial(n):
    """Calculate the factorial of a non-negative integer n using recursion."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    try:
        number = int(input("Enter a non-negative integer to calculate its factorial: "))
        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"The factorial of {number} is {factorial(number)}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()