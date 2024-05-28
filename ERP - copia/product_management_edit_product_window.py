
import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor, QDoubleValidator
from PyQt6.QtCore import Qt

class EditProductWindow(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.edit_user_widget(menu_anterior)

    def edit_user_widget(self, menu_anterior):
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Edit Products Menu")
        main_label.setFont(QFont("Arial", 16))

        product_label = QLabel(self)
        product_label.setText("Product to edit: ")
        product_label.setFont(QFont("Arial", 10))

        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT name FROM Products")
        usernames_from_db = self.c.fetchall()
            
        self.user_input = QComboBox()
        for user_db in usernames_from_db:
            self.user_input.addItem(user_db[0])

        upc = QLabel(self)
        upc.setText("UPC: ")
        upc.setFont(QFont("Arial", 10))

        self.upc = QLineEdit(self)
        self.upc.resize(250, 24)
        self.upc.setStyleSheet("background-color: #FFFFFF;")

        new_product_label = QLabel(self)
        new_product_label.setText("New Product: ")
        new_product_label.setFont(QFont("Arial", 10))

        self.new_product_label = QLineEdit(self)
        self.new_product_label.resize(250, 24)
        self.new_product_label.setStyleSheet("background-color: #FFFFFF;")
        
        id_presentation = QLabel(self)
        id_presentation.setText("Presentation: ")
        id_presentation.setFont(QFont("Arial", 10))

        self.id_presentation = QComboBox()
        self.id_presentation.setEditable(True)

        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT name FROM Presentation")
        presentations = self.c.fetchall()
        
        for presentation in presentations:
            self.id_presentation.addItem(presentation[0])

        price = QLabel(self)
        price.setText("Price Tag: ")
        price.setFont(QFont("Arial", 10))

        self.price = QLineEdit(self)
        self.price.resize(250, 24)
        self.price.setStyleSheet("background-color: #FFFFFF;")
        self.price.setValidator(QDoubleValidator(0.00, 999999.99, 2))

        cost = QLabel(self)
        cost.setText("Cost: ")
        cost.setFont(QFont("Arial", 10))

        self.cost = QLineEdit(self)
        self.cost.resize(250, 24)
        self.cost.setStyleSheet("background-color: #FFFFFF;")
        self.cost.setValidator(QDoubleValidator(0.00, 999999.99, 2))

        vat_inclusion = QLabel(self)
        vat_inclusion.setText("VAT inclusion: ")
        vat_inclusion.setFont(QFont("Arial", 10))


        self.vat_inclusion = QComboBox()
        self.vat_inclusion.addItem("True")
        self.vat_inclusion.addItem("False")
        self.vat_inclusion.resize(250, 24)
        self.vat_inclusion.setStyleSheet("background-color: #FFFFFF;")

        stock_qty = QLabel(self)
        stock_qty.setText("Stock Quantity: ")
        stock_qty.setFont(QFont("Arial", 10))

        self.stock_qty = QLineEdit(self)
        self.stock_qty.resize(250, 24)
        self.stock_qty.setStyleSheet("background-color: #FFFFFF;")
        self.stock_qty.setValidator(QDoubleValidator(0, 999999, 0))

        self.edit_user_button = QPushButton("Edit User", self)
        self.edit_user_button.clicked.connect(self.edit_user)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)

        layout.addWidget(main_label)
        layout.addWidget(product_label)
        layout.addWidget(self.user_input)
        layout.addWidget(upc)
        layout.addWidget(self.upc)
        layout.addWidget(new_product_label)
        layout.addWidget(self.new_product_label)
        layout.addWidget(id_presentation)
        layout.addWidget(self.id_presentation)
        layout.addWidget(price)
        layout.addWidget(self.price)
        layout.addWidget(cost)
        layout.addWidget(self.cost)
        layout.addWidget(vat_inclusion)
        layout.addWidget(self.vat_inclusion)
        layout.addWidget(stock_qty)
        layout.addWidget(self.stock_qty)
        layout.addWidget(self.edit_user_button)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - Edit Product')
    
    def edit_user(self):
        selected_product_input = self.user_input.currentText()
        new_product_label = self.new_product_label.text()
        upc = self.upc.text()
        id_presentation = self.id_presentation.currentText()
        price = self.price.text()
        cost = self.cost.text()
        vat_inclusion = self.vat_inclusion.currentText()
        stock_qty = self.stock_qty.text()
        
        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()

        if not upc or not new_product_label or not price or not cost or not stock_qty:
            QMessageBox.warning(self, 'Input Error', 'All fields must be filled out.')
            return

        # Validate numeric fields
        try:
            price = float(price)
            cost = float(cost)
            stock_qty = int(stock_qty)
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Price, Cost, and Stock Quantity must be valid numbers.')
            return

        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        
        try:
            self.c.execute('UPDATE Products SET upc=?, name=?, id_presentation=?, price=?, cost=?, has_iva=?, stock=? WHERE name=?', (upc, new_product_label, id_presentation, price, cost, vat_inclusion, stock_qty, selected_product_input))
            self.conn.commit()
            QMessageBox.information(self, 'Éxito', 'Product edited succesfully')
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Error', 'Product already exist.')