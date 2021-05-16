import turtle
from letter_utils import letter
import random

INITIAL_x = -200
INITIAL_y = 60

letter_function_map = {
    'A': letter.a_function,
    'B': letter.b_function,
    'C': letter.c_function,
    'D': letter.d_function,
    'E': letter.e_function,
    'F': letter.f_function,
    'G': letter.g_function,
    'H': letter.h_function,
    'I': letter.i_function,
    'J': letter.j_function,
    'K': letter.k_function,
    'L': letter.l_function,
    'M': letter.m_function,
    'N': letter.n_function,
    'O': letter.o_function,
    'P': letter.p_function,
    'Q': letter.q_function,
    'R': letter.r_function,
    'S': letter.s_function,
    'T': letter.t_function,
    'U': letter.u_function,
    'V': letter.v_function,
    'W': letter.w_function,
    'X': letter.x_function,
    'Y': letter.y_function,
    'Z': letter.z_function,
}


def name(turtle, name):
    col = ('red', 'yellow', 'green', 'blue', 'white')
    _names = list(name.split(" "))
    for _name in _names:
        for letter in _name:
            turtle.color(col[random.randint(0, 4)])
            letter_function_map[letter.upper()](turtle, letter)
            turtle.penup()
            turtle.left(90)
            turtle.forward(15)
            turtle.left(90)
            turtle.pendown()
        turtle.penup()
        y = INITIAL_y - 60
        turtle.goto(INITIAL_x, y)
        turtle.pendown()


def main():
    n = input("Enter the name here : ")
    t = turtle.Turtle()
    t.getscreen().bgcolor("black")
    t.color("white")

    t.penup()
    t.goto(INITIAL_x, INITIAL_y)
    t.pendown()
    t.left(90)

    t.speed(5)
    name(t, n)
    turtle.done()



if __name__ == '__main__':
    main()
