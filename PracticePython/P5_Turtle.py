# Ref.: Head First Learn To Code
# Turtle

import turtle
import time
slowpoke = turtle.Turtle()
slowpoke.fillcolor('#008080')
slowpoke.shape('turtle')

time.sleep(2)
slowpoke.right(3*360)

slowpoke.right(90)
slowpoke.pencolor('White')
slowpoke.forward(85)
slowpoke.pencolor('green')
slowpoke.forward(215)
slowpoke.pencolor('black')
slowpoke.left(90)
slowpoke.forward(300)
slowpoke.left(90)
slowpoke.forward(600)
slowpoke.left(90)
slowpoke.forward(600)
slowpoke.left(90)
slowpoke.forward(600)
slowpoke.left(90)
slowpoke.forward(300)
slowpoke.left(90)
slowpoke.pencolor('green')
slowpoke.forward(215)
slowpoke.pencolor('White')
slowpoke.forward(85)

slowpoke.pencolor('#FF1493')
for i in range(48):
    slowpoke.forward(i)
    slowpoke.right(360/(pow(i+1,1/2)*2))
for i in range(7):
    slowpoke.forward(48-i)
    slowpoke.right(360/(pow((48-i),1/2)*2))
#slowpoke.right(40)
#slowpoke.pencolor('white')
slowpoke.right(10)
slowpoke.forward(12)
slowpoke.pencolor('white')
slowpoke.left(85)
slowpoke.forward(91)
slowpoke.pencolor('green')

for i in range(22):
    slowpoke.forward(i)
    slowpoke.right(360/(pow(i+1,1/3)*40))
slowpoke.right(130)
for i in range(22):
    slowpoke.forward(21-i)
    slowpoke.right(360/(pow(22-i,1/3)*40))
slowpoke.left(165)
slowpoke.forward(72)

slowpoke.pencolor('#008080')
slowpoke.right(3*360+180)
turtle.mainloop()