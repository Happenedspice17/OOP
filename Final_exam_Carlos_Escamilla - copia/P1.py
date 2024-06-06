from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox, QTabWidget, QComboBox, QTableView, QTableWidget, QTableWidgetItem, QHBoxLayout, QSpinBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt
import sys
import csv


#Create the class for team
class Equipo:
    def __init__(self, nombre: str, jugadores: list) -> None:
        self.nombre = nombre
        self.jugadores = jugadores

#Create the class for player
class Jugador:
    def __init__(self, nombre: str, no_playera: int, posicion: str) -> None:
        self.nombre = nombre
        self.no_playera = no_playera
        self.posicion = posicion


#Create the main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #Create the teams window

        self.equipos = [
            Equipo("Equipo 1", [Jugador("martin", 10, "medio")]), 
            Equipo("Equipo 2", [Jugador("rafa", 7, "delantero")])
            ]
        
        #Create the UI
        self.display()

    def display(self):
        # Define the width and layout
        self.setFixedWidth(500)
        self.layout = QVBoxLayout()

        #Main title
        self.main_label = QLabel(self)
        self.main_label.setText("Dream team manager")
        self.main_label.setFont(QFont("Arial", 16))

        #Label of the teams available
        self.teams_label = QLabel()
        self.teams_label.setText("Available teams:")
        self.teams_label.setFont(QFont("Arial", 10))

        # Iterate throught the index of teams
        self.user_input = QComboBox()
        for equipo in self.equipos:
            self.user_input.addItem(equipo.nombre)
        self.user_input.currentIndexChanged.connect(self.populate_team)

        # Create the table
        self.player_table = QTableWidget()
        self.player_table.setColumnCount(3)
        self.player_table.setHorizontalHeaderLabels(["Name", "Number", "Position"])
        
        # Create the button of add player
        self.add_new_player = QPushButton("Add Player", self)
        self.add_new_player.clicked.connect(self.show_add_player_form)

        # Create the button of download players list
        self.download_players = QPushButton("Download Players List", self)
        self.download_players.clicked.connect(self.download_players_list)

        # Add those to a widget for the display
        self.layout.addWidget(self.main_label)
        self.layout.addWidget(self.teams_label)
        self.layout.addWidget(self.user_input)
        self.layout.addWidget(self.player_table)
        self.layout.addWidget(self.add_new_player)
        self.layout.addWidget(self.download_players)
        
        # The display in question
        self.setLayout(self.layout)
        self.setWindowTitle("Dream team manager")
        # Run the populate team
        self.populate_team()
        self.show()

    # When run populate the table
    def populate_team(self):
        current_team_name = self.user_input.currentText()
        # itereate through the teams to update the players in the team
        for equipo in self.equipos:
            if equipo.nombre == current_team_name:
                self.update_player_table(equipo.jugadores)
                break

    # Funtion to update the player in the team
    def update_player_table(self, jugadores):
        self.player_table.setRowCount(len(jugadores))

        for i, jugador in enumerate(jugadores):
            self.player_table.setItem(i, 0, QTableWidgetItem(jugador.nombre))
            self.player_table.setItem(i, 1, QTableWidgetItem(str(jugador.no_playera)))
            self.player_table.setItem(i, 2, QTableWidgetItem(jugador.posicion))

    def show_add_player_form(self):
        current_team_name = self.user_input.currentText()

        for equipo in self.equipos:
            if equipo.nombre == current_team_name:
                self.secondary_window = AddPlayerForm(equipo, self.populate_team())
                self.secondary_window.show()
                break

    def download_players_list(self):
        current_team_name = self.user_input.currentText()

        for equipo in self.equipos:
            if equipo.nombre == current_team_name:
                file_name = f"{equipo.nombre}_players.csv"

                with open(file_name, mode='w', newline='') as file:

                    writer = csv.writer(file)
                    writer.writerow(["name", "Number", "Position"])
                    for jugador in equipo.jugadores:

                        writer.writerow([jugador.nombre, jugador.no_playera, jugador.posicion])

                QMessageBox.information(self, "Download Complete", f"Players list saved as {file_name}")
                break


class AddPlayerForm(QWidget):
    def __init__(self, equipo: Equipo):
        super().__init__()
        self.equipo = equipo
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Add Player")
        self.layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Name of the player")
        
        self.number_input = QLineEdit(self)
        self.number_input.setPlaceholderText("Number on the shirt")
        
        self.position_input = QComboBox(self)
        self.position_input.addItems(["Keeper", "Defense", "Mid", "Forward"])

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_player)
        
        self.layout.addWidget(QLabel("Name of the player:", self))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(QLabel("Shirt Number:", self))
        self.layout.addWidget(self.number_input)
        self.layout.addWidget(QLabel("Position:", self))
        self.layout.addWidget(self.position_input)
        self.layout.addWidget(self.save_button)
        
        self.setLayout(self.layout)

    def save_player(self):
        name = self.name_input.text()
        number = self.number_input.text()
        position = self.position_input.currentText()

        if not name or not number:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        if not number.isdigit():
            QMessageBox.warning(self, "Input Error", "Number must be an integer.")
            return

        number = int(number)

        for jugador in self.equipo.jugadores:
            if jugador.no_playera == number:
                QMessageBox.warning(self, "Error", "Number on shirt already exists.")
                return
        
        new_player = Jugador(name, number, position)
        self.equipo.jugadores.append(new_player)
        
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = MainWindow()
    sys.exit(app.exec())