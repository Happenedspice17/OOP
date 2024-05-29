import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt


class ViewClientWindow(QWidget):
    def __init__(self, user_id, menu_anterior):
        super().__init__()
        self.user_id = user_id
        self.view_client_widget(menu_anterior)

    def view_client_widget(self, menu_anterior):
        self.setFixedWidth(700)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("View Clients Menu")
        main_label.setFont(QFont("Arial", 16))

        display_users = QLabel(self)
        display_users.setText(self.view_clients())
        display_users.setFont(QFont("Arial", 10))

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)

        layout.addWidget(main_label)
        layout.addWidget(display_users)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - View Clients')

    def view_clients(self):
        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        self.c.execute('SELECT * FROM Clients')
        users = self.c.fetchall()
        self.log_action(self.user_id, "user_viewed", "Users", f"Users seen by id {self.user_id}")

        msg = '\n'.join([f'Name: {user[1]}, RFC: {user[2]}, Fiscal regimen: {user[3]}, Address: {user[4]}, City: {user[5]}, State: {user[6]}, Zip Code: {user[7]}' for user in users])

        return msg
    
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