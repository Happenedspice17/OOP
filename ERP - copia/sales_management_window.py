from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

from record_sale_window import RecordSaleWindow
from view_sales_window import ViewSalesWindow


# Crear la segunda ventana de manejo de usuarios
class SalesManagement(QWidget):
    def __init__(self, user_id, menu_anterior):
        super().__init__()
        self.user_id = user_id
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Sales Management Menu")
        main_label.setFont(QFont("Arial", 16))
        layout.addWidget(main_label)

        # Crear y añadir los botones al diseño
        botones = [
            ("Record Sale", self.record_sale_window),
            ("View Sales", self.view_sales_window)
        ]
        
        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)

        self.setWindowTitle('Sales Management')
        self.show()

    def mostrar_menu(self):
        self.show()
        self.ventana.close()

    def record_sale_window(self):
        self.ventana = RecordSaleWindow(user_id=self.user_id, menu_anterior=self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def view_sales_window(self):
        self.ventana = ViewSalesWindow(user_id=self.user_id, menu_anterior=self.mostrar_menu)
        self.ventana.show()
        self.hide()

