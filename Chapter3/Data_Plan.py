def MB(X, N, spendingPerMonth):
    if not(1 < N <= 100) and not (1 < X <= 100) :
        return "Invaild input!"
    if not(len(spendingPerMonth) ==  N):
        return "Invalid Data!"

    R = 0 #initializing R with 0 
    
    for i in range(len(spendingPerMonth)):
        R += X
        R-= spendingPerMonth[i]
    R += X
    return R

X = int(input()) #quota_per_month 10MB for example
N = int(input()) # Number of available Month (with Data) 
spendingPerMonth = [4, 6, 2]
print(MB(X, N, spendingPerMonth))