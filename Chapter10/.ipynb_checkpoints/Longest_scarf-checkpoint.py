
def scarf_hash_map(Scarf, first_colour, second_colour): #Usage of the hash maps are better for searching, running time O(1)
    """
    Method to search for our colours and specifying the long of our final scarf after trimming it off based on desired colours.
    Params: 
        Scarf -> list: Available scarf
        first_colour -> str: 1st desired colour
        second_colour -> str: 2nd desired colour
    Returns: 
        colours idcies -> int
        Updated_Scarf -> list: Available scarf after trimming it off
        length of the new scarf -> int
    """
    first_colour_index = None
    Last_colour_index = None
    
    Scarf_hash_map = {}
    for i, colour in enumerate(Scarf):
        if not i in Scarf_hash_map:
            Scarf_hash_map[i] = colour
    print(Scarf_hash_map)
    
    for index, colour in Scarf_hash_map.items():
        if colour == first_colour and first_colour_index == None:
            first_colour_index = index
    print(f"First colour position: {first_colour_index}") #first occurrence
            
    for index, colour in Scarf_hash_map.items():
        if colour == second_colour:
            Last_colour_index = index
    print(f"Second colour position: {Last_colour_index}") #first occurrence
    return f"Final scarf after trimming off the unnessary parts: {Scarf[first_colour_index: Last_colour_index + 1]}"
        
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
            return relatives_map[relative]

def The_Scarf(scarf_length):
    available_scarf = ["Red", "Blue", "White", "Yellow", "Orange", "Orange"]
    if not(len(available_scarf) == scarf_length):
        return "No scarf with the desired length, No gifts! :("
    else:
        return available_scarf
    
scarf_length = int(input("Your scarf length (in feet): ")) #enter 6
relatives_colours = [["Blue","Orange"], ["Red", "Yellow"], ["Blue", "White"]]
relatives_keys= [1, 2, 3]
relatives_numbers = int(input("How many relatives from which you'll choose one to send a gift: ", )) #enter 3
print(Finding_the_Scarf(scarf_length, relatives_numbers,relatives_keys, relatives_colours))
chosen_relative = int(input("Relative number: ", ))  #choose number from 1: 3
print(preferred_relative(chosen_relative))
print(f"Available Scarf: ",The_Scarf(scarf_length))
Scarf = The_Scarf(scarf_length)

colours = preferred_relative(chosen_relative)
first_colour = colours[0]
second_colour = colours[1]

print(scarf_hash_map(Scarf, first_colour, second_colour))