# Function to compute LCM
def compute_lcm(x, y):
    # Finding the greater number
    greater = max(x, y)

    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

# User input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Compute LCM
lcm = compute_lcm(num1, num2)

print(f"The LCM of {num1} and {num2} is {lcm}")
