import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox, QDialog
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

class EditUserDialog(QDialog):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Edit User")
        self.UserManagment()

    def UserManagment(self):
        layout = QVBoxLayout()

        self.editusername_label = QLabel("User to edit:")
        self.editusername_input = QComboBox()  # Cambiar a QComboBox
        self.editusername_input.setStyleSheet("background-color: #C9EBE1;")
        self.editusername_input.setFont(QFont("Times New Roman", 12))
        layout.addWidget(self.editusername_label)
        layout.addWidget(self.editusername_input)

        self.username_label = QLabel("New Username:")
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("background-color: #C9EBE1;")
        self.username_input.setFont(QFont("Times New Roman", 12))
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("New Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("background-color: #C9EBE1;")
        self.password_input.setFont(QFont("Times New Roman", 12))
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        
        # Combo box for role selection
        self.role_label = QLabel("New Role:")
        self.role_input = QComboBox()  # Change to QComboBox
        self.role_input.setStyleSheet("background-color: #C9EBE1;")
        self.role_input.setFont(QFont("Times New Roman", 12))
        self.role_input.addItems(["Sales Management", "Product Management", "Client Management"])  
        layout.addWidget(self.role_label)
        layout.addWidget(self.role_input)
        
        self.name_label = QLabel("New Name:")
        self.name_input = QLineEdit()
        self.name_input.setStyleSheet("background-color: #C9EBE1;")
        self.name_input.setFont(QFont("Times New Roman", 12))
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        
        self.lastname_label = QLabel("New Lastname:")
        self.lastname_input = QLineEdit()
        self.lastname_input.setStyleSheet("background-color: #C9EBE1;")
        self.lastname_input.setFont(QFont("Times New Roman", 12))
        layout.addWidget(self.lastname_label)
        layout.addWidget(self.lastname_input)
        
        self.add_button = QPushButton("Edit User")
        self.add_button.clicked.connect(self.edit_user)
        layout.addWidget(self.add_button)
        
        self.setLayout(layout)
        
        self.populate_users()  # Llamar a la función para llenar el QComboBox

    def populate_users(self):
        try:
            conn = sqlite3.connect('dbsales.db')
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM Users WHERE username != 'admin'")  
            usernames = cursor.fetchall()  
            self.editusername_input.addItems([user[0] for user in usernames])  # Agregar nombres de usuario al QComboBox
            conn.close()
        except sqlite3.Error as e:
            print("Error while connecting to the database:", e)

    def edit_user(self):
        editusername = self.editusername_input.currentText()  # Obtener el nombre de usuario seleccionado en el QComboBox
        username = self.username_input.text()
        password = self.password_input.text()
        role = self.role_input.currentText()  # Get selected role from ComboBox
        name = self.name_input.text()
        lastname = self.lastname_input.text()

        conn = sqlite3.connect('dbsales.db')
        cursor = conn.cursor()

        cursor.execute('''UPDATE Users SET username=?, password=?, role=?, name=?, lastname=? WHERE username=?''', (username, password, role, name, lastname, editusername))
    
        conn.commit()

        if cursor.rowcount > 0:
            QMessageBox.information(self, 'Success', 'User information updated successfully.')
            self.close()
        else:
            QMessageBox.warning(self, 'Error', 'Invalid User')

        conn.close()

if _name_ == '_main_':
    import sys
    app = QApplication(sys.argv)
    dialog = EditUserDialog()
    dialog.show()
    sys.exit(app.exec())
