import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt


class ViewProductWindow(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.view_product_widget(menu_anterior)

    def view_product_widget(self, menu_anterior):
        self.setFixedWidth(600)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("View Products Menu")
        main_label.setFont(QFont("Arial", 16))

        display_users = QLabel(self)
        display_users.setText(self.view_product())
        display_users.setFont(QFont("Arial", 10))

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)

        layout.addWidget(main_label)
        layout.addWidget(display_users)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - View Products')

    def view_product(self):
        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        self.c.execute('SELECT * FROM Products')
        products = self.c.fetchall()
        msg = '\n'.join([f'UPC: {product[1]}, Name: {product[2]}, Presentation: {product[3]}, Price: {product[4]} Cost: {product[5]}, IVA: {product[6]}, Stock: {product[7]}' for product in products])

        return msg