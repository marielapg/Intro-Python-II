from room import Room

# Declare all the rooms
from player import Player
from PyInquirer import prompt
from colorama import init, Fore, Style
import os

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter your name: ")
player_one = Player(player_name, room['outside'])

start_menu = [
    {
        "type": "list",
        "name": "start",
        "message": f"Hello, {player_one.name}! Would you like to play a game?",
        "choices": ["Start", "Quit"]
    }
]

main_menu = [
    {
        "type": "list",
        "name": "menu",
        "message": f"{player_one.name}, What would you like to do?",
        "choices": ["Move", "Look", "Quit"] 
    }
]

direction_menu = [
    {
        "type": "list", 
        "name": "direction",
        "message": "Which direction",
        "choices": ["North", "South", "East", "West", "Back to Menu"],  
    }
]

command = prompt(start_menu)["start"]
direction = ""
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while not command == "Quit":
    print(Fore.LIGHTCYAN_EX + f"{player_one.name} " + Fore.RESET + f"moved {direction}")
    print(Fore.LIGHTCYAN_EX + f"{player_one.name} " + Fore.RESET + "is in the " + Fore.GREEN + f"{player_one.location.name}")
    print(Fore.YELLOW + f"{player_one.location}")

    command = prompt(main_menu)["menu"]

    if command == "Start":
        os.system("cls")
        command = prompt(main_menu)["menu"]

    if command == "Look":
        command = prompt(main_menu)["menu"]

    if command == "Move":
        direction = prompt(direction_menu)["direction"]
        if direction == "North":
            os.system("cls")
            try:
                player_one.location = player_one.location.n_to
            except:
                print(Fore.RED + "There is nowhere to go here!")
        elif direction == "East":
            os.system("cls")
            try:
                player_one.location = player_one.location.e_to
            except:
                print(Fore.RED + "There is nowhere to go here!")
        elif direction == "South":
            os.system("cls")
            try:
                player_one.location = player_one.location.s_to
            except:
                print(Fore.RED + "There is nowhere to go here!")
        elif direction == "West":
            os.system("cls")
            try:
                player_one.location = player_one.location.w_to
            except:
                print(Fore.RED + "There is nowhere to go here!")
        elif direction == "Back to Menu":
            direction = ""
            command = prompt(main_menu)["menu"]
os.system("cls")
print(Fore.RED + f"Goodbye {player_one.name}")