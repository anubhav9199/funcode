import random
import string

LETTERS = string.ascii_letters
NUMS = '0123456789'
SPE = '-+*%&$!_'

SYMBOLS = LETTERS + NUMS + SPE


def password_generator(length):
    return ''.join(random.sample(SYMBOLS, length))


def main():
    length = int(input('Enter the length password you required : '))
    password = password_generator(length)
    print("Your %s length password is %s" % (str(length), password))


if __name__ == '__main__':
    main()

