import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

class DeleteClientWindow(QWidget):
    def __init__(self, user_id, menu_anterior):
        super().__init__()
        self.user_id = user_id
        self.delete_client_widget(menu_anterior)


    def delete_client_widget(self, menu_anterior):
        self.setFixedWidth(400)
        layout = QVBoxLayout()

        main_label = QLabel(self)
        main_label.setText("Delete Clients Menu")
        main_label.setFont(QFont("Arial", 16))

        user_label = QLabel(self)
        user_label.setText("Client: ")
        user_label.setFont(QFont("Arial", 10))

        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT name FROM Clients")
        usernames_from_db = self.c.fetchall()

        self.user_input = QComboBox()
        for user_db in usernames_from_db:
            self.user_input.addItem(user_db[0])

        self.delete_user_button = QPushButton("Delete Client", self)
        self.delete_user_button.clicked.connect(self.delete_client)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)

        layout.addWidget(main_label)
        layout.addWidget(user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.delete_user_button)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - Delete Client')


    def delete_client(self):
        selected_user_input = self.user_input.currentText()
        
        self.conn = sqlite3.connect('erp_sales.db')
        self.c = self.conn.cursor()
        
        try:
            self.c.execute('DELETE FROM Clients WHERE name = ?', (selected_user_input,))
            self.conn.commit()
            self.log_action(self.user_id, "user_deleted", "Users", f"User deleted by id {self.user_id}")
            QMessageBox.information(self, 'Éxito', 'User deleted succesfully')
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Error', 'User does not exist.')

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