def is_armstrong(number):
    # Convert the number to a string to get the number of digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate the sum of the digits each raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum of the powers is equal to the original number
    return sum_of_powers == number

# Example usage
number = 153
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
