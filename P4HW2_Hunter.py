#CTI-110
#P4HW2: Running Total
#Elianna Hunter
#3/22/2018


total = 0
userNumber = float( input("Please enter the first number or a negative " + \
                          "number to quit: ") )

while userNumber > -1:
    total = total + userNumber
    userNumber = float( input("Please enter the next number or a negative " + \
                              "number to quit: " ) )
    print( "The sum of all the numbers you entered is", total )


    
