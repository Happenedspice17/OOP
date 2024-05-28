from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt
import sqlite3

from inventory_report_window import InventoryReportWidget
from sales_report_window import SalesReportWidget
from users_reports_window import UserActivityReportWidget

# Crear la segunda ventana de manejo de clientes
class ReportManagement(QWidget):
    def __init__(self, user_id, menu_anterior):
        super().__init__()
        self.user_id = user_id
        self.setFixedWidth(600)
        self.setWindowTitle("Reports Main Menu")
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Reports Managment Menu")
        main_label.setFont(QFont("Arial", 16))
        layout.addWidget(main_label)

        # Crear y añadir los botones al diseño
        botones = [
            ("Sales Reports", self.sales_report_window),
            ("Inventory Reports", self.inventory_report_window),
            ("User Activity Reports", self.user_activity_window)
        ]
        
        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)

        self.setWindowTitle('Client Management')
        self.show()

    def mostrar_menu(self):
        self.show()
        self.ventana.close()

    def inventory_report_window(self):
        self.ventana = InventoryReportWidget(menu_anterior=self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def sales_report_window(self):
        self.ventana = SalesReportWidget(menu_anterior=self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def user_activity_window(self):
        self.ventana = UserActivityReportWidget(menu_anterior=self.mostrar_menu)
        self.ventana.show()
        self.hide()
