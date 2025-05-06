import inspect

def track_recursion(func):
    def wrapper(*args):
        print(f"Recurrence relation: {func.__name__}({', '.join(map(str, args))})")
        return func(*args)
    return wrapper

@track_recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@track_recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# Test cases
print(f"Factorial: {factorial(5)}")
print(f"Fibonacci: {fibonacci(5)}")
