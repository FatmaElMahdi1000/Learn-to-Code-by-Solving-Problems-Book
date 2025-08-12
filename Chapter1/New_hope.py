def repeating(n):
    string = "A long time ago in a galaxy far, far away..."
    if not 1 <= n <= 5:
        return "invalid number of reps!"
    str1 = string[0:27]
    str2 = string[33:]
    i = 1
    str3 = " " 
    while i < n:
        str3 = str3 + "far, "
        i += 1
    return str1 + str3 + str2 
        
n = int(input(" "))
print(repeating(n))

print("***Another shorter solution***")
def repeating(n):
    string = "A long time ago in a galaxy far, far away..."
    if not 1 <= n <= 5:
        return "invalid number of reps!"
    return f"A long time ago in a galaxy {'far, ' * n}away..."
