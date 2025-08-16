from sys import argv

def file_cleaning(file_name):
    my_lines = []
    with open (file_name, "r", encoding="utf-8") as txt:
        my_text = txt.readlines()
        for line in my_text:
            line= line.strip() #removing "\n" new lines or tabs at the end or the beginning of each line
            cleaned_line = list(map(int, line.split())) #split, when splitng, we'll get each number as str, convert to int 
            #list(map(int,['5', '8']))   # → [5, 8] 
            my_lines.append(cleaned_line)
        my_lines.remove(my_lines[0])
        return(my_lines)

def optimization(intervals, Fired):
    """
    Method to take: time intervals, calculating max time units of shift coverage
    Param:
        intervals (list)
        Fired (idex) -> Desired LG to be fired
    Returns:
        covered (int): max time units of shift coverage (same output will be copied/written to another file)
    """
    covered = set() #set usage as it's gonna rm any duplicates, as LG shifts might overlap
    intervals_length = len(intervals)
    for i in range(intervals_length):
        if i != Fired:
            interval = intervals[i]
            for j in range(interval[0], interval[1]):
                covered.add(j)
    return len(covered)

def try_firing_all(intervals):
    """
    Tries firing each index in intervals and prints the coverage.
    """
    with open (output_file, "w", encoding="utf-8") as written:
        Max_coverage = 0
        for i in range(len(intervals)):
            coverage = optimization(intervals, i)  #i that's Fired in optimization method
            if coverage > Max_coverage:
                Max_coverage = coverage #override the Max_coverage value as long as there's a new coverage that's better than it.
                written.write(f"If we fire index {i}: coverage = {coverage}\n")
        written.write(f"Max_coverage = {Max_coverage}\n")
    return Max_coverage

script, file_name, output_file = argv
intervals = file_cleaning(file_name)

print(try_firing_all(intervals))
    
        




        
    