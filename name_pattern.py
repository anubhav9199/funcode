import turtle
import letter_utils
import random

INITIAL_x = -200
INITIAL_y = 60

letter_function_map = {
    'A': letter_utils.a_function,
    'B': letter_utils.b_function,
    'C': letter_utils.c_function,
    'D': letter_utils.d_function,
    'E': letter_utils.e_function,
    'F': letter_utils.f_function,
    'G': letter_utils.g_function,
    'H': letter_utils.h_function,
    'I': letter_utils.i_function,
    'J': letter_utils.j_function,
    'K': letter_utils.k_function,
    'L': letter_utils.l_function,
    'M': letter_utils.m_function,
    'N': letter_utils.n_function,
    'O': letter_utils.o_function,
    'P': letter_utils.p_function,
    'Q': letter_utils.q_function,
    'R': letter_utils.r_function,
    'S': letter_utils.s_function,
    'T': letter_utils.t_function,
    'U': letter_utils.u_function,
    'V': letter_utils.v_function,
    'W': letter_utils.w_function,
    'X': letter_utils.x_function,
    'Y': letter_utils.y_function,
    'Z': letter_utils.z_function,
}


def name(turtle, name):
    col = ('red', 'yellow', 'green', 'blue', 'white')
    y = INITIAL_y
    turtle.penup()
    turtle.goto(INITIAL_x, y)
    turtle.pendown()
    turtle.left(90)
    _names = list(name.split(" "))
    for _n in range(len(_names)):
        for letter in _names[_n]:
            turtle.color(col[random.randint(0, 4)])
            letter_function_map[letter.upper()](turtle, letter)
            turtle.penup()
            turtle.left(90)
            turtle.forward(15)
            turtle.left(90)
            turtle.pendown()
        turtle.penup()
        y = INITIAL_y - ((_n + 1) * 100)
        turtle.goto(INITIAL_x, y)
        turtle.pendown()


def main():
    n = input("Enter the name here : ")
    t = turtle.Turtle()
    t.getscreen().bgcolor("black")
    t.color("white")

    t.speed(5)
    name(t, n)
    turtle.done()



if __name__ == '__main__':
    main()
