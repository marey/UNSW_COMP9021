# Written by Eric Martin for COMP9021


letters = input('Enter uppercase letters: ')
if not all(c.isupper() for c in letters):
    letters = ''.join(c for c in letters if c.isupper())
    print(f"I only keep the uppercase letters, so work with '{letters}'.")
with open('dictionary.txt') as dictionary:
    min_length = float('inf')
    words = []
    for word in dictionary:
        if len(word) > min_length + 1:
            continue
        word = word.rstrip()
        index = 0
        for e in letters:
            index = word.find(e, index)
            if index == -1:
                break
        else:
            if len(word) < min_length:
                min_length = len(word)
                words = [word]
            elif len(word) == min_length:
                words.append(word)
if not words:
    print('No word in the dictionary embeds', letters, end='.\n')
elif len(words) == 1 and words[0] == letters:
    print(letters, 'is a word in the dictionary.')
else:
    print(f"The shortest words in the dictionary that embed '{letters}' are:")
    for word in words:
        print('   ', word)
