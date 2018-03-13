#CTI-110
#P3T1 - Areas Of Rectangles
#Elianna Hunter
#2/28/2018

def main():
    print('Hello world')

main()
length1 = int(input('Enterr the length of rectangle 1: '))
width1 = int(input('Enter the width of the rectangle 1: '))

length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print("Rectangle 1 has the greater area. ")
else:
    if area2 > area1:
        print("Rectangle 2 has the greater area.")
    else:
        prnit("Both have the same area.")
