#CTI110
#P5T1 : Kilometer Converter
#Elianna Hunter
#4/1/2018

CONVERSION_FACTOR = 0.6214

def main():
    kilometers = float(input('Enter a distance in kilometers: '))
    
    show_miles(kilometers)

def show_miles(km):
    miles = km * CONVERSION_FACTOR
    
    print(km, 'kilometers equals', miles, 'miles.')

main()
