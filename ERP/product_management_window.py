from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

from product_management_add_product_window import AddProductWindow
from product_management_edit_product_window import EditProductWindow
from product_management_view_product_window import ViewProductWindow
from product_management_delete_product_window import DeleteProductWindow

# Crear la segunda ventana de manejo de usuarios
class ProductManagement(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Product Managment Menu")
        main_label.setFont(QFont("Arial", 16))
        layout.addWidget(main_label)

        # Crear y añadir los botones al diseño
        botones = [
            ("Add Users", self.add_product_window),
            ("Edit Users", self.edit_product_window),
            ("View Users", self.view_product_window),
            ("Delete Users", self.delete_product_window),
        ]
        
        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)

        self.setWindowTitle('Product Management')
        self.show()

    def mostrar_menu(self):
        self.show()
        self.ventana.close()

    def add_product_window(self):
        self.ventana = AddProductWindow(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def edit_product_window(self):
        self.ventana = EditProductWindow(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def view_product_window(self):
        self.ventana = ViewProductWindow(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def delete_product_window(self):
        self.ventana = DeleteProductWindow(self.mostrar_menu)
        self.ventana.show()
        self.hide()
