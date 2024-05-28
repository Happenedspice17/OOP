import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

class EditClientWindow(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.menu_anterior = menu_anterior
        self.edit_client_widget()

    def edit_client_widget(self):
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Edit Clients Menu")
        main_label.setFont(QFont("Arial", 16))

        name_label = QLabel(self)
        name_label.setText("Name to edit: ")
        name_label.setFont(QFont("Arial", 10))

        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT name FROM Clients")
        usernames_from_db = self.c.fetchall()
            
        self.user_input = QComboBox()
        for user_db in usernames_from_db:
            self.user_input.addItem(user_db[0])

        client_label = QLabel("New Name:")
        client_label.setFont(QFont("Arial", 10))
        self.client_input = QLineEdit(self)
        self.client_input.resize(250, 24)
        self.client_input.setStyleSheet("background-color: #FFFFFF;")

        RFC_label = QLabel("RFC:")
        RFC_label.setFont(QFont("Arial", 10))
        self.RFC_input = QLineEdit(self)
        self.RFC_input.setStyleSheet("background-color: #FFFFFF;")

        fiscalregimen_label = QLabel("Fiscal Regimen:")
        fiscalregimen_label.setFont(QFont("Arial", 10))
        self.fiscalregimen_input = QLineEdit(self)
        self.fiscalregimen_input.setStyleSheet("background-color: #FFFFFF;")

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

        self.edit_client_button = QPushButton("Edit Client", self)
        self.edit_client_button.clicked.connect(self.edit_client)

        self.boton_regresar = QPushButton("Regresar al menú anterior")
        self.boton_regresar.clicked.connect(self.menu_anterior)


        layout.addWidget(main_label)
        layout.addWidget(name_label)
        layout.addWidget(self.user_input)
        layout.addWidget(client_label)
        layout.addWidget(self.client_input)
        layout.addWidget(RFC_label)
        layout.addWidget(self.RFC_input)
        layout.addWidget(fiscalregimen_label)
        layout.addWidget(self.fiscalregimen_input)
        layout.addWidget(address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(state_label)
        layout.addWidget(self.state_input)
        layout.addWidget(zip_code_label)
        layout.addWidget(self.zip_code_input)
        layout.addWidget(self.edit_client_button)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - Edit Client')

    def edit_client(self):
        selected_client_input = self.user_input.currentText()
        client_name = self.client_input.text()
        rfc = self.RFC_input.text()
        fiscal_regimen = self.fiscalregimen_input.text()
        address = self.address_input.text()
        city = self.city_input.text()
        state = self.state_input.text()
        zip_code = self.zip_code_input.text()

        if not all([selected_client_input, client_name, rfc, fiscal_regimen, address, city, state, zip_code]):
            QMessageBox.warning(self, 'Error', 'All fields are required.')
            return

        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        
        try:
            self.c.execute('''UPDATE Clients SET name = ?, RFC = ?, fiscal_regimen_id = ?, address = ?, city = ?, state = ?, zip_code = ? WHERE name=?''',
                (client_name, rfc, fiscal_regimen, address, city, state, zip_code, selected_client_input))
            self.conn.commit()
            if self.c.rowcount == 0:
                QMessageBox.warning(self, 'Error', 'Client does not exist.')
            else:
                QMessageBox.information(self, 'Success', 'Client updated successfully.')
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'Error', f'Database error: {e}')
        finally:
            self.conn.close()