# Project 3: Pakudex - Luis Martinez

from pakuri import Pakuri


class Pakudex:
    # Initializes this object to contain exactly capacity objects when completely full. The default capacity for the
    # pakudex should be 20
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.num_of_species = 0
        self.list_pakuri = []

    # Returns the number of critters currently being stored in the pakudex
    def get_size(self):
        return self.num_of_species

    # Returns the number of critters that the pakudex has the capacity to hold at most
    def get_capacity(self):
        return self.capacity

    # Returns a string list containing the species of the critters as ordered in the pakudex; if there are no species
    # added yet, this method should return None
    def get_species_array(self):
        # If the number of species in the Pakudex is 0, return None
        if self.num_of_species == 0:
            return None
        # Otherwise create a list of species
        pakuri_list = []
        for pakuri in self.list_pakuri:
            species = pakuri.get_species()
            pakuri_list.append(species)
        return pakuri_list

    # Returns an int list containing the attack, defense, and speed statistics of species at indices 0, 1,
    # and 2 respectively; if species is not in the pakudex, returns None
    def get_stats(self, species):
        # Loop through each pakuri in the Pakudex
        for pakuri in self.list_pakuri:
            # If the species matches the species provided, get its stats and return them
            if pakuri.species == species:
                stats_list = []
                stats_list.append(pakuri.get_attack())
                stats_list.append(pakuri.get_defense())
                stats_list.append(pakuri.get_speed())
                return stats_list
        return None

    # Sorts the pakuri objects in this pakudex according to Python standard lexicographical ordering of species name
    def sort_pakuri(self):
        # Defines a method that sorts the list of objects in alphabetical order
        self.list_pakuri.sort(key=lambda pakuri: pakuri.species)
        return self.list_pakuri

    # Adds species to the pakudex; if successful, return True, and False otherwise
    def add_pakuri(self, species):
        # Check if there is room to add another Pakuri to the list of Pakudex
        if self.num_of_species < self.capacity:
            # Check if the Pakudex already contains a Pakuri with the given species, and prints and error message if it does
            for pakuri in self.list_pakuri:
                if pakuri.species == species:
                    print("Error: Pakudex already contains this species!")
                    return False
            add_pakuri = Pakuri(species)
            # Keep track of the number of species
            self.num_of_species += 1
            self.list_pakuri.append(add_pakuri)
            return True
        else:
            # If there is no more room for pakuri, return False
            return False

    # Attempts to evolve species within the pakudex; if successful, return True, and False otherwise
    def evolve_species(self, species):
        # Loop through each Pakuri in the Pakudex
        for pakuri in self.list_pakuri:
            # Evolve the pakuri and return its updated stats when the condition below is given
            if pakuri.species == species:
                stats_list = []
                stats_list.append(pakuri.evolve())
                return stats_list
        # Return False if no matching species is found
        return False
