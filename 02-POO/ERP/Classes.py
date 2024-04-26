job_positions = ["Manager", "Supervisor", "Assistant",
                 "Secretary", "Accountant", "Cashier", "Salesman", "Driver"]
product_presentations = ["60gr", "100gr", "200gr",
                         "500gr", "100ml", "200ml", "500ml", "1L", "2L"]


class Client:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.address = ""
        self.rfc = ""
        self.zip_code = ""

    def update_information(self) -> None:
        self.address = input("Enter the address: ")
        self.rfc = input("Enter the RFC: ")
        self.zip_code = input("Enter the ZIP code: ")


class ProductSold:
    def __init__(self) -> None:
        self.name = ""
        self.upc = ""
        self.presentation = ""
        self.price = 0
        self.quantity_sold = 0
        self.hasIVA = True
        self.hasIEPS = False


class Product(ProductSold):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name
        self.cost = 0
        self.stock = 0

    def update_information(self) -> None:
        self.upc = input("Enter the UPC: ")
        self.price = float(input("Enter the price: "))
        self.cost = float(input("Enter the cost: "))
        print("Select the presentation:")
        for i, presentation in enumerate(product_presentations):
            print(f"{i+1}. {presentation}")
        while True:
            try:
                self.presentation = product_presentations[int(input())-1]
                break
            except:
                print("Invalid option")
        self.hasIVA = input("Has IVA? (y/n): ").lower() == "y"
        self.hasIEPS = input("Has IEPS? (y/n): ").lower() == "y"

    def update_stock(self) -> None:
        self.stock = int(input("Enter the stock: "))


class Employee:
    def __init__(self, id: int, name: str, age: int) -> None:
        self.id = id
        self.id_company = -1
        self.name = name
        self.age = age
        self.address = ""
        self.rfc = ""
        self.salary = 0
        self.position = ""
        self.department = ""

    def update_personal_information(self) -> None:
        self.name = input("Enter the name: ")
        self.age = int(input("Enter the age: "))

    def update_information(self) -> None:
        self.address = input("Enter the address: ")
        self.rfc = input("Enter the RFC: ")
        self.salary = float(input("Enter the salary: "))
        self.department = input("Enter the department: ")
        print("Select the position:")

        # Another way to iterate over a list
        # for i in range(len(job_positions)): # for(int i, i < len(job_positions), i++)
        #     print(f"{i+1}. {job_positions[i]}")

        for i, position in enumerate(job_positions):
            print(f"{i+1}. {position}")
        while True:
            try:
                self.position = job_positions[int(input())-1]
                break
            except:
                print("Invalid option")

    def see_info(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"RFC: {self.rfc}")
        print(f"Salary: {self.salary}")
        print(f"Position: {self.position}")
        print(f"Department: {self.department}\n")


class Company:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.address = ""
        self.rfc = ""
        self.regimen = ""
        self.employees = []
        self.clients = []
        self.products = []
        self.sales = []

    def see_company_information(self) -> None:
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"RFC: {self.rfc}")
        print(f"Regimen: {self.regimen}\n")

    def update_company_name(self) -> None:
        self.name = input("Enter the new name of the company: ")

    def update_information_sat(self) -> None:
        self.address = input("Enter the address: ")
        self.rfc = input("Enter the RFC: ")
        self.regimen = input("Select the Regimen: ")

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def list_employees(self) -> None:
        for i, employee in enumerate(self.employees):
            print(f"{i+1}.- Name: {employee.name} - Position: {employee.position}")
        print("\nDo you want to see additional information of the employee?", end=" ")
        option = input("y/n: ").lower() == "y"
        if option:
            try:
                selected_employee = int(input("Select the employee: ")) - 1
                self.employees[selected_employee].see_info()
                print("Do you want to edit the information of the employee?", end=" ")
                option = input("y/n: ").lower() == "y"
                if option:
                    self.employees[selected_employee].update_personal_information()
                    self.employees[selected_employee].update_information()
            except:
                print("Invalid option")

    def add_client(self, client: Client) -> None:
        self.clients.append(client)

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def add_sale(self, sale) -> None:  # TODO: Define the Sale class
        self.sales.append(sale)
