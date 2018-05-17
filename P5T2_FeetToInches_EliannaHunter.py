#CTI110
#This project is about converting feet to inches
#P5T2 : Feet to Inches
#Elianna Hunter
#4/1/2018

INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter a number of feet: '))

    print(feet, 'equals', feet_to_inches(feet), 'inches')
                     
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
