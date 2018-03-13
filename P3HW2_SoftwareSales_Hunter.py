#CTI-110
#P3HW2 - Software Sales
#Elianna Hunter
#2/28/2018

def main():
    print('Hello world')

main() 
userNumber0fPackages = int(input("Please enter the number of packages bought: "))
packagePrice = 99
if userNumber0fPackages < 10:
    discount = 0;
elif userNumber0fPackages < 20:
    discount = 0.10;
elif userNumber0fPackages < 50:
    discount = 0.20;
elif userNumber0fPackages < 100:
    discount = 0.30;
else:
    discount = 0.40;

subTotal = userNumber0fPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print ("\nAmount of discount: $" + format( discountAmount, ",.2f" ) + \
       "\nTotal amount: $" + format( total, ",.2f" ) )
    

