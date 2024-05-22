
import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

class EditUserWindow(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.edit_user_widget(menu_anterior)

    def edit_user_widget(self, menu_anterior):
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Edit Users Menu")
        main_label.setFont(QFont("Arial", 16))

        user_label = QLabel(self)
        user_label.setText("User to edit: ")
        user_label.setFont(QFont("Arial", 10))

        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT username FROM Users WHERE username != 'admin'")
        usernames_from_db = self.c.fetchall()
            
        self.user_input = QComboBox()
        for user_db in usernames_from_db:
            self.user_input.addItem(user_db[0])

        new_username_label = QLabel(self)
        new_username_label.setText("New Username: ")
        new_username_label.setFont(QFont("Arial", 10))


        self.new_username_input = QLineEdit(self)
        self.new_username_input.resize(250, 24)
        self.new_username_input.setStyleSheet("background-color: #FFFFFF;")
        

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
        self.role_input.addItem('Sales Managemnet')
        self.role_input.addItem('Client Managment')
        self.role_input.addItem('Product Managment')

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

        self.edit_user_button = QPushButton("Edit User", self)
        self.edit_user_button.clicked.connect(self.edit_user)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)

        layout.addWidget(main_label)
        layout.addWidget(user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(new_username_label)
        layout.addWidget(self.new_username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(role_label)
        layout.addWidget(self.role_input)
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.edit_user_button)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - Edit User')
    
    def edit_user(self):
        selected_user_input = self.user_input.currentText()
        new_username = self.new_username_input.text()
        password = self.password_input.text()
        selected_role = self.role_input.currentText()
        name = self.name_input.text()
        lastname = self.last_name_input.text()
        
        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        
        try:
            self.c.execute('''UPDATE Users SET username=?, password=?, role=?, name=?, lastname=? WHERE username=?''', (new_username, password, selected_role, name, lastname, selected_user_input))
            self.conn.commit()
            QMessageBox.information(self, 'Éxito', 'User updated succesfully')
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Error', "Can't complete")