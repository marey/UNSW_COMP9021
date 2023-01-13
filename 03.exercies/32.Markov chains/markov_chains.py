# Written by Eric Martin for COMP9021


from collections import defaultdict, Counter
from random import random, seed


def computed_markov_chain(words, n):
    counts = Counter((word[i : i + n], word[i + n])
                         for word in words if len(word) > n
                             for i in range(len(word) - n)
                    )
    # Include m-grams for m < n with the extra condition that
    # they start a word (the particular case m = 0 determines
    # the probablity that this or that letter starts a word).
    counts.update((word[: i], word[i])
                      for i in range(n)
                          for word in words if len(word) > i
                 )
    totals_for_grams = defaultdict(int)
    for gram_next_c in counts:
        totals_for_grams[gram_next_c[0]] += counts[gram_next_c]
    markov_chain = {}
    # '[' is the character after 'Z', could write instead chr(ord('Z') + 1)
    for gram, c in sorted(counts, key=lambda k: k[1] == '\n' and '[' or k[1]):
        if gram not in markov_chain:
            markov_chain[gram] = [(c, counts[gram, c])]
        elif c != '\n':
            markov_chain[gram].append((c, counts[gram, c]
                                       + markov_chain[gram][-1][1]
                                      )
                                     )
    # A gram that is a key of the dictionary
    # - either is always followed by the same symbol s, possibly
    #   '\n', in which case the value is [(s, 1.0)],
    # - or can be followed by at least 2 symbols, in which case
    #   the value contains a pair of the form (s, p) only for
    #   s different to '\n', and so the value will be a list of
    #   length 1 in the more specific case where the gram can be
    #   followed by either a given letter or '\n'.
    return {gram: [(c, count / totals_for_grams[gram])
                       for (c, count) in markov_chain[gram]
                  ] for gram in markov_chain
           }
    

def generate_word(words, markov_chain, n):
    word = ''
    while True:
        word_end = word[-n :]
        if markov_chain[word_end][0][0] == '\n':
            return word
        p = random()
        for (c, cumulative_proba) in markov_chain[word_end]:
            # Will always succeed iff word_end can only be
            # followed by one symbol and that symbol is not '\n'.
            if p < cumulative_proba:
                word += c
                break
        else:
            return word
        
          
with open('dictionary.txt') as dictionary:
    # We keep the '\n' character that ends each word read from the
    # dictionary to play the role of end of word marker.
    words = set(dictionary)
    while True:
        try:
            n = int(input('What n to use for the n-grams? '))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print('Incorrect input, try again.')               
    while True:
        try:
            nb_of_words = int(input('How many words to generate? '))
            break
        except ValueError:
            print('Incorrect input, try again.')
    while True:
        try:
            for_seed = int(input('What integer for the seed? '))
            break
        except ValueError:
            print('Incorrect input, try again.')
    markov_chain = computed_markov_chain(words, n)
    seed(for_seed)
    for _ in range(nb_of_words):
        word = generate_word(words, markov_chain, n)
        if word + '\n' in words:
            print('Rediscovered', word)
        else:
            print('Invented', word)
