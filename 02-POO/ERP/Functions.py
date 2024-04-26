from Classes import *
import os


def main_menu() -> None:
    """Print the main menu of the program"""
    print("Main Menu:")
    print("1. Add Company")
    print("2. Access Company")
    print("3. Exit")


def update_company(company: Company) -> None:
    """Function to save the companies to a file.

    Parameters:
    companies: list
    """
    companies = []  # List to store the companies
    # Check if the company file exists
    if os.path.isfile("companies.csv"):
        with open("companies.csv", "r") as file:
            for line in file:
                data = line.strip().split(",")
                c = Company(data[0], data[1])
                c.address = data[2]
                c.rfc = data[3]
                c.regimen = data[4]
                companies.append(c)

    company_in_list = False
    for c in companies:
        if c.id == company.id:
            c = company
            company_in_list = True
            break

    if company_in_list == False:
        companies.append(company)

    with open("companies.csv", "w") as file:
        for c in companies:
            file.write(f"{c.id},{c.name},{c.address},{c.rfc},{c.regimen}\n")

    print("Companies saved successfully")


def create_company(id: int) -> Company:
    """Function to create a new company object and return it.

    Parameters: 
    id: int


    return: Company object
    """
    name = input("Enter the name of the company: ")
    company = Company(id, name)
    return company


def print_company_menu(company: Company) -> None:
    """Function to print the company menu.

    Parameters:
    company: Company object
    """
    print(f"Company Menu: {company.name}")
    print("1. See Company Details")
    print("2. Edit Company Name")
    print("3. Edit Company Information")
    print("4. Add Employee")
    print("5. List Employees")
    print("6. Back")


def save_employee_to_file(employee: Employee) -> None:
    """Function to save the employees to a file.

    Parameters:
    employee: Employee object
    """
    employees = []  # List to store the employees
    # Check if the employee file exists
    if os.path.isfile("employees.csv"):
        with open("employees.csv", "a") as file:
            file.write(f"{employee.id},{employee.id_company},{employee.name},{employee.age},{
                       employee.address},{employee.rfc},{employee.salary},{employee.position},{employee.department}\n")


def update_employee_file(employees: list) -> None:
    """Function to save the employees to a file.

    Parameters:
    employees: list
    """
    pass


def add_employee(idCo: int, idE: int) -> Employee:
    """Function to create a new employee object and return it.

    Parameters:
    idCo: int - id of the company
    idE: int - id of the employee

    return: Employee object
    """
    name = input("Enter the name of the employee: ")
    age = int(input("Enter the age of the employee: "))
    employee = Employee(idE, name, age)
    employee.id_company = idCo

    save_employee_to_file(employee)

    return employee


def company_menu(company: Company, idE: int) -> Company:
    """Function to show the company menu and return the updated company object.

    Parameters:
    company: Company object
    idE: int - id of the next employee on the system

    return: updated Company object
    return: updated id employee
    """
    company_menu_running = True  # Variable to control the company menu execution
    while company_menu_running:
        print_company_menu(company)
        option = input("Select an option: ")
        if option == "1":
            company.see_company_information()
        elif option == "2":
            company.update_company_name()
        elif option == "3":
            company.update_information_sat()
        elif option == "4":
            company.employees.append(add_employee(company.id, idE))
            idE += 1
        elif option == "5":
            company.list_employees()
            update_employee_file(company.employees)
        elif option == "6":
            update_company(company)
            company_menu_running = False
        else:
            print("Invalid option")
    return company, idE
