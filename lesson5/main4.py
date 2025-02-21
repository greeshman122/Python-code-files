# Function to generate Fibonacci series up to n terms
def fibonacci_series(n):
    fib_sequence = [0, 1]
    
    # Generate Fibonacci series
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence

# Take input from the user
n = int(input("Enter the number of terms: "))

# Ensure valid input
if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci_series(n)
    print(f"Fibonacci series up to {n} terms: {result}")
