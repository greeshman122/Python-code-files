def swap1(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After Swapping : a = " , a , "b = " , b)
swap1(98 , 48)
print("Bitwise Operators")


def swap2(a,b):
    a = (a & b) + ( a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print("\nAfter swapping : a = ", a , "b = " , b)
swap2(22 , 38)
print("Arithematic Operators")