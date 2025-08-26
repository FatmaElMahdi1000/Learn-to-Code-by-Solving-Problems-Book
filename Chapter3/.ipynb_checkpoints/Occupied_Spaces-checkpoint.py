def Occupied_OR_Not(N, today, yesterday): #N parking spaces
     """
    Determines how many parking spaces remain occupied on both days.

    Args:
        N (int): Total number of parking spaces (must be between 1 and 100).
        today (str): String of length N representing today's parking state 
                     ('C' for car, '.' for empty).
        yesterday (str): String of length N representing yesterday's parking state
                         ('C' for car, '.' for empty).

    Returns:
        int: Number of spaces that were occupied yesterday and are still occupied today.
        str: Error message if input values are invalid.
        """
    
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
