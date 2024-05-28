import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QPushButton, QWidget, QComboBox, QMessageBox
from datetime import datetime

class RecordSaleWindow(QMainWindow):
    def __init__(self, user_id, menu_anterior):
        super().__init__()
        self.user_id = user_id
        self.product_prices = {}  # Dictionary to store product prices
        
        self.setWindowTitle("Record Sale")
        self.setGeometry(100, 100, 600, 400)
        
        # Vertical layout for the form
        self.layout = QVBoxLayout()
        
        # Client ID input
        self.client_id_label = QLabel("Client ID:")
        self.client_id_input = QLineEdit()
        self.client_id_input.setPlaceholderText("Enter Client ID")
        self.layout.addWidget(self.client_id_label)
        self.layout.addWidget(self.client_id_input)
        
        # Product selection
        self.product_label = QLabel("Product:")
        self.product_combo_box = QComboBox()
        self.product_combo_box.currentIndexChanged.connect(self.update_price)
        self.layout.addWidget(self.product_label)
        self.layout.addWidget(self.product_combo_box)
        
        # Quantity input
        self.quantity_label = QLabel("Quantity:")
        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Enter Quantity")
        self.quantity_input.textChanged.connect(self.update_total_price)
        self.layout.addWidget(self.quantity_label)
        self.layout.addWidget(self.quantity_input)
        
        # Price per unit display
        self.price_label = QLabel("Price per Unit:")
        self.price_display = QLabel("")
        self.layout.addWidget(self.price_label)
        self.layout.addWidget(self.price_display)
        
        # Total price display
        self.total_price_label = QLabel("Total Price:")
        self.total_price_display = QLabel("")
        self.layout.addWidget(self.total_price_label)
        self.layout.addWidget(self.total_price_display)
        
        # Record sale button
        self.submit_button = QPushButton("Record Sale")
        self.submit_button.clicked.connect(self.record_sale)
        self.layout.addWidget(self.submit_button)
        
        # Return to previous menu button
        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)
        self.layout.addWidget(self.boton_regresar)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    
    def populate_product_combo_box(self):
        try:
            conn = sqlite3.connect('erp_sales.db')
            cursor = conn.cursor()
            cursor.execute('SELECT name, price FROM Products')
            products = cursor.fetchall()
            self.product_combo_box.clear()
            self.product_combo_box.addItems([product[0] for product in products])
            self.product_prices = {product[0]: product[1] for product in products}
            conn.close()
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'Error', f'Database error: {e}')
    
    def update_price(self):
        selected_product = self.product_combo_box.currentText()
        if selected_product in self.product_prices:
            price_per_unit = self.product_prices[selected_product]
            self.price_display.setText(f'{price_per_unit:.2f}')
            self.update_total_price()

    def update_total_price(self):
        selected_product = self.product_combo_box.currentText()
        if selected_product in self.product_prices:
            price_per_unit = self.product_prices[selected_product]
            try:
                quantity = int(self.quantity_input.text())
                total_price = price_per_unit * quantity
                self.total_price_display.setText(f'{total_price:.2f}')
            except ValueError:
                self.total_price_display.setText("0.00")

    def record_sale(self):
        try:
            client_id = int(self.client_id_input.text())
            selected_product = self.product_combo_box.currentText()
            quantity = int(self.quantity_input.text())

            if not client_id or not selected_product or not quantity:
                QMessageBox.warning(self, 'Input Error', 'All fields must be filled out.')
                return

            if selected_product and quantity > 0:
                sale_price_per_unit = self.product_prices[selected_product]

                # Database operations
                conn = sqlite3.connect('erp_sales.db')
                cursor = conn.cursor()
                
                cursor.execute('SELECT id, has_iva FROM Products WHERE name=?', (selected_product,))
                product_data = cursor.fetchone()
                product_id, has_iva = product_data[0], product_data[1]

                total_amount = quantity * sale_price_per_unit
                if has_iva:
                    total_amount *= 1.16  # Assuming IVA is 16%

                # Take out the stock and calculate
                cursor.execute('SELECT stock FROM Products WHERE name=?', (selected_product,))
                product_stock_data = cursor.fetchone()
                stock = product_stock_data[0]

                actual_stock = stock - quantity

                # Insert sale record
                cursor.execute('''INSERT INTO Sales (date_of_sale, user_id, client_id, total_amount) VALUES (?, ?, ?, ?)''', (datetime.now(), self.user_id, client_id, total_amount))
                sale_id = cursor.lastrowid

                # Insert product sold record
                cursor.execute('''INSERT INTO ProductSold (id_sale, id_product, quantity, sale_price_per_unit) VALUES (?, ?, ?, ?)''', (sale_id, product_id, quantity, sale_price_per_unit))

                # Reduce the number of stock in Products
                cursor.execute('UPDATE Products SET stock=? WHERE id=?', (actual_stock, product_id))

                conn.commit()
                conn.close()
                
                QMessageBox.information(self, 'Success', 'Sale recorded successfully!')
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'Error', f'Database error: {e}')
        except ValueError as e:
            QMessageBox.warning(self, 'Error', f'Invalid input: {e}')
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'An error occurred: {e}')

    def showEvent(self, event):
        self.populate_product_combo_box()
        super().showEvent(event)
