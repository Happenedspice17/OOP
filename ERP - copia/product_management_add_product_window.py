import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor, QDoubleValidator
from PyQt6.QtCore import Qt

class AddProductWindow(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.add_product_widget(menu_anterior)


    def add_product_widget(self, menu_anterior):
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Add Product Menu")
        main_label.setFont(QFont("Arial", 16))

        upc = QLabel(self)
        upc.setText("UPC: ")
        upc.setFont(QFont("Arial", 10))

        self.upc = QLineEdit(self)
        self.upc.resize(250, 24)
        self.upc.setStyleSheet("background-color: #FFFFFF;")

        product_name = QLabel(self)
        product_name.setText("Product name: ")
        product_name.setFont(QFont("Arial", 10))

        self.product_name = QLineEdit(self)
        self.product_name.resize(250, 24)
        self.product_name.setStyleSheet("background-color: #FFFFFF;")

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


        self.add_product_button = QPushButton("Add Product", self)
        self.add_product_button.clicked.connect(self.add_product)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)

        layout.addWidget(main_label)
        layout.addWidget(upc)
        layout.addWidget(self.upc)
        layout.addWidget(product_name)
        layout.addWidget(self.product_name)
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
        layout.addWidget(self.add_product_button)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - Add Product')
    
    def add_product(self):
        upc = self.upc.text()
        product_name = self.product_name.text()
        id_presentation = self.id_presentation.currentText()
        price = self.price.text()
        cost = self.cost.text()
        vat_inclusion = self.vat_inclusion.currentText()
        stock_qty = self.stock_qty.text()
        

        if not upc or not product_name or not price or not cost or not stock_qty:
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
            self.c.execute('INSERT INTO Products (UPC, name, id_presentation, price, cost, has_iva, stock) VALUES (?, ?, ?, ?, ?, ?, ?)', (upc, product_name, id_presentation, price, cost, vat_inclusion, stock_qty))
            self.conn.commit()
            QMessageBox.information(self, 'Éxito', 'Product added succesfully')
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Error', 'Product already exist.')