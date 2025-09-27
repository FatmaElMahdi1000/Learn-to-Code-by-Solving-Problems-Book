def smarties_eating(N, colours):
    if (0 <= N <= 200):

        hash_table_colours = {}
        while colours != 'end of box':
            if colours not in hash_table_colours:
                hash_table_colours[colours] = 1   ##7 colour counts in the outer loop.
            else:
                hash_table_colours[colours] += 1
                
            colours = input().strip().lower()
        Non_red_eating_time = 0
        red_eating_time = 0
        for key, value in hash_table_colours.items():
            if key != 'red':
                if value <= 7:
                   Non_red_eating_time = Non_red_eating_time + 13
            else:
                red_eating_time = red_eating_time + (value * 16)
        total_consumed_time = Non_red_eating_time + red_eating_time
        return total_consumed_time
                    
N = int(input())
colours = input().strip().lower()
print(smarties_eating(N, colours))