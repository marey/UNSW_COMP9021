# Written by Eric Martin for COMP9021


import sys


word = input('Please input a string of lowercase letters: ')
if not all(c.islower() for c in word):
    print('Incorrect input.')
    sys.exit()
word = [ord(c) for c in word]
longest_length = 0
start = None
current_start = 0
while current_start < len(word) - longest_length:
    current_length = 1
    last_in_sequence = word[current_start]
    for i in range(current_start + 1, len(word)):
        if word[i] - last_in_sequence == 1:
            current_length += 1
            last_in_sequence = word[i]
    if current_length > longest_length:
        longest_length = current_length
        start = current_start
    current_start += 1
print('The solution is:', ''.join(chr(word[start] + i)
                                      for i in range(longest_length)
                                 )
     )
