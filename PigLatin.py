
vowels = ['a', 'e', 'i', 'o', 'u']
phrase = input("Enter Phrase: ")
words = phrase.split()
pl_words = []
i = 0

for word in words:
    if word[0] in (vowels):
        word += 'way'
        pl_words.append(word)

    else:
        for letter in word:
            if letter in vowels:
                end = word[:i]
                word = word [i:]
                word += end + 'ay'
                break
            i += 1
        pl_words.append(word)

pl_words = ' '.join(pl_words)
print (pl_words)