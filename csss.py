import turtle
def jump(n,x,y):
    n.penup()
    n.goto(x,y)
    n.pendown()
s=turtle.Screen()
s.bgcolor('powderblue')
t=turtle.Turtle()
a=turtle.Turtle()
b=turtle.Turtle()
a.pencolor('darkblue')
b.pencolor('green')
t.pencolor('green')
b.circle(100)
t.right(180)
t.circle(0)
