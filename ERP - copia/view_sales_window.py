import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QPushButton, QWidget, QScrollArea, QMessageBox
from PyQt6.QtCore import Qt
from datetime import datetime

class ViewSalesWindow(QMainWindow):
    def __init__(self, user_id, menu_anterior):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("View Sales")
        self.setGeometry(100, 100, 800, 600)

        # Layout for filtering options
        self.filter_layout = QVBoxLayout()

        # Date filter
        self.date_label = QLabel("Date (dd/mm/yyyy):")
        self.date_filter = QLineEdit()
        self.date_filter.setPlaceholderText("Enter Date")
        self.filter_layout.addWidget(self.date_label)
        self.filter_layout.addWidget(self.date_filter)

        # Client filter
        self.client_label = QLabel("Client ID:")
        self.client_filter = QLineEdit()
        self.client_filter.setPlaceholderText("Enter Client ID")
        self.filter_layout.addWidget(self.client_label)
        self.filter_layout.addWidget(self.client_filter)

        # Seller filter
        self.seller_label = QLabel("Seller ID:")
        self.seller_filter = QLineEdit()
        self.seller_filter.setPlaceholderText("Enter Seller ID")
        self.filter_layout.addWidget(self.seller_label)
        self.filter_layout.addWidget(self.seller_filter)

        # Filter button
        self.filter_button = QPushButton("Filter")
        self.filter_button.clicked.connect(self.filter_sales)
        self.filter_layout.addWidget(self.filter_button)

        # Return button
        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)
        self.filter_layout.addWidget(self.boton_regresar)

        # Scroll area for sales data
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.sales_display = QLabel()
        self.sales_display.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.scroll_area.setWidget(self.sales_display)
        
        # Main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.filter_layout)
        self.main_layout.addWidget(self.scroll_area)

        container = QWidget()
        container.setLayout(self.main_layout)
        self.setCentralWidget(container)

        self.load_sales()

    def load_sales(self):
        try:
            conn = sqlite3.connect('erp_sales.db')
            cursor = conn.cursor()
            cursor.execute('''SELECT Sales.date_of_sale, Sales.client_id, Sales.user_id, Sales.total_amount, group_concat(ProductSold.id_product || ' x ' || ProductSold.quantity) 
                              FROM Sales
                              JOIN ProductSold ON Sales.id = ProductSold.id_sale
                              GROUP BY Sales.id
                              ORDER BY Sales.date_of_sale DESC''')
            sales = cursor.fetchall()

            sales_text = ""
            for sale in sales:
                total_amount = round(sale[3], 2)
                sale_info = (
                    f"Date: {sale[0]}\n"
                    f"Client ID: {sale[1]}\n"
                    f"Seller ID: {sale[2]}\n"
                    f"Total Amount: {total_amount:.2f}\n"
                    f"Products (Id, Qty): {sale[4]}\n"
                    "----------------------------------------\n"
                )
                sales_text += sale_info

            self.sales_display.setText(sales_text)
            conn.close()
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'Error', f'Database error: {e}')

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

    def filter_sales(self):
        date_filter = self.date_filter.text()
        client_filter = self.client_filter.text()
        seller_filter = self.seller_filter.text()

        self.log_action(self.user_id, "filtered_sales_table", "filter", f"The user with id {self.user_id} filtered the sales database")

        query = '''SELECT Sales.date_of_sale, Sales.client_id, Sales.user_id, Sales.total_amount, group_concat(ProductSold.id_product || ' x ' || ProductSold.quantity) 
                   FROM Sales
                   JOIN ProductSold ON Sales.id = ProductSold.id_sale
                   WHERE 1=1'''

        params = []
        if client_filter:
            query += ' AND Sales.client_id = ?'
            params.append(client_filter)
        if seller_filter:
            query += ' AND Sales.user_id = ?'
            params.append(seller_filter)
        if date_filter:
            try:
                date = datetime.strptime(date_filter, '%d/%m/%Y').date()
                query += ' AND date(Sales.date_of_sale) = date(?)'
                params.append(date)
            except ValueError:
                QMessageBox.warning(self, 'Error', 'Invalid date format. Use dd/mm/yyyy.')
                return

        query += ' GROUP BY Sales.id ORDER BY Sales.date_of_sale DESC'

        try:
            conn = sqlite3.connect('erp_sales.db')
            cursor = conn.cursor()
            cursor.execute(query, params)
            sales = cursor.fetchall()

            sales_text = ""
            for sale in sales:
                total_amount = round(sale[3], 2)
                sale_info = (
                    f"Date: {sale[0]}\n"
                    f"Client ID: {sale[1]}\n"
                    f"Seller ID: {sale[2]}\n"
                    f"Total Amount: {total_amount:.2f}\n"
                    f"Products: {sale[4]}\n"
                    "----------------------------------------\n"
                )
                sales_text += sale_info

            self.sales_display.setText(sales_text)
            conn.close()
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'Error', f'Database error: {e}')

