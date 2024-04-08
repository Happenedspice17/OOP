import random
import time

class LegendaryPet:
    def _init_(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.items = []
        self.poke_counter = 0

        self.last_poke_time = None
        self.available_items = ["Sword", "Golden Apple", "Shield", "Poison", "Plague"]
        self.GoodItems = ["Sword", "Golden Apple", "Shield"]

    def eat(self):
        if self.hunger == 0:
            self.happiness -= 10
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0

    def sleep(self):
        self.energy += 50
        if self.energy > 100:
            self.energy = 100

    def use_item(self, item):
        if item in self.items:
            self.hunger -= 10
            self.energy += 10
            self.happiness += 10

            if self.energy > 100:
                self.energy = 100
            if self.happiness > 100:
                self.happiness = 100
            if self.hunger < 0:
                self.hunger = 0         
            print(f"{self.name} used {item}.")
            self.items.remove(item)
        else:
            print("Invalid item.")

    def generate_random_items(self, game_choice):
        if game_choice in ["run", "fly", "dive"]:
                item = random.choice(self.available_items)
                if item in self.GoodItems:
                  if item not in self.items:
                    self.items.append(item)
                    print(f"{self.name} found {item} during the turn.")
                elif item == "Poison" or item == "Plague":
                  print(f"{self.name} found {item} during the turn.")
                  if self.hunger !=100:
                       self.hunger += 10
                  if self.energy !=0:
                       self.energy -= 10
                  if self.happiness !=0:
                       self.happiness -= 10

    def poked(self):
        current_time = time.time()
        if self.last_poke_time is None or current_time - self.last_poke_time > 120:
            self.poke_counter = 1
        else:
            self.poke_counter += 1

        self.last_poke_time = current_time

        if self.poke_counter >= 10:
            self.happiness = 0
        else:
            self.happiness += 10

        if self.happiness > 100:
            self.happiness = 100

    def gather_food(self):
        self.energy -= 20
        if self.energy < 0:
            self.energy = 0

class Fenrir(LegendaryPet):
    def _init_(self, name):
        super()._init_(name)

    def poked(self):
        super().poked()
        print("Fenrir: Woof!")

    def run(self):
      if self.energy == 0:
          print("Fenrir cannot run because its energy is depleted.")
      else:
        self.hunger += 20
        self.energy -= 20
        if self.hunger >100 :
            self.hunger = 0
        if self.energy < 0:
            self.energy = 0

    def fenrir_says(self):
        self.hunger -= 10
        self.energy -= 10
        if self.hunger < 0:
            self.hunger = 0
        if self.energy < 0:
            self.energy = 0
        choicesfenrir = ["red", "yellow", "green"]
        choice = random.choice(choicesfenrir)
        usersays=input(f"Fenrir: Say that write:{choice}\n ")
        if choice == usersays:
            print("Fenrir: Correct!")
        else:
          print("you lose")
        
        

class Kraken(LegendaryPet):
    def _init_(self, name):
        super()._init_(name)

    def poked(self):
        super().poked()
        print("Kraken: Growl!")

    def dive(self):
      if self.energy == 0:
          print("Kraken cannot dive because its energy is depleted.")
      else:
        self.hunger += 30
        self.energy -= 30
        if self.hunger > 100:
            self.hunger = 0
        if self.energy < 0:
            self.energy = 0

    def where_is_kraken(self):
            self.hunger -= 10
            self.energy -= 10
            if self.hunger < 0:
                self.hunger = 0
            if self.energy < 0:
                self.energy = 0
            kraken_position = random.randint(1, 3)

            ktaken = int(input("Choose a number between 1 and 3 to guess where the Kraken is: "))
            while ktaken != kraken_position:
                ktaken = int(input("Incorrect guess. Please choose a number between 1 and 3 again: "))

            print("You guessed the correct position! The Kraken is in position", kraken_position)
class Dragon(LegendaryPet):
    def _init_(self, name):
        super()._init_(name)

    def poked(self):
        super().poked()
        print("Dragon: Roar!")

    def fly(self):
      if self.energy == 0:
          print("Dragon cannot fly because its energy is depleted.")
      else:
        self.hunger = 30
        self.energy -= 30
        if self.hunger > 100:
            self.hunger = 0
        if self.energy < 0:
            self.energy = 0

    def tail_claw_fang(self):
        self.hunger += 20
        self.energy -= 20
        if self.hunger > 100:
            self.hunger = 100
        if self.energy < 0:
            self.energy = 0
        choices = ["scissors", "paper", "rock"]
        selected_choice = random.choice(choices)
        user_choice = input("Enter your choice (scissors, paper, rock): ")
        if user_choice==selected_choice:
          print ("its a draw")
        elif user_choice == "scissors" and selected_choice == "paper":
          print ("you win")
        elif user_choice == "paper" and selected_choice == "rock":
          print ("you win")
        elif user_choice == "rock" and selected_choice == "scissors":
          print ("you win")
        else:
          print ("you lose")
          

def create_new_pet(existing_names):
    while True:
        pet_name = input("Enter your pet's name: ")
        if pet_name in existing_names:
            print("A pet with this name already exists. Please choose a different name.")
        else:
            existing_names.add(pet_name)
            break
    pet_type = input("Choose a pet type (Fenrir, Kraken, or Dragon): ")
    if pet_type == "Fenrir":
        return Fenrir(pet_name)
    elif pet_type == "Kraken":
        return Kraken(pet_name)
    elif pet_type == "Dragon":
        return Dragon(pet_name)
    else:
        print("Invalid pet type.")
        return None

def main_menu(pets):
    print("\nMain Menu:")
    print("1. Create a new pet")
    print("2. Continue game")
    print("3. Remove a pet")
    print("4. Exit game")

    if pets:
        print("\nYour Pets:")
        for i, pet in enumerate(pets):
            print(f"{i+1}. {pet.name}")

    choice = input("Enter your choice: ")
    return choice

def remove_pet(pets):
    if pets:
        print("\nChoose a pet to remove:")
        for i, pet in enumerate(pets):
            print(f"{i+1}. {pet.name}")

        pet_choice = int(input("Enter the number of the pet to remove: "))
        if 1 <= pet_choice <= len(pets):
            removed_pet = pets.pop(pet_choice - 1)
            print(f"{removed_pet.name} has been removed.")
            save_game(pets)
        else:
            print("Invalid pet choice.")
    else:
        print("No pets to remove.")

def save_game(pets):
    with open("saved_game.txt", "w") as file:
        for pet in pets:
            file.write(f"{pet.name},{pet._class.name_},{pet.hunger},{pet.energy},{pet.happiness}\n")

def load_game():
    pets = []
    try:
        with open("saved_game.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts[1] == "Fenrir":
                    pet = Fenrir(parts[0])
                elif parts[1] == "Kraken":
                    pet = Kraken(parts[0])
                elif parts[1] == "Dragon":
                    pet = Dragon(parts[0])
                pet.hunger = int(parts[2])
                pet.energy = int(parts[3])
                pet.happiness = int(parts[4])
                pets.append(pet)
    except FileNotFoundError:
        pass
    return pets

existing_names = set()
pets = load_game()

while True:
    choice = main_menu(pets)

    if choice == "1":
        pet = create_new_pet(existing_names)
        if pet:
            pets.append(pet)
            print("New pet created successfully!")
            save_game(pets)
    elif choice == "2":
        if pets:
            print("\nChoose a pet to continue playing:")
            for i, pet in enumerate(pets):
                print(f"{i+1}. {pet.name}")

            pet_choice = int(input("Enter the number of the pet: "))
            if 1 <= pet_choice <= len(pets):
                pet = pets[pet_choice - 1]
                game_choice = None
                while True:
                    print("\nPet Status:")
                    print("Name:", pet.name)
                    print("Hunger:", pet.hunger)
                    print("Energy:", pet.energy)
                    print("Happiness:", pet.happiness)

                    action = input("\nChoose an action (eat, sleep, use item, poke, play, save, return): ")
                    if action == "eat":
                        pet.eat()
                    elif action == "sleep":
                        pet.sleep()
                    elif action == "use item":
                        item_name = input("Enter item name: ")
                        pet.use_item(item_name)
                    elif action == "poke":
                        pet.poked()
                    elif action == "gather food":
                        pet.gather_food()
                    elif action == "play":
                        if isinstance(pet, Fenrir):
                            game_choice = input("Choose a game (FenrirSays, run): ")
                            if game_choice == "FenrirSays":
                                pet.fenrir_says()
                            elif game_choice == "run":
                                pet.run()
                            else:
                                print("Invalid game choice.")
                        elif isinstance(pet, Kraken):
                            game_choice = input("Choose a game (WhereIsKraken, dive): ")
                            if game_choice == "WhereIsKraken":
                                pet.where_is_kraken()
                            elif game_choice == "dive":
                                pet.dive()
                            else:
                                print("Invalid game choice.")
                        elif isinstance(pet, Dragon):
                            game_choice = input("Choose a game (fly, tail_claw_fang): ")
                            if game_choice == "fly":
                                pet.fly()
                            elif game_choice == "tail_claw_fang":
                                pet.tail_claw_fang()
                            else:
                                print("Invalid game choice.")
                        else:
                            print("Invalid pet type.")
                    elif action == "save":
                        save_game(pets)
                        print("Game saved successfully!")
                    elif action == "return":
                        break
                    else:
                        print("Invalid action.")

                    pet.generate_random_items(game_choice)
            else:
                print("Invalid pet choice.")
        else:
            print("No pet found. Create a new pet first.")
    elif choice == "3":
        remove_pet(pets)
    elif choice == "4":
        print("Exiting the game.")
        break
    else:
        print("Invalid choice.")