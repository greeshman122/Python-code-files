def longest_consecutive_ones(n):
    max_count = 0
    count = 0

    while n > 0:
        if n & 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
        n >>= 1
    return max_count

# Example usage
num = int(input("Enter a number: "))
result = longest_consecutive_ones(num)
print(f"The longest sequence of consecutive 1’s is: {result}")