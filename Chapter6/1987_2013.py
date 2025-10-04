def distinct(starting_year):
    next_year = starting_year + 1
    while True:
        next_year_set = set(str(next_year))
        if len(next_year_set) == len(str(next_year)):
            return next_year
        else:
            next_year += 1
            
starting_year = int(input())
print(distinct(starting_year))