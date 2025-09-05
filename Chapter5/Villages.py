def village_size(N, position):
    if not(3 < N <= 100):
        return "ERROR: invalid Range"
    else:
        villages_positions = []
        villages_positions.append(position)
        count = 1
        while count < N and (-1000000000) < position < (1000000000):
            position = int(input())
            villages_positions.append(position)
            count += 1
        sorted_villages_positions = sorted(villages_positions)

        left = (sorted_villages_positions[1] - sorted_villages_positions[0]) / 2
        right = (sorted_villages_positions[2] - sorted_villages_positions[1]) / 2
        min_size = left + right
        
        for i in range(2, N - 1):
            left = (sorted_villages_positions[i] - sorted_villages_positions[i-1]) / 2
            right = (sorted_villages_positions[i+1] - sorted_villages_positions[i]) / 2
            size = left + right
            if size < min_size:
                min_size = size
        return min_size
            
N = int(input())
position = int(input())
print(village_size(N, position))