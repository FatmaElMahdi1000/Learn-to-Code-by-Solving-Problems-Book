def validOrNot(password):
    if not (8 <= len(password) <= 12):
        return "Invalid"
    else:
        lower_case_letters = []
        upper_case_letters = []
        digits = []
        digit_length = []
    
        for digit in range(0, 10):
            digits.append(str(digit))
            
        for char in password:
            if char.islower():
                lower_case_letters.append(char)
            if char.isupper():
                upper_case_letters.append(char) 
            if char in digits:
                digit_length.append(char)
        
        if not (len(lower_case_letters) >= 3):
            return "Invalid"
            
        elif not (len(upper_case_letters) >= 2):
            return "Invalid"
            
        elif not (len(digit_length) > 1 or len(digit_length) == 1):
            return "Invalid"
        else:
            return "Valid"
            
password = input("")
print(validOrNot(password))