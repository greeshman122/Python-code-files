def multiply_once(n, m):
    """Multiply N by M in a single iteration"""
    return n * m

def multiply_n_times(n, m):
    """Multiply N by M using N iterations"""
    result = 0
    for _ in range(n):
        result += m
    return result

N = 5
M = 4

print("Multiplication in one iteration:", multiply_once(N, M))
print("Multiplication in N iterations:", multiply_n_times(N, M))