import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

class DeleteProductWindow(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.delete_product_widget(menu_anterior)


    def delete_product_widget(self, menu_anterior):
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Delete Products Menu")
        main_label.setFont(QFont("Arial", 16))

        user_label = QLabel(self)
        user_label.setText("Product: ")
        user_label.setFont(QFont("Arial", 10))

        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT name FROM Products")
        products_from_db = self.c.fetchall()

        self.user_input = QComboBox()
        for product in products_from_db:
            self.user_input.addItem(product[0])

        self.delete_product_button = QPushButton("Delete Product", self)
        self.delete_product_button.clicked.connect(self.delete_product)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)

        layout.addWidget(main_label)
        layout.addWidget(user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.delete_product_button)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - Delete Product')


    def delete_product(self):
        selected_product_input = self.user_input.currentText()
        
        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        
        try:
            self.c.execute('DELETE FROM Products WHERE name = ?', (selected_product_input,))
            self.conn.commit()
            QMessageBox.information(self, 'Éxito', 'Product deleted succesfully')
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Error', 'User does not exist.')