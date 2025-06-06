def logic_circuit_bitwise(A, B, C):
    # Convert boolean values to binary (1 for True, 0 for False)
    A, B, C = int(A), int(B), int(C)

    # Perform bitwise operations
    and1 = A & B
    and2 = B & C
    or1 = A | C
    and3 = or1 & and2

    # Final output using bitwise OR
    Q = and1 | and3

    return Q

# Example usage
A = True  # Input A
B = False # Input B
C = True  # Input C

output = logic_circuit_bitwise(A, B, C)
print(f"The output Q is: {output}")
