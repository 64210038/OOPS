from turtle import Turtle
from random import randint

#create object

leo = Turtle()
leo.color('blue')
leo.shape('turtle')
leo.penup()
leo.goto(-160,100)
leo.pendown()

dona = Turtle()
dona.color('purple')
dona.shape('turtle')
dona.penup()
dona.goto(-160,70)
dona.pendown()


raps = Turtle()
raps.color('red')
raps.shape('turtle')
raps.penup()
raps.goto(-160,40)
raps.pendown()

mike = Turtle()
mike.color('orange')
mike.shape('turtle')
mike.penup()
mike.goto(-160,10)
mike.pendown()


for movement in range(100):
    leo.forward(randint(1,5))
    dona.forward(randint(1,5))
    raps.forward(randint(1,5))
    mike.forward(randint(1,5))

endp = input("Press Enter to close")
print("End")
