'''
import sys
import time

import user_utils

USER_DICT = {}

Questions = {
    1: 'What is your fathers name ->: ', 
    2: 'What is your teachers name ->: ', 
    3: 'What is your pets name ->: ', 
    4: 'What is your last working company\'s name ->: ',
}


def register_user(username, password, question, answer):
    user_utils.write_in_file(username, password, question, answer)


def forget_password():
    username = input("Enter the Username ->: ")
    return


def change_password():
    return


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
        user_utils.write_login_logs(username, "Logout")
        print("Logged Out Successfully")
        return

    print("You are already logged out")


def login():
    username = input("Enter the Username ->: ")
    password = input("Enter the Password ->: ")
    if password == USER_DICT[username]['password']:
        USER_DICT[username]['login'] = True
        USER_DICT[username]['loginTs'] = int(time.time())
        user_utils.write_login_logs(username, 'Login')
        print("Logged In Successfully")
        return
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
'''

user_data = {'shruti':'@Shruti27'}

# Register function  
def register():
    symbol = ['@','#','$']
    while 1:
        name = input("Enter your username to register: ")
        if name in user_data:
            prompt ='This username has already been used, please re-enter:'
            continue
        else:
            break
        
    while 1:
        password = input('Please enter the password:')
        if password == '':
          print("Password cannot be empty.")
          continue
         
        elif len(password)<6:
            print("Length of password should be greater than 6 characters.")
            continue
            
        elif not any(char.isdigit() for char in password):
            print('Password should have at least one numeral.')
            continue

        elif not any(char.isupper() for char in password):
            print('Password should have at least one uppercase letter.')
            continue

        elif not any(char.islower() for char in password):
            print('Password should have at least one lowercase letter.')
            continue

        elif not any(char in symbol for char in password):
            print("Password should have at least one special symbol.")
            continue
            
        elif not password or " " in password:
            print("Password cannot contain spaces.")     
            continue

        verify_pwd = input('Re-Enter your password: ')
        if password == verify_pwd:
            user_data[name] = password
            print('Registered successfully!')
        else:
            print('Password not verified!')  
            
# Loginfunction             
def login():
    # wile 1:
    name = input("Please enter the user name: ")
    if name not in user_data:
        print('This user does not exist!\nKindly register yourself:-> ')
        register()
        # continue
    else:
        # break
        password = input('Please enter the password:')
        pwd = user_data.get(name)
        if password == pwd:
            print('Welcome',name)
        else:
            print('Password error!')

# Change your Password function 
def change_password():
    while 1:
        username = input("Enter your username: ")
        if username not in user_data:
            print("This user doesn't exist! Create new user:->")
            register()
        else:
            password = input("Enter you current password: ")
            pwd = user_data.get(username)
            if password != pwd:
                print("Your input doesn't match to your current password.")
            else:
                new_pwd = input("Enter your new password: ")
                user_data[username] = new_pwd
                print("Password changed successfully.") 

# Main Function
def main():
      prompt ='''
 |---New user: N---|
 |---Login account: L---|
 |---Change password: C---|
 |---Exit the program: E---|

 Enter the command code: '''
      while 1:
            chosen = False
            while not chosen:
                  choice = input(prompt)
                  if choice.upper() not in "NLCE":
                      print('Instruction error re-enter: ')
                  else:
                      chosen = True
            if choice in ["E", "e"]:
                  break
            if choice in ["N","n"]:
                  register()
            if choice in ["L","l"]:
                  login()
            if choice in ["C","c"]:
                  change_password()


if __name__ == "__main__":
    main()




