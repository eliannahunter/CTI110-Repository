#CTI-110
#P4HW3: Factorial
#Elianna Hunter
#3/22/2018


userInteger = int( input("Please enter a number: ") )

while userInteger < 1:
    userInteger = int( input( "Please enter a positive number please: ") )

factorial = 1

for currentNumber in range( 1, userInteger + 1 ):
    factorial = factorial * currentNumber
    print()
    print("The factorial of", userInteger, "is", factorial )
