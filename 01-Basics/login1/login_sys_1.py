username="Charles"
password ="1234"

def main_menu():
    print("1.-Access the system.")
    print("2.-Exit")
    option =int(input("Choose the option"))

    return option


def access_menu():
    u = input("Username: ")
    p = input("Password: ")

    if u == username and p == password:
        print("Logged in " + username + "\n")
        print("1. Log out")
        option =int(input("Choose the option"))
            
        if option == 1:
            print("Logged out")
        
        return option
    else:
        print ("Wrong Password, try another time")
        

program_running = True

while program_running:
    option= main_menu()
    if option == 1:
        access_menu()
    elif option == 2:
        program_running=False
        print("Bye Bye")
    else:
        print("option not valid")