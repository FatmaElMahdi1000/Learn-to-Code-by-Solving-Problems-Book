def common_word(m, k): #only 1 number of dataset now
    hash_table = {}
    #m = set(m)
    m_length = len(m)
    if not m_length <= 1000:
        return "ERROR: invalid dataset, out of range"
    else:

        for word in m:
            if not(len(word) <=  20):
                return "ERROR: invalid dataset"
            else:
                for char in word:
                    if not char.isalpha() and not char.lower():
                        return "ERROR: invalid dataset"
            if not word in hash_table:
                count = m.count(word)    #using count built-in function
                """
                another way of counting:
                count = 0
                for i in range(0, m_length):
                    if m[i] == word:
                        count += 1"""
                hash_table[word] = count #default value is 0
        #return hash_table
        for word, count in hash_table.items():
            if count == k:
                return word
        
#n dataset  (to run the same code on many data set, we used something called "tuple unpacking") , EX:tuple1 =  (["the", "brown", "the", "fox", "red", "the", "red"], 2) _ m: ["the", "brown", "the", "fox", "red", "the", "red"]  AND k: 2
datasets = [
    (["the", "brown", "the", "fox", "red", "the", "red"], 2),
    (["apple", "banana", "apple", "cherry", "banana"], 1),
]
for m, k in datasets:
    print(common_word(m, k))    #calling the function here 