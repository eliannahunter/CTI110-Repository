#CTI-110
#P4LAB: Nested Loops
#Elianna Hunter
#3/22/2018


import turtle
wn = turtle.Screen()
t = turtle.Turtle()

t.pensize(4)
t.pencolor("pink")
t.shape("turtle")

t.left(180)

for i in (1,2,3,4,5):
    for j in (1,2,3,4):
        t.forward(90)
        t.right(90)
    t.forward(100)
    t.left(73)


