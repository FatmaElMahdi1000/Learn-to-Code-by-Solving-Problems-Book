def correct_answers(N, correct_answer):
    if not (1 <= N < 100):
        return "Invalid Number of answers"

    Hash_table = {} 
    Adrian_correct_answers = []
    Bruno_correct_answers = []
    Goran_correct_answers = []
    
    Adrian_answer = "ABC"
    Bruno_answer = "BABC"
    Goran_answer = "CCAABB"
    
    i = 0
    while i < len(correct_answer):
        if correct_answer[i] == Adrian_answer[i % len(Adrian_answer)]:
            Adrian_correct_answers.append(correct_answer[i])
        if correct_answer[i] == Bruno_answer[i % len(Bruno_answer)]:
            Bruno_correct_answers.append(correct_answer[i])
        if correct_answer[i] == Goran_answer[i % len(Goran_answer)]:
            Goran_correct_answers.append(correct_answer[i])
        i += 1
            
    names = ['Adrian', 'Bruno', 'Goran']
    for name in names:
        if not name in Hash_table:
            Hash_table[name] = []
            if name == 'Adrian':
                Hash_table[name] = len(Adrian_correct_answers)
            elif name == 'Bruno':
                Hash_table[name] = len(Bruno_correct_answers)
            else:
                Hash_table[name] = len(Goran_correct_answers)
    max_score = max(Hash_table.values())
    print(max_score)
    winners = []
    for keys, values in Hash_table.items():
        if values == max_score:
            winners.append(keys)
    if len(winners) == 1:
        for w in winners:
            return w
    else:
        winners.sort()
        for w in winners:
            return w 
    
N = int(input())
correct_answer = input()
print(correct_answers(N, correct_answer))