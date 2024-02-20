username = ["admin"]
password = ["123"]


def main_menu():
    print("1. User Panel")
    print("2.Login")
    print("3.-Exit")
    option = int(input("Choose the option: "))
    
    return option

def access_panel():
    print("1. Add user")
    print("2. Remove user")
    print("3. Go back")
    opt2 = 0
    opt2 = int(input("Choose the option: "))

    if opt2 == 1:
        add_user()
    elif opt2 == 2:
        remove_user()
    elif opt2 == 3:
        pass
    else:
        print("Invalid option, try again")

def add_user():
    username_add = input("Enter the new username: ")

    if username_add in username:
        print(f"User {username_add} already exists, try again")
        access_panel()
    else:
        password_add = input("Enter the new password: ")
        
        username.append(username_add)
        password.append(password_add)
        
        print(f"User {username_add} added to the system\n")
        access_panel()

def remove_user():
    username_remove = input("Enter the username to remove: ")

    if username_remove in username:
        index_of_password = username.index(username_remove)

        username.remove(username_remove)
        password.pop(index_of_password)

        print(f"Username {username_remove} deleted successful")
        
        access_panel()
    else:
        print(f"Wrong input, username {username_remove} doesn't exist")
        access_panel()


def access_menu():
    u = input("Username: ")
    p = input("Password: ")

    if u == username and p == password:
        print("Logged in " + username + "\n")
        print("1. Log out")
        option = int(input("Choose the option"))
            
        if option == 1:
            print("Logged out")
        
        return option
    else:
        print ("Wrong Password, try another time")

program_running = True

while program_running:
    option = main_menu()
    opt2 = 0
    if option == 1:
        access_panel()
    elif option == 2:
        access_menu()
    elif option == 3:
        program_running = False
        print("Bye Bye")
    else:
        print("Option not valid")
