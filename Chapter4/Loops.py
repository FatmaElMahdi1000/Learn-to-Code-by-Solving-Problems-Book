s = 'zephyrrr'
for i in range(0, len(s), 3): #jump by 3 steps.
    print(s[i])
print("=================================================")
for i in range(len(s) - 1, -1, -1):
    print(s[i])
print("=================================================")
string = 'ipi lipikepe yopoupu'

original = ""
i = 0 
while i < len(string):
    original = original + string[i]
    if string[i] in 'aeiou':
        i = i + 3
    else:
        i = i + 1
print(original) 

print("=================================================")
ss = 'zephyr'

i = 0
while i < len(ss):
    if ss[i] not in 'aeiou':
        i = i + 1
        continue
    else:
        print(s[i], i)
        i = i + 1
    











            






        
            