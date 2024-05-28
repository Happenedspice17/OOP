import sys
import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

# Imports of the users logins
from AdminView import MainWindowAdmin
from HRView import MainWindowHR
from ProdManView import MainWindowProductManagement
from ClientManView import MainWindowClientManagement
from SalesManView import SalesManagement


# SELECT * FROM FiscalRegimen

# Función para hacer la database
# def init_db():
#     conn = sqlite3.connect('erp_sales.db')
#     cursor = conn.cursor()

#     cursor.execute('''CREATE TABLE IF NOT EXISTS Logs (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         timestamp TEXT NOT NULL,
#                         user_id INTEGER NOT NULL,
#                         action TEXT NOT NULL,
#                         entity TEXT NOT NULL,
#                         details TEXT NOT NULL
#                       )''')
    
#     cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         username TEXT UNIQUE NOT NULL,
#                         password TEXT NOT NULL,
#                         role TEXT NOT NULL,
#                         name TEXT NOT NULL,
#                         lastname TEXT NOT NULL,
#                         date_joined DATE NOT NULL)''')
    
#     cursor.execute('''CREATE TABLE IF NOT EXISTS Clients (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         name TEXT NOT NULL,
#                         RFC TEXT NOT NULL,
#                         fiscal_regimen_id INTEGER NOT NULL,
#                         address TEXT NOT NULL,
#                         city TEXT NOT NULL,
#                         state TEXT NOT NULL,
#                         zip_code TEXT NOT NULL)''')
    
#     cursor.execute('''CREATE TABLE IF NOT EXISTS FiscalRegimen (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         code INTEGER NOT NULL,
#                         name TEXT NOT NULL)''')
    
#     cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         UPC TEXT NOT NULL,
#                         name TEXT NOT NULL,
#                         id_presentation INTEGER NOT NULL,
#                         price REAL NOT NULL,
#                         cost REAL NOT NULL,
#                         has_iva BOOLEAN NOT NULL,
#                         stock INTEGER NOT NULL)''')
    
#     cursor.execute('''CREATE TABLE IF NOT EXISTS Presentation (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         name TEXT NOT NULL)''')
    
#     cursor.execute('''CREATE TABLE IF NOT EXISTS Sales (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         date_of_sale DATETIME NOT NULL,
#                         user_id INTEGER NOT NULL,
#                         client_id INTEGER NOT NULL,
#                         total_amount REAL NOT NULL)''')
    
#     cursor.execute('''CREATE TABLE IF NOT EXISTS ProductSold (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         id_sale INTEGER NOT NULL,
#                         id_product INTEGER NOT NULL,
#                         quantity INTEGER NOT NULL,
#                         sale_price_per_unit REAL NOT NULL)''')
    
#     # Insert default admin user
#     cursor.execute('''INSERT OR IGNORE INTO Users (username, password, role, name, lastname, date_joined) 
#                       VALUES ('admin', 'admin', 'Admin', 'Default', 'Admin', DATE('now'))''')
    
#     conn.commit()
#     conn.close()

# Hacemos las clases de user, cliente, etc.

class User:
    def __init__(self, username, password, role, name, lastname):
        self.id = None
        self.username = username
        self.password = password
        self.role = role
        self.name = name
        self.lastname = lastname
        self.date_joined = datetime.now().date()

class Client:
    def __init__(self, name, RFC, fiscal_regimen_id, address, city, state, zip_code):
        self.id = None
        self.name = name
        self.RFC = RFC
        self.fiscal_regimen_id = fiscal_regimen_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

class FiscalRegimen:
    def __init__(self, code, name):
        self.id = None
        self.code = code
        self.name = name

class Product:
    def __init__(self, UPC, name, id_presentation, price, cost, has_iva, stock):
        self.id = None
        self.UPC = UPC
        self.name = name
        self.id_presentation = id_presentation
        self.price = price
        self.cost = cost
        self.has_iva = has_iva
        self.stock = stock

class Presentation:
    def __init__(self, name):
        self.id = None
        self.name = name

class Sale:
    def __init__(self, user_id, client_id, total_amount):
        self.id = None
        self.date_of_sale = datetime.now()
        self.user_id = user_id
        self.client_id = client_id
        self.total_amount = total_amount

class ProductSold:
    def __init__(self, id_sale, id_product, quantity, sale_price_per_unit):
        self.id = None
        self.id_sale = id_sale
        self.id_product = id_product
        self.quantity = quantity
        self.sale_price_per_unit = sale_price_per_unit


# Ventana principal del login
class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Initialize a basic UI
    def initUI(self):
        self.setFixedWidth(400)
        #self.setFixedHeight(400)

        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Login Menu ")
        main_label.setFont(QFont("Arial", 16))

        username_label = QLabel(self)
        username_label.setText("Username: ")
        username_label.setFont(QFont("Arial", 10))

        self.username_input = QLineEdit(self)
        self.username_input.resize(250, 24)
        self.username_input.setStyleSheet("background-color: #FFFFFF;")
        
        password_label = QLabel(self)
        password_label.setText("Password: ")
        password_label.setFont(QFont("Arial", 10))

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 24)
        self.password_input.setStyleSheet("background-color: #FFFFFF;")
        
        
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.check_credentials)
        
        layout.addWidget(main_label)
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - Login')
        self.show()

    # Fn to check creds
    def check_credentials(self):

        # User inputs
        username = self.username_input.text()
        password = self.password_input.text()

        # Conect the db
        conn = sqlite3.connect('erp_sales.db')
        cursor = conn.cursor()
        
        # search in db if user exist
        cursor.execute('SELECT * FROM Users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        
        # if true we login
        if user:
            role = user[3]
            user_id = user[0]

            print(user[0], user[1], user[2], user[3],)

            if role.lower() == "admin":
                print("logged in as an admin")
                QMessageBox.information(self, 'Success', 'Login Successful')
                self.main_window = MainWindowAdmin(user_id)
                self.log_action(user_id, "admin_login", "login", "Admin logged in")
                self.main_window.show()
                self.close()

            elif role.lower() == "hr":
                print("logged in as an hr")
                QMessageBox.information(self, 'Success', 'Login Successful')
                self.main_window = MainWindowHR(user_id)
                self.log_action(user_id, "hr_login", "login", "HR logged in")
                self.main_window.show()
                self.close()

            elif role.lower() == "sales management":
                print("logged in as a sales manage")
                QMessageBox.information(self, 'Success', 'Login Successful')
                self.main_window = MainWindowSalesManagement(user_id)
                self.log_action(user_id, "sales_management_login", "login", "Sales Management logged in")
                self.main_window.show()
                self.close()

            elif role.lower() == "client management":
                QMessageBox.information(self, 'Success', 'Login Successful')
                self.main_window = MainWindowClientManagement(user_id)
                self.log_action(user_id, "client_management_login", "login", "Client Management logged in")
                self.main_window.show()
                self.close()

            elif role.lower() == "product management":
                QMessageBox.information(self, 'Success', 'Login Successful')
                self.main_window = MainWindowProductManagement(user_id)
                self.log_action(user_id, "product_management_login", "login", "Product Management logged in")
                self.main_window.show()
                self.close()
            else:
                print("error")
                self.close()
        # Si no es verdadero, nos manda error y volvemos a la pagina principal
        else:
            QMessageBox.warning(self, 'Error', 'Invalid Credentials')

        # Cerramos la conexión
        conn.close()
    
    def log_action(self, user_id, action, entity, details):
        try:
            conn = sqlite3.connect('erp_sales.db')
            cursor = conn.cursor()
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''INSERT INTO Logs (timestamp, user_id, action, entity, details) VALUES (?, ?, ?, ?, ?)''', (timestamp, user_id, action, entity, details))
            
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")




class MainWindowSalesManagement(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("ERP Main Menu")
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("ERP Main Admin Menu")
        main_label.setFont(QFont("Arial", 16))
        layout.addWidget(main_label)

        # Crear y añadir los botones al diseño
        botones = [
            ("Sales Management", self.sales_managment),
            ("Log Out", self.logout)
            
        ]

        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)


        self.setLayout(layout)
        self.show()


    def sales_managment(self):
        self.ventana = SalesManagement(user_id=self.user_id, menu_anterior=self.mostrar_menu)
        self.log_action(self.user_id, "sales_management_window", "enter", f"User with id {self.user_id} entered the sales management tab")
        self.ventana.show()
        self.hide()

    def logout(self):
        self.log_action(self.user_id, "logout", "logout", f"User with id {self.user_id} logout the system")
        self.close()

    def mostrar_menu(self):
        self.show()
        self.ventana.close()

    def log_action(self, user_id, action, entity, details):
        try:
            conn = sqlite3.connect('erp_sales.db')
            cursor = conn.cursor()
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''INSERT INTO Logs (timestamp, user_id, action, entity, details) VALUES (?, ?, ?, ?, ?)''', (timestamp, user_id, action, entity, details))
            
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

if __name__ == '__main__':

   # init_db()
    app = QApplication(sys.argv)
    login = LoginForm()
    sys.exit(app.exec())
