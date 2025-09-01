def analysis(N, commands):
    if not(0 < N <1000):
        return "ERROR"
    commands_lines = ""
    while commands != "EOF" and len(commands_lines) < 1000000:
        if commands.islower():
            return "ERROR"
        elif commands.isupper():
            commands_lines = commands_lines + ' ' + commands
            commands = input()
            
    cmd_list = commands_lines.strip()
    cmd_list = cmd_list.split(' ')

    sublists = []
    temp = []
    for cmd in cmd_list:
        temp.append(cmd)
        if cmd == "CLOSE":
            sublists.append(temp)  # save this chunk including CLOSE
            temp = []              # start a new one
    if temp:
        sublists.append(temp)
        
    for sublist in sublists:  ####Carry on from where you left off here...:D 
        
        
N = int(input())
commands = input()
print(analysis(N, commands))