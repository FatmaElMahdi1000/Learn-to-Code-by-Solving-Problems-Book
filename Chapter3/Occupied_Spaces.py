def Occupied_OR_Not(N, today, yesterday): #N parking spaces
    if not (0 < N <= 100):
        return "Something wrong about your input"
    elif (0 < N <= 100) and (len(today) == N) and (len(yesterday) == N):
        Cs_today = list(today) 
        Cs_yesterday = list(yesterday)

        Final = [] 
        idx1 = []
        idx2 = []
        for index1, char1 in enumerate(Cs_today):
            if char1 == 'C':
                idx1.append(index1)
        for index2, char2 in enumerate(Cs_yesterday):
            if char2 == 'C':
                idx2.append(index2)

        for num1 in idx1:
            for num2 in idx2:
                if num1 == num2:
                    Final.append(num1)
        return len(Final)
                    
N = int(input()) 
today = (input())
yesterday = (input())
print(Occupied_OR_Not(N, today, yesterday))
