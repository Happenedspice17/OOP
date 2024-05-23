import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

class AddClientWindow(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.menu_anterior = menu_anterior
        self.add_client_widget()

    def add_client_widget(self):
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Add Clients Menu")
        main_label.setFont(QFont("Arial", 16))

        client_label = QLabel("Client:")
        client_label.setFont(QFont("Arial", 10))

        self.client_input = QLineEdit(self)
        self.client_input.setStyleSheet("background-color: #FFFFFF;")

        RFC_label = QLabel("RFC:")
        RFC_label.setFont(QFont("Arial", 10))

        self.RFC_input = QLineEdit(self)
        self.RFC_input.setStyleSheet("background-color: #FFFFFF;")

        fiscal_regimen_id_label = QLabel("Fiscal Regimen:")
        fiscal_regimen_id_label.setFont(QFont("Arial", 10))

        self.fiscal_regimen_id_input = QLineEdit(self)
        self.fiscal_regimen_id_input.setStyleSheet("background-color: #FFFFFF;")

        address_label = QLabel("Address:")
        address_label.setFont(QFont("Arial", 10))

        self.address_input = QLineEdit(self)
        self.address_input.setStyleSheet("background-color: #FFFFFF;")

        city_label = QLabel("City:")
        city_label.setFont(QFont("Arial", 10))

        self.city_input = QLineEdit(self)
        self.city_input.setStyleSheet("background-color: #FFFFFF;")

        state_label = QLabel("State:")
        state_label.setFont(QFont("Arial", 10))

        self.state_input = QLineEdit(self)
        self.state_input.setStyleSheet("background-color: #FFFFFF;")

        zip_code_label = QLabel("Zip Code:")
        zip_code_label.setFont(QFont("Arial", 10))

        self.zip_code_input = QLineEdit(self)
        self.zip_code_input.setStyleSheet("background-color: #FFFFFF;")

        self.add_client_button = QPushButton("Add Client", self)
        self.add_client_button.clicked.connect(self.add_client)

        self.boton_regresar = QPushButton("Regresar al menú anterior")
        self.boton_regresar.clicked.connect(self.menu_anterior)


        layout.addWidget(main_label)
        layout.addWidget(client_label)
        layout.addWidget(self.client_input)
        layout.addWidget(RFC_label)
        layout.addWidget(self.RFC_input)
        layout.addWidget(fiscal_regimen_id_label)
        layout.addWidget(self.fiscal_regimen_id_input)
        layout.addWidget(address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(state_label)
        layout.addWidget(self.state_input)
        layout.addWidget(zip_code_label)
        layout.addWidget(self.zip_code_input)
        layout.addWidget(self.add_client_button)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - Add Client')

    def add_client(self):
        client_name = self.client_input.text()
        rfc = self.RFC_input.text()
        fiscal_regimen = self.fiscal_regimen_id_input.text()
        address = self.address_input.text()
        city = self.city_input.text()
        state = self.state_input.text()
        zip_code = self.zip_code_input.text()

        if not all([client_name, rfc, fiscal_regimen, address, city, state, zip_code]):
            QMessageBox.warning(self, 'Error', 'All fields are required.')
            return

        conn = sqlite3.connect('erp_sales.db')
        c = conn.cursor()
        
        try:
            c.execute('''INSERT INTO Clients (name, RFC, fiscal_regimen_id, address, city, state, zip_code) VALUES (?, ?, ?, ?, ?, ?, ?)''', (client_name, rfc, fiscal_regimen, address, city, state, zip_code))
            conn.commit()
            QMessageBox.information(self, 'Success', 'Client added successfully.')
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Error', 'Client already exists.')
        finally:
            conn.close()