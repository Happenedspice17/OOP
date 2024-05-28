
import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

class AddUserWindow(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.add_user_widget(menu_anterior)


    def add_user_widget(self, menu_anterior):
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Add Users Menu")
        main_label.setFont(QFont("Arial", 16))

        user_label = QLabel(self)
        user_label.setText("User: ")
        user_label.setFont(QFont("Arial", 10))

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.setStyleSheet("background-color: #FFFFFF;")

        password_label = QLabel(self)
        password_label.setText("Password: ")
        password_label.setFont(QFont("Arial", 10))

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 24)
        self.password_input.setStyleSheet("background-color: #FFFFFF;")

        role_label = QLabel(self)
        role_label.setText("Role: ")
        role_label.setFont(QFont("Arial", 10))

        self.role_input = QComboBox()
        self.role_input.addItem('Sales Management')
        self.role_input.addItem('Client Management')
        self.role_input.addItem('Product Management')
        self.role_input.addItem('HR')

        name_label = QLabel(self)
        name_label.setText("Name: ")
        name_label.setFont(QFont("Arial", 10))

        self.name_input = QLineEdit(self)
        self.name_input.resize(250, 24)
        self.name_input.setStyleSheet("background-color: #FFFFFF;")

        last_name_label = QLabel(self)
        last_name_label.setText("Lastname: ")
        last_name_label.setFont(QFont("Arial", 10))

        self.last_name_input = QLineEdit(self)
        self.last_name_input.resize(250, 24)
        self.last_name_input.setStyleSheet("background-color: #FFFFFF;")

        self.add_user_button = QPushButton("Add User", self)
        self.add_user_button.clicked.connect(self.add_user)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)

        layout.addWidget(main_label)
        layout.addWidget(user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(role_label)
        layout.addWidget(self.role_input)
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.add_user_button)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - Add User')
    
    def add_user(self):
        username = self.user_input.text()
        password = self.password_input.text()
        selected_role = self.role_input.currentText()
        name = self.name_input.text()
        lastname = self.last_name_input.text()
        date_joined = datetime.now().date()
        
        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()

        if not username or not password or not selected_role or not name or not lastname:
            QMessageBox.warning(self, 'Input Error', 'All fields must be filled out.')
            return
        
        try:
            self.c.execute('INSERT INTO Users (username, password, role, name, lastname, date_joined) VALUES (?, ?, ?, ?, ?, ?)', (username, password, selected_role, name, lastname, date_joined))
            self.conn.commit()
            QMessageBox.information(self, 'Éxito', 'User added succesfully')
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Error', 'User already exist.')