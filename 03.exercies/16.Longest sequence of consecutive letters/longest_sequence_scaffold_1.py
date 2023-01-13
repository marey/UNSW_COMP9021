# Prompts the user for a string w of lowercase letters and outputs the
# longest sequence of consecutive letters that occur in w,
# but with possibly other letters in between, starting as close
# as possible to the beginning of w.


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
    pass
    # Replace pass above with your code

print('The solution is:', ''.join(chr(word[start] + i)
                                      for i in range(longest_length)
                                 )

