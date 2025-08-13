from sys import argv

script, filename = argv

with open (filename, encoding="utf-8") as txt:
    #my_text = txt.read()
    text_lines = txt.readlines() #a list of lines
    """Email Addresses cleaning"""
    
    my_set = set()  #set remove repeated inputs, it's useful for counting the number of actual email
    Email_p1 = []
    updated_Email_p1 = []
    updated_Email_p1_final = []
    Email_p2 = []
    updated_Email_p2_final = []
    
    for line1 in text_lines:
        if "@" in line1:
            idx = line1.find("@")
            Email_p1.append(line1[0:idx].lower())
            Email_p2.append(line1[idx:].strip().lower())  #strip is used here to remove the "\n" new line symbol that appears at the end. much safer
    print(Email_p2)
    for line2 in Email_p1:
        if "." in line2:
            line2 = line2.replace(".", "")
        updated_Email_p1.append(line2)
    for line3 in updated_Email_p1:
        if "+" in line3:
            plus_idx = line3.find("+")
            line3 = line3[0:plus_idx]
        updated_Email_p1_final.append(line3)
    #print(updated_Email_p1_final)  #printing first part before @
    for line4 in Email_p2:
        if line4.endswith(".com"):
            updated_line4 = line4[:-4]
            if "." in updated_line4:
                updated_line4 = updated_line4.replace(".", "")
            updated_line4 = updated_line4 + ".com"
            updated_Email_p2_final.append(updated_line4)
    #print(updated_Email_p2_final)
    for a, b in zip(updated_Email_p1_final, updated_Email_p2_final):
        combined = a + b
        my_set.add(combined)
    print(my_set)
    my_set_length = len(my_set)
    print(f"Number of actual emails = {my_set_length}")
            
    
    
 
