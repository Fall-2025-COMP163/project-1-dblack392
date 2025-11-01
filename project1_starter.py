"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [De'Aundre Black]
Date: [10/30/2025]

AI Usage: ChatGPT helped with code structure and stat logic, as well as syntax.
"""

# =========================
# Function 1: Character Creator
# =========================

def create_character(name, character_class):
    """Creates a character dictionary with base stats and gold."""
    level = 1
    strength, magic, health = calculate_stats(character_class, level)

    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        return None  # Reject invalid class names

    # Character data stored in a dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }
    return character


# =========================
# Stat Calculation Function
# =========================

def calculate_stats(character_class, level):
    """Calculates character stats based on class and level."""
    character_class = character_class.lower()

    # Default base stats
    strength = 5
    magic = 15
    health = 80

    # Apply bonuses per class
    if character_class == "warrior":
        strength += 85
        magic += 5
        health += 15
    elif character_class == "mage":
        strength += 30
        magic += 70
        health += 0
    elif character_class == "rogue":
        strength += 55
        magic += 25
        health += 10
    elif character_class == "cleric":
        strength += 40
        magic += 40
        health += 10
    else:
        print("Invalid class, defaulting to Warrior.")
        return calculate_stats("Warrior", level)

    return strength, magic, health


# =========================
# Character File Saving
# =========================

def save_character(character, filename):
    """Saves the character dictionary to a text file."""
    import os

    if not isinstance(character, dict) or not filename:
        return False

    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False

    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")

    return True


# =========================
# Character Loading
# =========================

import os

def load_character(filename):
    """Loads a character dictionary from a saved text file."""
    if not os.path.exists(filename):
        return None  # Return None if file not found

    with open(filename, "r") as file:
        lines = file.readlines()

    character = {}
    for line in lines:
        if ": " not in line:
            continue  # Skip malformed lines
        key, value = line.strip().split(": ", 1)
        key = key.lower().replace("character ", "")  # Normalize keys
        if value.isdigit():
            value = int(value)
        character[key] = value

    if len(character) == 0:
        return None

    return character


# =========================
# Character Display
# =========================

def display_character(character):
    """Prints character information in a formatted sheet."""
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character.get('name', '')}")
    print(f"Class: {character.get('class', '')}")
    print(f"Level: {character.get('level', 0)}")
    print(f"Strength: {character.get('strength', 0)}")
    print(f"Magic: {character.get('magic', 0)}")
    print(f"Health: {character.get('health', 0)}")
    print(f"Gold: {character.get('gold', 0)}")
    print("=======================")


# =========================
# Level-Up Function
# =========================

def level_up(character):
    """Increases the character's level and updates stats."""
    character["level"] += 1
    s, m, h = calculate_stats(character["class"], character["level"])
    character["strength"] = s
    character["magic"] = m
    character["health"] = h
    print(f"\n{character['name']} leveled up to level {character['level']}!")


# =========================
# Testing Space
# =========================

if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    n = input("Enter your name: ")
    cls = input("What class will you choose? (Warrior/Mage/Rogue/Cleric): ")

    char = create_character(n, cls)
    if char is not None:
        display_character(char)
        level_up(char)
        display_character(char)

        save_character(char, "my_character.txt")
        loaded = load_character("my_character.txt")

        print("\nLoaded character from file:")
        display_character(loaded)
    else:
        print("Invalid class. Please choose Warrior, Mage, Rogue, or Cleric.")
