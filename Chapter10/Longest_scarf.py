from random import random, choice #random returns floating point number(that's a real number), choice get a random element from a list for example

def Finding_the_Scarf(scarf_length, relatives_numbers,relatives_keys, relatives_colours):
    relatives_map = {}
    if not 1 <= scarf_length <= 100000:
        return "Invalid Scarf length"
        
    if not (len(relatives_keys) == relatives_numbers) or not (1 <= relatives_numbers <= 100000):
        return "Invalid Relative Numbers"
    else:
        for relative in relatives_keys:
            relatives_map[relative] = []
    if relatives_map:
        index = 0
        for index, relative in enumerate(relatives_map):
            if relatives_colours and index < len(relatives_colours):
                relatives_map[relative] = relatives_colours[index]   #another way, shortcut/shorthand is using zip() method to map two lists
    return relatives_map

def preferred_relative(chosen_relative):
    relatives_map = Finding_the_Scarf(scarf_length, relatives_numbers,relatives_keys, relatives_colours)
    for relative in relatives_map:
        if not (chosen_relative == relative) and not (chosen_relative <= len(relatives_keys)):
            return "Invalid Input, OUT OF RANGE!"
        else:
            return f"My relative number {chosen_relative}'s preferred colours are {relatives_map[relative]}"



scarf_length = int(input("Your scarf length (in feet): ")) #enter 6
relatives_colours = [["Red","Orange"], ["Red", "Yellow"], ["Blue", "White"]]
relatives_keys= [1, 2, 3]
relatives_numbers = int(input("How many relatives from which you'll choose one to send a gift: ", )) #enter 3
print(Finding_the_Scarf(scarf_length, relatives_numbers,relatives_keys, relatives_colours))
chosen_relative = int(input("Relative number: ", ))  #choose number from 1: 3
print(preferred_relative(chosen_relative))