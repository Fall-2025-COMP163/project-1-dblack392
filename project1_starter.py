"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [De'Aundre Black]
Date: [10/30/2025]

AI Usage: ChatGPT helped with code structure and stat logic.
"""


def calculate_stats(character_class, level):
    #Calculates base stats based on class and level
    #Checks which class the player chose
    if character_class.lower() == "warrior":
        #Warriors have high strength and health, low magic
        strength = 10 + (level * 3)
        magic = 3 + (level * 1)
        health = 100 + (level * 10)
    elif character_class.lower() == "mage":
        #Mages have high magic, low strength, medium health
        strength = 5 + (level * 1)
        magic = 15 + (level * 4)
        health = 80 + (level * 7)
    elif character_class.lower() == "rogue":
        #Rogues have balanced stats but slightly less health
        strength = 8 + (level * 2)
        magic = 8 + (level * 2)
        health = 70 + (level * 6)
    elif character_class.lower() == "cleric":
        #Clerics have high magic and health, medium strength
        strength = 7 + (level * 2)
        magic = 12 + (level * 3)
        health = 90 + (level * 8)
    else:
        #Base stats if class not recognized
        strength = 5 + (level * 2)
        magic = 5 + (level * 2)
        health = 80 + (level * 5)
    #Returns the three stats calculated values as a tuple
    return (strength, magic, health)


def create_character(name, character_class):
    #Creates a new character dictionary with calculated stats
    #Every new character starts at level 1
    level = 1
    #Use calculate_stats() to get starting stats
    strength, magic, health = calculate_stats(character_class, level)
    #Stores all character information in a dictionary
    #Every new character starts with 100 gold
    character = {"name": name, "class": character_class, "level": level, "strength": strength, "magic": magic, "health": health, "gold": 100}
    #Returns the completed character dictionary
    return character


def save_character(character, filename):
    #Saves character to text file in specific format
    #Opens a file in write mode ("w" = overwrite or create new)
    file = open(filename, "w")
    #Write each piece of character data to the file
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    #Closes the file to save changes
    file.close()
    #Returns True to show saving was successful
    return True


def load_character(filename):
    #Loads character from text file
    #Returns: character dictionary
    #Opens the file in read mode ("r" = read only)
    file = open(filename, "r")
    #Read all lines from the file into a list
    lines = file.readlines()
    #Close the file once the data is completely collected
    file.close()
    #I created an empty dictionary to hold the data
    data = {}
    #AI helped me here
    #Goes through each line and extract the label and value
    for line in lines:
        #Split only at the first ": " to separate key and value
        if ":" in line:
            #Convert the key to lowercase and replace spaces with underscores
            key, value = line.strip().split(": ", 1)
            data[key.lower().replace(" ", "_")] = value
    #Convert number values from strings to integers
    character = {"name": data.get("character_name", "Unknown"), "class": data.get("class", "Unknown"), "level": int(data.get("level", 1)), "strength": int(data.get("strength", 0)), "magic": int(data.get("magic", 0)), "health": int(data.get("health", 0)), "gold": int(data.get("gold", 0))}
    #Return the reconstructed character dictionary
    return character


def display_character(character):
    #Prints formatted character sheet

    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=======================\n")


def level_up(character):
#Increases character level and recalculates stats
#Return the reconstructed character dictionary
#Add 1 to the current level
    character["level"] += 1
#Recalculate the stats for the new level
    strength, magic, health = calculate_stats(character["class"], character["level"])
#Update the character’s dictionary values
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
#Lets the player know they leveled up
    print(f"{character['name']} leveled up to Level {character['level']}!")


# Main testing area
if __name__ == "__main__":
    print("=== CHARACTER CREATOR TEST ===")
    char = create_character("Aria", "Mage")
    display_character(char)

    print("Saving character...")
    save_character(char, "aria.txt")

    print("Loading character...")
    loaded = load_character("aria.txt")
    display_character(loaded)

    print("Leveling up character...")
    level_up(loaded)
    display_character(loaded)