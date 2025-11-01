"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: De'Aundre Black
Date: 10/30/2025

AI Usage: ChatGPT helped with code structure, variable naming, and stat logic.
"""

import os

# Function 1: Character Creator
def create_character(player_name, player_class):
    """Creates a new character dictionary based on chosen class."""
    level = 1
    strength, magic, health = calculate_stats(player_class, level)

    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if player_class not in valid_classes:
        return None

    # Initial gold set to 100
    character_data = {
        "name": player_name,
        "class": player_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }
    return character_data


# Function 2: Stat Calculations
def calculate_stats(player_class, level):
    """Calculates base stats depending on class and level."""
    player_class = player_class.lower()

    # Base stats (common for all classes)
    base_strength = 5
    base_magic = 15
    base_health = 80

    if player_class == "warrior":
        base_strength += 85
        base_magic += 5
        base_health += 15
    elif player_class == "mage":
        base_strength += 30
        base_magic += 70
        base_health += 0
    elif player_class == "rogue":
        base_strength += 55
        base_magic += 25
        base_health += 10
    elif player_class == "cleric":
        base_strength += 45
        base_magic += 40
        base_health += 20
    else:
        print("Invalid class type, defaulting to Warrior.")
        return calculate_stats("Warrior", level)

    return base_strength, base_magic, base_health


# Function 3: Save Character to File
def save_character(character_data, filename):
    """Saves the character's data to a text file."""
    if not isinstance(character_data, dict) or not filename:
        return False

    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False

    with open(filename, "w") as file:
        file.write(f"Character Name: {character_data['name']}\n")
        file.write(f"Class: {character_data['class']}\n")
        file.write(f"Level: {character_data['level']}\n")
        file.write(f"Strength: {character_data['strength']}\n")
        file.write(f"Magic: {character_data['magic']}\n")
        file.write(f"Health: {character_data['health']}\n")
        file.write(f"Gold: {character_data['gold']}\n")
    return True


# Function 4: Load Character from File
def load_character(filename):
    """Loads character data from a text file into a dictionary."""
    if not os.path.exists(filename):
        return None

    with open(filename, "r") as file:
        lines = file.readlines()

    character_data = {}
    for line in lines:
        if ": " not in line:
            continue
        key, value = line.strip().split(": ", 1)
        key = key.lower().replace("character ", "")
        if value.isdigit():
            value = int(value)
        character_data[key] = value

    if len(character_data) == 0:
        return None

    return character_data


# Function 5: Display Character Information
def display_character(character_data):
    """Displays a formatted character sheet in the console."""
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character_data.get('name', '')}")
    print(f"Class: {character_data.get('class', '')}")
    print(f"Level: {character_data.get('level', 0)}")
    print(f"Strength: {character_data.get('strength', 0)}")
    print(f"Magic: {character_data.get('magic', 0)}")
    print(f"Health: {character_data.get('health', 0)}")
    print(f"Gold: {character_data.get('gold', 0)}")
    print("=======================")


# Function 6: Level Up System
def level_up(character_data):
    """Increases the character's level and recalculates stats."""
    character_data["level"] += 1
    new_strength, new_magic, new_health = calculate_stats(character_data["class"], character_data["level"])
    character_data["strength"] = new_strength
    character_data["magic"] = new_magic
    character_data["health"] = new_health

    print(f"\n{character_data['name']} leveled up to level {character_data['level']}!")


# Main Program (Testing Area)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    player_name = input("Enter your name: ")
    player_class = input("Choose your class (Warrior / Mage / Rogue / Cleric): ")

    player_character = create_character(player_name, player_class)

    if player_character is not None:
        display_character(player_character)
        level_up(player_character)
        display_character(player_character)

        save_character(player_character, "my_character.txt")
        loaded_character = load_character("my_character.txt")

        print("\nLoaded character from file:")
        display_character(loaded_character)
    else:
        print("Invalid class. Please choose Warrior, Mage, Rogue, or Cleric.")
