import sys
import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt


from sales_management_window import SalesManagement

class MainWindowSalesManagement(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("ERP Main Menu")
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        
        main_label = QLabel(self)
        main_label.setText("ERP Main Sales Management Menu")
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
