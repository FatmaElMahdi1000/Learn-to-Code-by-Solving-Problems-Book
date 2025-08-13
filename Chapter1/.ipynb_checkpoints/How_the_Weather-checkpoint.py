from math import floor, ceil #floor: rounding down , Ceil: rounding up 
def conversion(c):
    if not (-40 <= c <= 40):
        return "invalid input"
    else:
        F = (c* (9/5)) + 32
        return F
        
c = int(input())
print(conversion(c))