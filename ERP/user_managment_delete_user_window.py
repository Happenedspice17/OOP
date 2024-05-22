import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

class DeleteUserWindow(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.delete_user_widget(menu_anterior)


    def delete_user_widget(self, menu_anterior):
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Delete Users Menu")
        main_label.setFont(QFont("Arial", 16))

        user_label = QLabel(self)
        user_label.setText("User: ")
        user_label.setFont(QFont("Arial", 10))

        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT username FROM Users WHERE username != 'admin'")
        usernames_from_db = self.c.fetchall()

        self.user_input = QComboBox()
        for user_db in usernames_from_db:
            self.user_input.addItem(user_db[0])

        self.delete_user_button = QPushButton("Delete User", self)
        self.delete_user_button.clicked.connect(self.delete_user)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)

        layout.addWidget(main_label)
        layout.addWidget(user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.delete_user_button)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - Delete User')


    def delete_user(self):
        selected_user_input = self.user_input.currentText()
        
        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        
        try:
            self.c.execute('DELETE FROM Users WHERE username = ?', (selected_user_input,))
            self.conn.commit()
            QMessageBox.information(self, 'Éxito', 'User deleted succesfully')
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Error', 'User already exist.')