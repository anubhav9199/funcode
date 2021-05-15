import turtle

col = ('red', 'yellow', 'green', 'blue', 'white')

t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor('black')

t.speed(30)

for i in range(150):
    t.color(col[i%5])
    t.forward(i*4)
    t.left(150)
    t.width(4)