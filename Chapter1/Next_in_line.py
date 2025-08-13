def ages(y, m):
    """
    calculating the age of the oldest child
    
    Parameters/ Args:
        y (int): yongest child's age
        m (int): middle child's age 
    Returns: 
        o (int): oldest child age or str error has been detected.
    """
    if not (0 <= y <= 50) or not (y <= m <= 50):
        return "Error: invalid ages"
    else:
        o = m + (m - y)
        return o

y = int(input())
m = int(input())
print(ages(y, m))
    