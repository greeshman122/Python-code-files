l1 = input("Enter any 3 digit numbers : ")
print("The original number is : " , l1)
r1 = l1[::-1]
print("The reversed number is : " , r1)
if l1 == r1 :
    print("The entered number is palindrome ")
else :
    print("The entered number is not a palindrome")