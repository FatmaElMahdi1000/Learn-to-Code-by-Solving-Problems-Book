def word_count(string):
    string = string.lower()
    string_len = len(string)
    if string_len > 80:
        return "invalid input"
    else:
        cleaned_list = []
        my_list = list(string.split(" "))
        for word in my_list:
            for char in word:
                if not char.isalnum():
                    word = word.replace(char, "")
            if word: #avoid counting empty strings
                cleaned_list.append(word)
        return len(cleaned_list)
          
string = input(" ")
print(word_count(string))
