# Function to convert binary to decimal
def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Function to perform basic binary operations
def binary_operations(num1, num2):
    num1_bin = bin(num1)[2:]  # Convert to binary string
    num2_bin = bin(num2)[2:]

    print(f"Binary of {num1}: {num1_bin}")
    print(f"Binary of {num2}: {num2_bin}")

    print(f"Addition: {bin(num1 + num2)[2:]}")
    print(f"Subtraction: {bin(num1 - num2)[2:]}")
    print(f"Multiplication: {bin(num1 * num2)[2:]}")
    print(f"Bitwise AND: {bin(num1 & num2)[2:]}")
    print(f"Bitwise OR: {bin(num1 | num2)[2:]}")
    print(f"Bitwise XOR: {bin(num1 ^ num2)[2:]}")


# Example usage
binary_str = input("Enter a binary number: ")
decimal_value = binary_to_decimal(binary_str)
print(f"Decimal equivalent: {decimal_value}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
binary_operations(num1, num2)
