import sys
import time

USER_DICT = {"anubhav": "anubhav@12345", "vaishnavi": "vaishnavi@12345"}

Questions = {
    1: 'What is your fathers name ->: ', 
    2: 'What is your teachers name ->: ', 
    3: 'What is your pets name ->: ', 
    4: 'What is your last working company\'s name ->: ',
}


def register_user(username, password, question, answer):
    USER_DICT[username] = {
        "password": password,
        "login": False,
        "loginTs": int(time.time())
    }
    USER_DICT[username][question] = answer


def forget_password():
    username = input("Enter the Username ->: ")


def change_password():
    username = input("Enter the Username ->: ")
    password = input("Enter the Password ->: ")
    verify_password = input("Enter the Password again ->: ")


def signup():
    username = input("Enter the Username ->: ")
    if username in USER_DICT:
        print("please select different user name and try again")
    password = input("Enter the Password ->: ")
    verify_password = input("Enter the Password again ->: ")
    question = int(input('Hint Questions (set one of them to use in case of recovery)\n\n1. What is your fathers name\n2. What is your teachers name\n3. What is your pets name\n4. What is your last working company\'s name\n\nEnter your choice by pressing 1, 2....'))
    answer = input(Questions[question])
    
    if verify_password == password:
        register_user(username, password, question, answer)
    else:
        print("your password does not match \nplease come back and try again")


def logout():
    username = input("Enter the Username ->: ")
    if USER_DICT[username]['login']:
        USER_DICT[username]['login'] = False
        print("Logged Out Successfully")
        return

    print("You are already logged out")


def login():
    username = input("Enter the Username ->: ")
    password = input("Enter the Password ->: ")
    if password == USER_DICT[username]['password']:
        USER_DICT[username]['login'] = True
        USER_DICT[username]['loginTs'] = int(time.time())
        print("Logged In Successfully")
    else:
        if USER_DICT[username]['login']:
            USER_DICT[username]['login'] = False

        print("Username or Password is mismatch\nPlease Try again")


def main():
    print("\nWhat you want to do?\n\n1. Login\n2. Sign Up\n3. Change Password\n4. Forget Password\n")
    user_input = int(input("Enter your input ->: "))
    if user_input == 1:
        login()
    elif user_input == 2:
        signup()
    elif user_input == 3:
        change_password()
    elif user_input == 4:
        forget_password()
    else:
        print("You have given a wrong input!! \nPlease give a write input again")



if __name__ == '__main__':
    try:
        while True:
            main()
    except:
        sys.exit
