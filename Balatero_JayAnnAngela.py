from Balatero_JayAnnAngela2 import Wizard, Knight, Archer, Assassin
from Balatero_JayAnnAngela1 import Character


def main():
    Char = Character()                                  # Creating a Character Object stored in Char
    Char.setClass()                                     # Setting Class of the created Character
    Char.setWeapon()                                    # Setting Weapon of the created Character
    Char.setAbilities(Char.Class)                       # Setting Abilities of the created Character based on selected Class
    Char.displayCharacterData()                         # Display Character Details


    # Added extra functions for inheritance
        # print(Char.WeaponAttack())
        # print(Char.CastAbility())

    Char.awaitContinuation()


if __name__ == '__main__':
    main()