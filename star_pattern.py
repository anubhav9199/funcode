import turtle


def star(turtle, size):
    col = ('red', 'yellow', 'green', 'blue', 'white')
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.color(col[i])
            turtle.forward(size)
            star(turtle, size//3)
            turtle.left(216)
            turtle.end_fill()

def main():
    t = turtle.Turtle()
    t.getscreen().bgcolor("black")

    t.penup()
    t.goto(-200, 60)
    t.pendown()

    t.speed(1000)
    star(t, 360)
    turtle.done()

if __name__ == '__main__':
    main()