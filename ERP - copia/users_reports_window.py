from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QComboBox, QScrollArea
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt
import sqlite3
from datetime import datetime


class UserActivityReportWidget(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()

        self.setWindowTitle("Users Report Main Menu")

        layout = QVBoxLayout()

        self.user_activity_report_button = QPushButton("Generate User Activity Report")
        self.user_activity_report_button.clicked.connect(self.generate_user_activity_report)
        layout.addWidget(self.user_activity_report_button)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        layout.addWidget(self.scroll_area)

        self.boton_regresar = QPushButton("Return Prev Menu")
        self.boton_regresar.clicked.connect(menu_anterior)
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)

    def generate_user_activity_report(self):
        try:
            conn = sqlite3.connect('erp_sales.db')
            cursor = conn.cursor()
            cursor.execute('''
                SELECT Logs.id, Logs.user_id, Users.username, Logs.action, Logs.entity, Logs.details, Logs.timestamp
                FROM Logs
                INNER JOIN Users ON Logs.user_id = Users.id
            ''')
            logs = cursor.fetchall()

            for i in reversed(range(self.scroll_layout.count())):
                self.scroll_layout.itemAt(i).widget().setParent(None)

            report = "User Activity Report:\n\n"
            for log in logs:
                report += f"Log ID: {log[0]}, User ID: {log[1]}, Username: {log[2]}, Action: {log[3]}, Entity: {log[4]}, Details: {log[5]}, Timestamp: {log[6]}\n"
                log_label = QLabel(report)
                self.scroll_layout.addWidget(log_label)

            conn.close()
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'Error', f'Database error: {e}')

