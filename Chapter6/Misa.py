from sys import exit

def shaking_hands(benchs):

    Row = len(benchs)
    Col = len(benchs[0])

    Hand_shakes = 0 
    for i in Row:
        for j in Col:
            if benchs[i][j] == "o":
                #checking Right direction
                if j + 1 < Col and benchs[i][j + 1] == "o":
                    Hand_shakes += 1
                #checking down direction 
                elif i + 1 < Row and benchs[i+1][j] == 'o':
                    Hand_shakes += 1
                #down right 
                elif i + 1 < Row and j + 1 < Col and benchs[i + 1][j + 1] == 'o':
                    Hand_shakes += 1
                elif i + 1 < Row and j - 1 >= 0 and benchs[i + 1][j - 1] == 'o':
                    Hand_shakes += 1
    return Hand_shakes

def available_benchs(R, S):
    if not(1 <= R <= 50) and not(1 <= S <= 50):
        exit(1)
    else:
        Grid = []
        for i in range(R): #rows
            row = input()
            grid = list(map(str, row.split()))
            Grid.append(grid)
            for sublist in Grid:
                if len(sublist) > S:
                    return "Error: No seats available"
        return Grid
            
R = int(input())
S = int(input())

benchs = available_benchs(R, S)
print(shaking_hands(benchs))

