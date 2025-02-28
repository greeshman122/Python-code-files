import random
print('guess a number between 1 to 10')
n = int(input('gussed number'))
cg = random.randint(1,10)
if n == cg:
    print('You got it right')
else:
    print('You got it wrong')

print('The right number is ' , cg)