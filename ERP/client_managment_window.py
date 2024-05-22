from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

from client_managment_add_client_window import AddClientWindow
from client_managment_edit_client_window import EditClientWindow
from client_managment_view_client_window import ViewClientWindow
from client_managment_delete_client_window import DeleteClientWindow


# Crear la segunda ventana de manejo de clientes
class ClientManagment(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Client Managment Menu")
        main_label.setFont(QFont("Arial", 16))
        layout.addWidget(main_label)

        # Crear y añadir los botones al diseño
        botones = [
            ("Add Clients", self.add_user_window),
            ("Edit Clients", self.edit_user_window),
            ("View Clients", self.view_user_window),
            ("Delete Clients", self.delete_user_window),
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

    def add_user_window(self):
        self.ventana = AddUserWindow(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def edit_user_window(self):
        self.ventana = EditUserWindow(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def view_user_window(self):
        self.ventana = ViewUserWindow(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def delete_user_window(self):
        self.ventana = DeleteUserWindow(self.mostrar_menu)
        self.ventana.show()
        self.hide()
