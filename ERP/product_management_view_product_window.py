import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt


class ViewProductWindow(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.view_user_widget(menu_anterior)

    def view_user_widget(self, menu_anterior):
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("View Users Menu")
        main_label.setFont(QFont("Arial", 16))

        display_users = QLabel(self)
        display_users.setText(self.view_users())
        display_users.setFont(QFont("Arial", 10))

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)

        layout.addWidget(main_label)
        layout.addWidget(display_users)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - View User')

    def view_users(self):
        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        self.c.execute('SELECT * FROM Users')
        users = self.c.fetchall()
        msg = '\n'.join([f'Usuario: {user[1]}, Contraseña: {user[2]}' for user in users])

        return msg