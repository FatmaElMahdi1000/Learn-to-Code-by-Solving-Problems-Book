def conversion(USword):
    Words = ""
    while True:
        if USword == 'quit!' or not (0 < len(USword) <= 64):
            break
        else:
            Words = Words + "\n" + USword
        USword = input()
    Words = Words.strip().split("\n")
    Translated_Words = ""
    
    for word in Words:
        if len(word) > 4:
            if word[-2:] == 'or' and not (word[-3] in "oiuey"):
                word = word.replace('or', 'our')
                Translated_Words = Translated_Words + '\n' + word
            else:
                Translated_Words = Translated_Words + '\n' + word
        else:
            Translated_Words = Translated_Words + '\n' + word
            
    return Translated_Words
    
USword = input()
print(conversion(USword))