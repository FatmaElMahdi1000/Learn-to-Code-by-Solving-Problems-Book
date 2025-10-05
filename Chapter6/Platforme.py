def Pillars_Coordinates(n, coordinates_list):
    # Sort platforms by altitude (highest first)
    coordinates_list.sort(reverse=True)
    
    total_length = 0

    for i, (y, x1, x2) in enumerate(coordinates_list):
        x1 = x1 + 0.5  # left pillar coordinate 
        x2 = x2 - 0.5  # right pillar coordinate 

 
        for x in [x1, x2]:
            pillar_bottom = 0
            # Look for the first platform below that supports this pillar
            for y2, x1_below, x2_below in coordinates_list[i+1:]:
                if x1_below <= x <= x2_below:
                    pillar_bottom = y2
                    break
 
            total_length += y - pillar_bottom

    return int(total_length)


# Input reading
n = int(input())  # number of platforms
coordinates_list = [tuple(map(int, input().split())) for _ in range(n)]

print(Pillars_Coordinates(n, coordinates_list))
