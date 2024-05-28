from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt
import sqlite3
from datetime import datetime

class InventoryReportWidget(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()

        self.setWindowTitle("Inventory Main Menu")

        layout = QVBoxLayout()

        self.inventory_report_button = QPushButton("Generate Inventory Report")
        self.inventory_report_button.clicked.connect(self.generate_inventory_report)
        layout.addWidget(self.inventory_report_button)

        self.inventory_report_display = QLabel()
        layout.addWidget(self.inventory_report_display)
        
        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)

    def mostrar_menu(self):
        self.show()
        self.ventana.close()

    def generate_inventory_report(self):
        try:
            conn = sqlite3.connect('erp_sales.db')
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, name, price, stock, has_iva
                FROM Products
            ''')
            products = cursor.fetchall()

            report = "Inventory Report:\n\n"
            for product in products:
                report += f"Product ID: {product[0]}, Name: {product[1]}, Price: {product[2]:.2f}, Stock: {product[3]}, Has IVA: {'Yes' if product[4] else 'No'}\n"

            self.inventory_report_display.setText(report)
            conn.close()
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'Error', f'Database error: {e}')
