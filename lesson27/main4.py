def is_power_of_8(n):
    if n <= 0:
        return False

    # Check if n is a power of 2
    if (n & (n - 1)) != 0:
        return False

    # Check if the only set bit is at a position that is a multiple of 3
    count = 0
    while n > 1:
        n >>= 1
        count += 1

    return count % 3 == 0

# Test cases
print(is_power_of_8(8))      # True
print(is_power_of_8(64))     # True
print(is_power_of_8(512))    # True
print(is_power_of_8(32))     # False
print(is_power_of_8(10))     # False