from Classes import *  # Import all classes from Classes.py
# from Classes import Company, Employee # Import specific classess from Classes.py
from Functions import *  # Import all functions from Functions.py
import os  # Import the os module

companies = []  # List to store the companies
id = 0
id_employee = 0
# Check if the company file exists
if os.path.isfile("companies.csv"):
    with open("companies.csv", "r") as file:
        for line in file:
            data = line.strip().split(",")
            company = Company(data[0], data[1])
            company.address = data[2]
            company.rfc = data[3]
            company.regimen = data[4]
            companies.append(company)
            id = int(data[0])

    if len(companies) > 0:
        if os.path.isfile("employees.csv"):
            with open("employees.csv", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    employee = Employee(data[0], data[2], data[3])
                    employee.id_company = int(data[1])
                    employee.address = data[4]
                    employee.rfc = data[5]
                    employee.salary = float(data[6])
                    employee.position = data[7]
                    employee.department = data[8]
                    for company in companies:
                        if company.id == employee.id_company:
                            company.employees.append(employee)
                            break
                    id_employee = int(data[0])

id = id + 1  # Update the id to the next available id
id_employee = id_employee + 1  # Update the id_employee to the next available id
programm_running = True  # Variable to control the program execution

while programm_running:
    main_menu()  # Call the main_menu function
    option = input("Select an option: ")  # Ask the user for an option
    if option == "1":
        # Call the add_company function and add the company to the list
        companies.append(create_company(id))
        id += 1
        with open("companies.csv", "w") as file:
            for company in companies:
                file.write(f"{company.id},{company.name},{company.address},{
                           company.rfc},{company.regimen}\n")
    elif option == "2":
        # Print the companies to select one
        for i, company in enumerate(companies):
            print(f"{i+1}. {company.name}")
        # Ask the user for the company to access
        selected_company = int(input("Select the company to access: ")) - 1
        # Call the company_menu function with the selected company and update the company in the list
        # once we have finished working with it
        companies[selected_company], id_employee = company_menu(
            companies[selected_company], id_employee)
    elif option == "3":
        # Save the companies to a file
        programm_running = False
    else:
        print("Invalid option")
