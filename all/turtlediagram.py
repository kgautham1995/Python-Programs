#pip install  turtle

import turtle
a=turtle.Screen()
turtle.speed(20)
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()