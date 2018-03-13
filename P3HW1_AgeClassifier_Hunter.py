#CTI-110
#P3HW1 - Age Classifier
#Elianna Hunter
#2/28/2018

def main():
    print('Hello world')
    
main()
userAge = int(input("Please enter your age: "))
if userAge <= 1:
    print("You are an infant")
elif userAge < 13:
    print("You are a child")
elif userAge < 20:
    print("You are a teenager")
elif userAge >= 20:
    print("You are an adult")
