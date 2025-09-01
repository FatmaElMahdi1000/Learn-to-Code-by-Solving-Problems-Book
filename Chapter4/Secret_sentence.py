def decode(encoded_sentence):
    vowels = "aeiou"
    words = encoded_sentence.strip().split()
    decoded_words = []

    for word in words:
        decoded_word = ""
        i = 0
        while i < len(word):
            decoded_word += word[i]  # add current character

            # if current char is a vowel and next two chars are 'p' + same vowel
            if i + 2 < len(word) and word[i] in vowels and word[i+1] == 'p' and word[i+2] == word[i]:
                i += 3  # skip the 'p' + repeated vowel
            else:
                i += 1

        decoded_words.append(decoded_word)

    return " ".join(decoded_words)


# Test
encoded_sentence = input()
print(decode(encoded_sentence))
