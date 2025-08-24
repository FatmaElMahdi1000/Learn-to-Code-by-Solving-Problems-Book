from sys import argv

"""
argv explanation:
- argv[0] : script name (python program name)
- argv[1] : file to open and read
"""

def EN_OR_FR(File_name):
    with open(File_name, "r", encoding="utf-8") as txt:
        s_list = []
        t_list = []
        New_line = ""
        
        for line1 in txt:
            for char1 in line1:
                if not char1.isdigit():
                    New_line += char1
    
    for line2 in New_line:
        if 0 < len(line2) < 100:
            for char2 in line2:
                if char2 == "s" or char2 == "S":
                    s_list.append(char2)
                elif char2 == "t" or char2 == "T":
                    t_list.append(char2)
        else:
            return "invalid number of characters per line"
            
    if len(s_list) > len(t_list):
        return "French"
    elif len(s_list) < len(t_list):
        return "English"
    else:
        return "French"

script_Name , File_name = argv
print(EN_OR_FR(File_name))
