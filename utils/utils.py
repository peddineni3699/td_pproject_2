# Treehouse TechDegree - Python, Unit 2: Secret Messages

import os

EXIT_ARGS = {"Q", "QUIT"}


def exit_check(choice):
    if choice in EXIT_ARGS:
        exit()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_invalid_entry_message():
    print("Invalid entry.  Please select again.\n")
