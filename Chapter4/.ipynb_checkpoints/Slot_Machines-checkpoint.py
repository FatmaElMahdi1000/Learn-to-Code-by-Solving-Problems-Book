def playing(n, first_machine, second_machine, third_machine):
    if not(1 < n <= 1000):
        return "No Quarters to play with, in the Jar!"
    Plays = 0
    machine = 0
    
    while n >= 1:
        n = n - 1#give out 1 quarter to one of the machines
        if machine == 0:
            first_machine = first_machine + 1
            if first_machine == 35:
                first_machine = 0 #re-set the machine to 0 for the next play.
                n = n + 30
        elif machine == 1:
            second_machine = second_machine + 1
            if second_machine == 100:
                second_machine = 0
                n = n + 60 
        
        elif machine == 2:
            third_machine = third_machine + 1
            if third_machine == 10:
                third_machine = 0
                n = n + 9
                
        Plays = Plays + 1
        machine = machine + 1
        if machine == 3:
            machine = 0 #re-set to 1
    return Plays, n

n = int(input())#Quarters in the Jar 
first_machine = int(input())
second_machine = int(input())
third_machine = int(input())
print(playing(n, first_machine, second_machine, third_machine))