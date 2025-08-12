def spookiness_measurement(s):
    if not 2 <= s <= 20:
        return "invalid: incantation! :P"
    else:
        string = 'o' * s
        incantation = 'sp' + string + 'ky'
        return incantation
s = int(input())
print(spookiness_measurement(s))