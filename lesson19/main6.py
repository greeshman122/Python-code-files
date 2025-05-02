def ONSquareTime(n):
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
print("O(n²)")