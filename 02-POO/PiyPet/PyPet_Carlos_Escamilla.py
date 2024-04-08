from datetime import datetime
import random
import json

class Item:
  def __init__(self, name, item_type, effect_value):
    self.name = name
    self.item_type = item_type  # "good" or "bad"
    self.effect_value = effect_value

class LegendaryPet:
  def __init__(self, name, species, hunger=50, energy=50, happiness=50, items=[]):
    self.name = name
    self.species = species
    self.hunger = hunger
    self.energy = energy
    self.happiness = happiness
    self.items = items
    self.last_poked = datetime.now()

  def eat(self, food_amount):
    self.hunger = max(0, self.hunger - food_amount)

  def sleep(self, sleep_duration):
    self.energy = min(100, self.energy + sleep_duration * 10)

  def use_item(self, item):
    if item.item_type == "good":
      self.hunger = max(0, self.hunger - item.effect_value)
      self.energy = min(100, self.energy + item.effect_value)
      self.happiness = min(100, self.happiness + item.effect_value)
      print(f"{self.name} likes {item.name}!")
    else:
      self.hunger = min(100, self.hunger + item.effect_value)
      self.energy = max(0, self.energy - item.effect_value)
      self.happiness = max(0, self.happiness - item.effect_value)
      print(f"{self.name} doesn't like {item.name}!")
    self.items.remove(item)

  def poked(self):
    time_diff = (datetime.now() - self.last_poked).seconds // 60
    if time_diff <= 2 and self.happiness + 5 <= 100:
      self.happiness += 5
    elif time_diff <= 2:
      print(f"{self.name} doesn't like being poked so much!")
      self.happiness = max(0, self.happiness - 2)
    self.last_poked = datetime.now()

  def gather_food(self):
    self.energy = max(0, self.energy - 20)
    if random.randint(1, 3) == 1:
      food_item = Item("Meat", "good", 30)
      self.items.append(food_item)
      print(f"{self.name} found some {food_item.name}!")
    else:
      print(f"{self.name} couldn't find any food this time.")

class Fenrir(LegendaryPet):
  def run(self):
    self.energy = max(0, self.energy - 30)
    if random.randint(1, 4) == 1:
      bone_item = Item("Bone", "good", 20)
      self.items.append(bone_item)
      print(f"{self.name} found a {bone_item.name} while scavenging!")
    else:
      rotten_item_bad = Item("Rotten meat", "bad", -30)
      self.items.append(rotten_item_bad)
      self.use_item(rotten_item_bad)
      print(f"{self.name} soared through the skies and went wrong")

  def fenrir_says(self):
    actions = ["Scratch", "Rollover", "Shake"]
    correct_action = random.choice(actions)
    player_choice = input(f"Fenrir Says: {correct_action}. Do it! (Type {correct_action.lower()}):")
    if player_choice.lower() == correct_action.lower():
      self.happiness = min(100, self.happiness + 10)
      self.hunger = max(0, self.hunger - 15)
      self.energy = max(0, self.energy - 10)
      print(f"Good job! {self.name} is happy!")
    else:
      self.happiness = max(0, self.happiness - 5)
      self.hunger = min(100, self.hunger + 10)
      self.energy = max(0, self.energy - 5)
      print(f"Wrong! {self.name} feels a bit confused.")
    self.last_poked = datetime.now()  # Reset poke timer since interaction happened

class Kraken(LegendaryPet):
  def dive(self):
    self.energy = max(0, self.energy - 40)
    if random.randint(1, 5) == 1:
      treasure_item = Item("Shiny Pearl", "good", 50)
      self.items.append(treasure_item)
      print(f"{self.name} found a treasure - {treasure_item.name} during its dive!")
    else:
      mate_pearl = Item("Mate Pearl", "bad", -30)
      self.items.append(mate_pearl)
      self.use_item(mate_pearl)
      print(f"{self.name} soared through the skies and went wrong")

  def where_is_kraken(self):
    locations = ["Coral Reef", "Sunken Ship", "Hydrothermal Vent"]
    correct_location = random.choice(locations)
    player_choice = input(f"Where is Kraken hiding? (Choose from: {', '.join(locations)}):")
    if player_choice == correct_location:
      self.happiness = min(100, self.happiness + 15)
      self.hunger = max(0, self.hunger - 20)
      self.energy = max(0, self.energy - 15)
      print(f"You found {self.name}! They are happy you remembered.")
    else:
      self.happiness = max(0, self.happiness - 10)
      self.hunger = min(100, self.hunger + 15)
      self.energy = max(0, self.energy - 10)
      print(f"Wrong spot! {self.name} feels a bit forgotten.")

class Dragon(LegendaryPet):
  def fly(self):
    self.energy = max(0, self.energy - 50)
    if random.randint(1, 6) == 1:
      gem_item = Item("Fire Opal", "good", 30)
      self.items.append(gem_item)
      print(f"{self.name} found a rare gem - {gem_item.name} during its flight!")
    else:
      gem_item_bad = Item("Coral Opal", "bad", -30)
      self.items.append(gem_item_bad)
      self.use_item(gem_item_bad)
      print(f"{self.name} soared through the skies and went wrong")

  def tail_claw_fang(self):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    player_choice = input(f"Tail, Claw, or Fang? (Choose {', '.join(options)}):")
    if player_choice.lower() == computer_choice.lower():
      print(f"It's a tie! {self.name} is playful.")
    elif (player_choice.lower() == "rock" and computer_choice.lower() == "scissors") or (
        player_choice.lower() == "paper" and computer_choice.lower() == "rock") or (
        player_choice.lower() == "scissors" and computer_choice.lower() == "paper"):
      self.happiness = min(100, self.happiness + 20)
      self.hunger = min(100, self.hunger + 10)
      self.energy = max(0, self.energy - 20)
      print(f"You win! {self.name} is very happy!")
    else:
      self.happiness = max(0, self.happiness - 15)
      self.hunger = min(100, self.hunger + 20)
      self.energy = max(0, self.energy - 30)
      print(f"You lose! {self.name} teases you a bit.")

def save_pet(pet):
  """Saves the pet's data to a JSON file."""
  data = {
      "name": pet.name,
      "species": pet.species,
      "hunger": pet.hunger,
      "energy": pet.energy,
      "happiness": pet.happiness,
      "items": [item.name for item in pet.items],  # Save only item names
  }
  with open("pet_data.json", "w") as outfile:
    json.dump(data, outfile, indent=4)  # Save data with indentation

def load_pet():
  """Loads the pet's data from a JSON file if it exists."""
  try:
    with open("pet_data.json", "r") as infile:
      data = json.load(infile)
    pet_name = data["name"]
    pet_species = data["species"]
    hunger = data["hunger"]
    energy = data["energy"]
    happiness = data["happiness"]
    items = [Item(item_name, "good", 0) for item_name in data["items"]]  # Create basic items
    return LegendaryPet(pet_name, hunger, energy, happiness, items)
  except FileNotFoundError:
    print("No saved pet data found. Starting a new pet.")
    return None

# Game flow logic for starting the game, interacting with the pet, saving/loading

def main():
  print("Welcome to the Legendary Pet Game!")
  # Load existing pet or create a new one
  load_or_new = input("Do you want to load an existing pet (L) or create a new one (N)? ")
  if load_or_new.upper() == "L":
    if load_or_new.upper() == "L":
      pet = load_pet()
      if not pet:
        # No saved data, start a new pet
        pet_name = input("What is your pet's name? ")
        pet_type = input("Choose your pet: (F)enrir, (K)raken, or (D)ragon: ").upper()
        # Create pet object based on chosen type
        if pet_type == "F":
          pet = Fenrir(pet_name, "Fenrir")
        elif pet_type == "K":
          pet = Kraken(pet_name, "Kraken")
        elif pet_type == "D":
          pet = Dragon(pet_name, "Dragon")
        else:
          print("Invalid choice. Please choose F, K, or D.")
          exit()
  else:
    pet_name = input("What is your pet's name? ")
    pet_type = input("Choose your pet: (F)enrir, (K)raken, or (D)ragon: ").upper()
    # Create pet object based on chosen type
    if pet_type == "F":
      pet = Fenrir(pet_name, "Fenrir")
    elif pet_type == "K":
      pet = Kraken(pet_name, "Kraken")
    elif pet_type == "D":
      pet = Dragon(pet_name, "Dragon")
    else:
      print("Invalid choice. Please choose F, K, or D.")
      exit()

  # Game loop for interacting with the pet
  while True:
    print("\nWhat would you like to do?")
    print("1. Eat")
    print("2. Sleep")
    print("3. Use Item")
    print("4. Poke")
    print("5. Gather Food")
    print("6. Play")  # Specific action for each pet type
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
      food_amount = int(input("How much food do you want to give " + pet.name + "? "))
      pet.eat(food_amount)
      print(f"{pet.name}'s hunger is now {pet.hunger}.")
    elif choice == "2":
      sleep_duration = int(input(f"How many hours do you want {pet.name} to sleep? "))
      pet.sleep(sleep_duration)
      print(f"{pet.name}'s energy is now {pet.energy}.")
    elif choice == "3":
      if not pet.items:
        print(f"{pet.name} doesn't have any items.")
      else:
        print("Items:")
        for i, item in enumerate(pet.items):
          print(f"{i+1}. {item.name}")
        item_choice = int(input("Choose an item to use (1-" + str(len(pet.items)) + "): "))
        if 1 <= item_choice <= len(pet.items):
          pet.use_item(pet.items[item_choice - 1])
        else:
          print("Invalid choice.")
    elif choice == "4":
      pet.poked()
      print(f"{pet.name}'s happiness is now {pet.happiness}.")
    elif choice == "5":
      if pet.species == "Fenrir":
        pet.run()
      elif pet.species == "Kraken":
        pet.dive()
      elif pet.species == "Dragon":
        pet.fly()
    elif choice == "6":
      if pet.species == "Fenrir":
        pet.fenrir_says()
      elif pet.species == "Kraken":
        pet.where_is_kraken()
      elif pet.species == "Dragon":
        pet.tail_claw_fang()
    elif choice == "7":
      save_pet(pet)
      print(f"Game saved! You can continue playing with {pet.name} later.")
      break
    else:
      print("Invalid choice. Please choose a number between 1 and 8.")

if __name__ == "__main__":
  main()