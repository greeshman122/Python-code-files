#Program to find two numbers that are odd occurring
def printTwoOdd(arr , size):

    #xorof2 will hold 2 odd occurring numbers
    xorof2 = arr[0]
    x = 0
    y = 0

    #This will hold the rightmost set bot from xorof2
    Set bit = 0

    for i in range(1 , size):
        xorof2 = xorof2 ^ arr[i]

    setbit = xorof2 & ~(xo)