# Script 3 (50 pts)
# 1. Define a Videogame Class:
#     Attributes: Include attributes for title, year, genre, and platform.
#     Methods:
#         print_info(): Prints the complete information of the video game in a readable format.
# 2. Open and read the contents of videogames.csv, where each line contains details such as title, year,
# genre, and platform.
# 3. Make a function name print_list_of_videogames that takes one argument. This argument is the list
# of Videogame objects and prints each video game's details using the print_info method.
# 4. Make a function name amount_of_games_per_platform that takes one argument. This argument is
# the list of Videogame objects and prints the count of video games per platform.
# 5. Make a function called add_videogame that takes one argument. This argument is the list of
# Videogame objects.
#     This function prompts the user for details of a new video game, creates a Videogame object, and
#     appends it to the list.
# 6. Make a function called update_file that takes one argument. This argument is the list of Videogame
# objects and writes the updated list of video games back to the videogames.csv file.
# 7. Execute Functions:
#     Call print_list_of_videogames to display all video games.
#     Call amount_of_games_per_platform to see how many games each platform has.
#     Call add_videogame to add a new game to the collection.
#     Call update_file to save the updated list to the CSV file.\

import os

class Videogame:
    def __init__(self, title: str, year: int, genre: str, platform: str) -> None:
        self.title = title
        self.year = year
        self.genre =  genre
        self.platform = platform
    
    def print_info(self) -> None:
        print(f"Name: {self.title} Year: {self.year} Genre: {self.genre} Platform: {self.platform}")

games = []  # List to store the games

if os.path.isfile("C:/Users/emili/Documents/OOP/02-POO/Exam/videogames.csv"):
    with open("C:/Users/emili/Documents/OOP/02-POO/Exam/videogames.csv", "r") as file:
        for line in file:
            data = line.strip().split(",")
            videogame = Videogame(data[0], data[1], data[2], data[3])
            games.append(videogame)

def print_list_videogames(games: list[Videogame]):
    for game in games:
        game.print_info()
    print()

def amount_of_games_per_platform(games: list[Videogame]) -> None:
    platform_count = {}
    for game in games:
        if game.platform in platform_count:
            platform_count[game.platform] += 1
        else:
            platform_count[game.platform] = 1

    for platform, count in platform_count.items():
        print(f"{platform}: {count}")
    print()

def add_videogame(games: list[Videogame]) -> None:
    title = input("Enter the title of the video game: ")
    year = input("Enter the year of the video game: ")
    genre = input("Enter the genre of the video game: ")
    platform = input("Enter the platform of the video game: ")

    new_game = Videogame(title, year, genre, platform)
    games.append(new_game)

def update_file(games: list[Videogame]) -> None:
    with open("C:/Users/emili/Documents/OOP/02-POO/Exam/videogames.csv", "w") as file:
        for game in games:
            file.write(f"{game.title},{game.year},{game.genre},{game.platform}\n")

print_list_videogames(games)
amount_of_games_per_platform(games)
add_videogame(games)
update_file(games)