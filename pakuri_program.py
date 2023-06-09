# Project 3: Pakudex - Luis Martinez

from pakudex import Pakudex

species = None


def pakuri_program():
    print('Welcome to Pakudex: Tracker Extraordinaire!')

    while True:
        # Prompt the user to enter the max capacity
        try:
            max_capacity = int(input('Enter max capacity of the Pakudex: '))
            # Raise a ValueError when input is negative
            if max_capacity < 0:
                raise ValueError('Please enter a valid size.')
            print(f'The Pakudex can hold {max_capacity} species of Pakuri.')
            # Exit the while loop if the input for max capacity is valid
            break
        # Print an error message if an invalid max capacity is entered
        except ValueError:
            print('Please enter a valid size.')

    pakudex = Pakudex(max_capacity)
    # Keep track of the program. It will help exit the program if the user input is 6
    running_program = True
    while running_program:
        # Main menu
        print('\nPakudex Main Menu\n'
              '-----------------\n'
              '1. List Pakuri\n'
              '2. Show Pakuri\n'
              '3. Add Pakuri\n'
              '4. Evolve Pakuri\n'
              '5. Sort Pakuri\n'
              '6. Exit')
        # Prompt the user to select a menu option
        menu_option = input('\nWhat would you like to do? ')
        # Print a list of all the species
        if menu_option == '1':
            pakuri_list = pakudex.get_species_array()
            if pakuri_list is None:
                print('No Pakuri in Pakudex yet!')
            else:
                print(f'Pakuri In Pakudex:')
                for num, species in enumerate(pakuri_list, 1):
                    print(f'{num}. {species}')
        # Prompt the user to enter a species name and print its stats
        elif menu_option == '2':
            species = input('Enter the name of the species to display: ')
            stats = pakudex.get_stats(species)
            if stats is None:
                print('Error: No such Pakuri!')
            else:
                print(f'\nSpecies: {species}'
                      f'\nAttack: {stats[0]}'
                      f'\nDefense: {stats[1]}'
                      f'\nSpeed: {stats[2]}')
        # Prompt the user to enter a species name and add it to the Pakudex
        elif menu_option == '3':
            if pakudex.num_of_species == pakudex.capacity:
                print('Error: Pakudex is full!')
                continue
            species = input('Enter the name of the species to add: ')
            added_species = pakudex.add_pakuri(species)
            if added_species:
                print(f'Pakuri species {species} successfully added!')
        # Prompt the user to enter a species name and evolve it
        elif menu_option == '4':
            species = input('Enter the name of the species to evolve: ')
            evolve_species = pakudex.evolve_species(species)
            if evolve_species:
                print(f'{species} has evolved!')
            elif evolve_species is False:
                print('Error: No such Pakuri!')
        # Sort the Pakudex by species name (Python standard lexicographical order) and print a message
        elif menu_option == '5':
            sorted_list = pakudex.sort_pakuri()
            if sorted_list or pakudex.list_pakuri == []:
                print('Pakuri have been sorted!')
        # Print a goodbye message and exit the program
        elif menu_option == '6':
            print('Thanks for using Pakudex! Bye!')
            running_program = False
        else:
            # Any other input will be considered an invalid option. Will print an error message
            print('Unrecognized menu selection!')


if __name__ == '__main__':
    pakuri_program()
