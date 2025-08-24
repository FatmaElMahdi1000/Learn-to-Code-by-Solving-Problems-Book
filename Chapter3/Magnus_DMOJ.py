def Honi(string):
    target = "HONI"
    idx = 0 #for tracking each char in the target. #Tracing solution 
    count = 0
    for char in string:
        if char == target[idx]:
            idx += 1
            if idx == len(target): #4
                count += 1
                idx = 0 #we need to start over from idx 0 of the target searching for our next block if any in the string 
    
    return count
    
string = input("")
print(Honi(string))