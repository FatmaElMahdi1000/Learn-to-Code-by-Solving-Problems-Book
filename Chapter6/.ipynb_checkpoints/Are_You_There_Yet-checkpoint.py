def distance(distances):
    distances_list = list(map(int, distances.split()))
    city_positions = [0]
    grid = []
    for d in distances_list:
        city_positions.append(city_positions[-1] + d)
    #Build the 5x5 grid
    for i in range(5):
        grid.append([])
        for j in range(5):
            grid[i].append(abs(city_positions[j] - city_positions[i])) #abs - absolute value
    return grid
            
        
distances = input()
print(distance(distances))