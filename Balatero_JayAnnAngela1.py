import random  # Utilization of random library for randomly selecting Abilities to cast
from os import system

Customization = [  # Data Bank for all the necessary data needed (3D list)
    ["Wizard", "Knight", "Archer", "Assassin"],
    ["Wizard Staff", "Sword", "Bow & Arrow", "Katar"],
    [
        ["Energy Ball", "Dragons Breath", "Crown of Flame", "Hall Storm"],
        ["Fire Slash", "Power Slash", "Gigantic Storm", "Chaotic Disaster"],
        ["Take Aim", "Quick Shot", "Blazing Arrow", "Frost Arrow"],
        ["Cloaking", "Enchant Poison", "Sonic Acceleration", "Meteor Assault"]
    ]
]


class Character:  # Main Class having the characteristics of Class, Weapon and Abilities
    def __init__(self):
        self.Class = ""
        self.Weapon = ""
        self.Abilities = []

    @staticmethod
    def isValid(selection):  # A function for validating if the user input a number between 1 - 4
        return 0 < selection < 5

    @staticmethod  # A print function template used during the Character Customization
    def display(selection):
        print(f'\nYou chose {selection}.\n')

    @staticmethod
    def awaitContinuation():
        input("\nPress any key to continue...")

    def setClass(self):  # User Defined Method for customizing a Character Class
        system('cls')
        while True:  # Loop will continue unless a valid value is given
            try:  # Try-Except implementation for Error Handling
                print(f'Select your class:\n')
                for Class in range(4):  # Loop for displaying the 4 available classes
                    print(f'\t{Class + 1}.) {Customization[0][Class]}')  # Printing fetched from the 3D List (Databank)
                selection = int(input(f'\nEnter your class choice: '))
                if self.isValid(selection):  # Validating user input
                    chosenClass = Customization[0][selection - 1]
                    self.display(chosenClass)
                    self.Class = chosenClass  # Setting Character's class based on choice of the user
                    break
                else:
                    print("\nPick only from the available choices. [1 - 4]\n")
            except ValueError:  # Exception for invalid value input
                print("\nOnly numerical characters are allowed.\n")
        self.awaitContinuation()
        system('cls')

    def setWeapon(self):  # User Defined Method for customizing a Character Weapon
        system('cls')
        while True:  # Loop will continue unless a valid value is given
            try:  # Try-Except implementation for Error Handling
                print(f'Select your weapon:\n')
                for Weapon in range(4):  # Loop for displaying the 4 available classes
                    print(f'\t{Weapon + 1}.) {Customization[1][Weapon]}')  # Printing fetched data from the 3D List (Databank)
                selection = int(input(f'\nEnter your weapon choice: '))
                if self.isValid(selection):  # Validating user input
                    chosenWeapon = Customization[1][selection - 1]
                    self.display(chosenWeapon)
                    self.Weapon = chosenWeapon  # Setting Character's weapon based on choice of the user
                    break
                else:
                    print("\nPick only from the available choices. [1 - 4]\n")
            except ValueError:  # Exception for invalid value input
                print("\nOnly numerical characters are allowed.\n")

        self.awaitContinuation()

    def setAbilities(self, selectedClass):  # User Defined Method for customizing a Character Abilities
        Abilities = ["", "", ""]  # List that acts as a container for the selected abilities
        system('cls')
        while True:  # Loop will continue unless a valid value is given
            try:
                Class = Customization[0].index(selectedClass)
                print(f'Select 3 abilities:\n')
                for Ability in range(4):
                    print(
                        f'\t{Ability + 1}.) {Customization[2][Class][Ability]}')  # Printing fetched data from the 3D List (Databank)
                print("")
                for ability in range(3):  # Looping 3 times asking for 3 desired abilities
                    if Abilities[ability] == "":
                        while True:
                            selectedAbility = int(input(f'Desired Ability {ability + 1}: '))
                            if self.isValid(selectedAbility):  # Validating user input
                                Ability = Customization[2][Class][selectedAbility - 1]
                                if Ability not in Abilities:  # Validating if selected ability has not been selected yet to avoid repetition
                                    Abilities[ability] = Ability
                                    break
                                else:
                                    print("\nThat skill has been already selected, pick another one.")
                            else:
                                print("\nPick only from the available choices. [1 - 4]\n")
                    else:
                        pass

                self.display(Abilities)
                self.Abilities = Abilities  # Setting Character's abilities based on choice of the user
                break
            except ValueError:  # Exception for invalid value input
                print("\nOnly numerical characters are allowed.\n")

        self.awaitContinuation()
        system('cls')

    def WeaponAttack(self):  # Extra method behavior for the Character Class
        return "Charge Attack"

    def CastAbility(self):  # Extra method behavior for the Character Class
        return self.Abilities[random.randint(0, 3)]

    def displayCharacterData(self):  # Method for displaying the results of character customization
        print(f'------------------------------MY CHARACTER-------------------------------\n'
              f'|                                                                       |\n'
              f'\t\t\tClass:\t\t{self.Class}                                             \n'
              f'|                                                                       |\n'
              f'-------------------------------------------------------------------------\n'
              f'|                                                                       |\n'
              f'\t\t\tWeapon:\t\t{self.Weapon}                                           \n'
              f'|                                                                       |\n'
              f'-------------------------------------------------------------------------\n'
              f'|                                                                       |\n'
              f'\t\t\t\tABILITIES\n'
              f'\n\t\t\tAbility 1:\t{self.Abilities[0]}'
              f'\n\t\t\tAbility 2:\t{self.Abilities[1]}'
              f'\n\t\t\tAbility 3:\t{self.Abilities[2]}\n'
              f'|                                                                       |\n'
              f'-------------------------------------------------------------------------\n')
