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
    
    next_number = 1  # machine starts at 1

    for sublist in sublists:
        take_count = sublist.count('TAKE')
        serve_count = sublist.count('SERVE')
        # 1. students late that day
        late_students = take_count
        # 2. remaining in line after desk closed
        remaining = take_count - serve_count
        if remaining < 0:
            remaining = 0  # safety

        # 3. next number for next day
        next_number += take_count
        return late_students, remaining, next_number
        
N = int(input())
commands = input()
print(analysis(N, commands))