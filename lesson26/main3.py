def reverse_bits(n):
    # Determine the number of bits in the given number
    num_bits = n.bit_length()
    
    # Reverse the bits
    reversed_n = 0
    for i in range(num_bits):
        if (n >> i) & 1:
            reversed_n |= (1 << (num_bits - 1 - i))
    
    return reversed_n

# Example usage
num = int(input("Enter a number: "))
reversed_num = reverse_bits(num)
print(f"Original number: {num}")
print(f"Reversed bits number: {reversed_num}")