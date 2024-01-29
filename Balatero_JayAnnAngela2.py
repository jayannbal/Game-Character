from Balatero_JayAnnAngela1 import Character                       # Calling Main Class for Derived Class Inheriting


class Wizard(Character):                                # Wizard Class
    def __init__(self):
        super().__init__()                              # Referring to the Parent Class and Initializing based on it

    def WeaponAttack(self):                             # Overriding the based WeaponAttack method behavior specifically for Wizard
        return "Casting Magic Attack!"


class Knight(Character):                                # Knight Class
    def __init__(self):
        super().__init__()                              # Referring to the Parent Class and Initializing based on it

    def WeaponAttack(self):                             # Overriding the based WeaponAttack method behavior specifically for Knight
        return "Slashing Heavy Blows!"


class Archer(Character):                                # Archer Class
    def __init__(self):
        super().__init__()                              # Referring to the Parent Class and Initializing based on it

    def WeaponAttack(self):                             # Overriding the based WeaponAttack method behavior specifically for Archer
        return "Shooting Arrows!"


class Assassin(Character):                              # Assassin Class
    def __init__(self):
        super().__init__()                              # Referring to the Parent Class and Initializing based on it

    def WeaponAttack(self):                             # Overriding the based WeaponAttack method behavior specifically for Assassin
        return "Quick Silent Slashes!"