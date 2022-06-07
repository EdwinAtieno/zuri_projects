# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

# list containing the game sequence
game= ["R", "P", "S"]

# function to perform Rock-Paper-Scissors
def scissor_game():

    while True:
        preference = str(input("Please select one option between R, P or S\n")).upper()
        if preference in game:
            CPU= random.choice(game)
            if CPU == preference:
                print("Player ({}) : CPU ({})".format(preference, CPU))
            if CPU == "R" and preference == "S":
                print("Player ({}) : CPU ({})".format(preference, CPU))
                print("winner is CPU")
                return False
            elif CPU == "S" and preference == "R":
                print("Player ({}) : CPU ({})".format(preference, CPU))
                print("winner is player")
                return False

            elif CPU == "P" and preference == "R":
                print("Player ({}) : CPU ({})".format(preference, CPU))
                print("winner is CPU")
                return False
            elif CPU == "R" and preference == "P":
                print("Player ({}) : CPU ({})".format(preference, CPU))
                print("winner is Player")
                return False

            elif CPU == "S" and preference == "P":
                print("Player ({}) : CPU ({})".format(preference, CPU))
                print("winner is CPU")
                return False
            else:
                print("Player ({}) : CPU ({})".format(preference, CPU))
                print("winner is player")
                return False
        else:
            print("Player ({}) : CPU ({})".format(preference, CPU))
            print("Wrong selection. Please repeat again")

if __name__ == '__main__':
    scissor_game()
