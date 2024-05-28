from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt
import sqlite3
from datetime import datetime


class SalesReportWidget(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()

        self.setWindowTitle("Sales Main Menu")

        layout = QVBoxLayout()

        self.sales_date_from = QLineEdit()
        self.sales_date_from.setPlaceholderText("From Date (dd/mm/yyyy)")
        layout.addWidget(self.sales_date_from)

        self.sales_date_to = QLineEdit()
        self.sales_date_to.setPlaceholderText("To Date (dd/mm/yyyy)")
        layout.addWidget(self.sales_date_to)

        self.client_id_input = QLineEdit()
        self.client_id_input.setPlaceholderText("Client ID (optional)")
        layout.addWidget(self.client_id_input)

        self.product_id_input = QLineEdit()
        self.product_id_input.setPlaceholderText("Product ID (optional)")
        layout.addWidget(self.product_id_input)

        self.sales_report_button = QPushButton("Generate Sales Report")
        self.sales_report_button.clicked.connect(self.generate_sales_report)
        layout.addWidget(self.sales_report_button)

        self.sales_report_display = QLabel()
        layout.addWidget(self.sales_report_display)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)

    def generate_sales_report(self):
        try:
            conn = sqlite3.connect('erp_sales.db')
            cursor = conn.cursor()

            date_from = self.sales_date_from.text()
            date_to = self.sales_date_to.text()
            client_id = self.client_id_input.text()
            product_id = self.product_id_input.text()

            query = '''
                SELECT Sales.id, Sales.date_of_sale, Sales.client_id, Sales.total_amount, ProductSold.id_product, ProductSold.quantity
                FROM Sales
                INNER JOIN ProductSold ON Sales.id = ProductSold.id_sale
                WHERE Sales.date_of_sale BETWEEN ? AND ?
            '''
            params = [date_from, date_to]

            if client_id:
                query += " AND Sales.client_id = ?"
                params.append(client_id)

            if product_id:
                query += " AND ProductSold.id_product = ?"
                params.append(product_id)

            cursor.execute(query, params)
            sales = cursor.fetchall()

            report = "Sales Report:\n\n"
            for sale in sales:
                report += f"Sale ID: {sale[0]}, Date: {sale[1]}, Client ID: {sale[2]}, Total Amount: {sale[3]:.2f}, Product ID: {sale[4]}, Quantity: {sale[5]}\n"

            self.sales_report_display.setText(report)
            conn.close()
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'Error', f'Database error: {e}')
