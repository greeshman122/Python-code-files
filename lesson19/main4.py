#ist activity
'''def printnumber(n):
    iteration=0
    print("The number entered by user is " , n)
    iteration+=1
    print("Total iterations done by the code is " , iteration , "\n")

printnumber(10)
printnumber(20)
print("\n With any 'n' the time taken by our code wont change")'''

#2nd activity
'''def OnTime(n):
    iteration = 0
    for i in range(1, n+1):
        iteration += 1
    print("When n is", n, "Iterations =", iteration)

OnTime(10)
OnTime(20)
OnTime(42)'''

#3rd activity
'''def ONSquareTime(n):
    iteration=0
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
            iteration += 1
        print("")
    print("\nWhen n is", n, "Iterations =", iteration, "\n")

ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)

print("\nWith every 'n', the time taken equals n²")
print("O(n²)")'''