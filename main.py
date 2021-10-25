# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 10/25/2021
# Name: Ben Oblinski
# Description: Menu system for a text-based RPG game

# Imports the exernal files and displays
# a warining if there is a problem
try:
    import sys
    import Inventory as inv
    import Map as location
    import Characters as people
except ModuleNotFoundError:
    print("--------------------WARNING--------------------")
    print("One of the reqested files could not be imported")
else:
    print("All files were imported successfully")


def main_menu():
    """ The deafault menu text is a function.
    The menu shows you the options you can choose from.
    This function can be called by typing 'menu'
    """
    print("\n☠-----☠-----MAIN MENU-----☠-----☠")
    print("You can do any of the following actions:")
    print("-> charc----(Choose a Character to play)")
    print("-> inv------(View the items in your inventory)")
    print("-> map------(Look at your map to decide were to go)")
    print("-> quit-----(Leave the menu loop)\n")
    print("You can type 'menu' at any time to see the above list")
    print("☠-----☠-----☠-----☠-----☠\n")


# List of main weapons that the player can collect and use
primary_weapons = ["6 shooter", "tommy gun", "mauser", "sawed_off_shotgun",
                   "pump_action_shotgun", "hunting_rifle"]

# List of secondary weapons that the player can collect and use
secondary_weapons = ["Comabt Knife", "Hunting Knife", "Machete",
                     "Bullwhip", "Dynamite"]

# List of healing items the player can collect and use
healing_items = ["Bandages", "Adrealine Shot", "Disinfectant", "Health drink"]

# Print the main menu text
main_menu()

while True:

    # Asks the player to choose what they want to do
    user_input = str(input(""))

    # This code prints the list of playable characters
    # If the player types 'charc'
    if user_input == "charc":
        people.playerCharacters()

    # This code prints the map if the player types 'map'
    elif user_input == "map":
        location.playerMap()

    # This code prints the players inventory if the player types 'inv'
    elif user_input == "inv":
        inv.playerInventory()

    # If the player wants to see the main menu, print the main menu text
    elif user_input == "menu":
        main_menu()

    # If the player asks to quit, askt ehm to confirm their decesion
    elif user_input == "quit":
        print("are you sure you want to quit?")
        print("type 'y' to confrim")
        choose_to_quit = input("type any key to stay in the game\n")

        # This code shuts down the menu if the player types 'quit'
        if choose_to_quit == "y":
            print("You have left the menu")
            sys.exit()

        # This code returns to the main menu if the player decides not to quit
        else:
            print("You have choosen not to quit\n")
            main_menu()

    # This code returns an error message if the player makes a typo
    else:
        print("Invalid response. Please try a valid response.")
        print("you can type 'menu' at any time to see the list of options\n")
