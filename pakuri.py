# Project 3: Pakudex - Luis Martinez

class Pakuri:
    # Initialize the pakuri object with species attribute
    def __init__(self, species=None, attack=None, defense=None, speed=None):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    # Returns the species of this critter
    def get_species(self):
        return self.species

    # Returns the attack value for this critter
    def get_attack(self):
        return self.attack

    # Returns the defense value for this critter
    def get_defense(self):
        return self.defense

    # Returns the speed of this critter
    def get_speed(self):
        return self.speed

    # Changes the attack value for this critter to new_attack
    def set_attack(self, new_attack):
                 self.attack = new_attack

    # Will evolve the critter as follows: a) double the attack; b) quadruple the defense; and c) triple the speed
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3

