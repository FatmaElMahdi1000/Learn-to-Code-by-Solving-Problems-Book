def when(P, N, R):
    day = 1
    total = N # cumulative total so far
    while total <= P:
        N = N * R
        day_count += 1
    return day


P = int(input())
N = int(input())
R = int(input())
print(when(P, N, R))