def firstSetBit(n):
    if n == 0:
        return "No set bit found"
    
    count = 1
    while n:
        if n & 1 == 1:
            return 1 << (count - 1)  # Returns the number corresponding to the rightmost set bit
        count += 1
        n >>= 1
    
    return "No set bit found"

# Example usage
number = int(input("Enter a number: "))
rightmost_set_bit = firstSetBit(number)
print(f"The rightmost set bit (as a number) is: {rightmost_set_bit}")
