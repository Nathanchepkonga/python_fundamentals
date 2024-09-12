# calculate_factorial.py

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

# Test the function
if __name__ == "__main__":
    print(calculate_factorial(5))  # Output: 120
