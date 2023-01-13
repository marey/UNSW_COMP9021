# Written by Eric Martin for COMP9021


from random import choice, seed


try:
    for_seed = int(input('Feed seed if desired: '))
except ValueError:
    for_seed = 0
seed(for_seed)
dice = 4, 6, 8, 12, 20
chosen_dice = choice(dice)

nb_of_simulations_to_display = 5
hypotheses_probabilities = dict.fromkeys(dice, 0.2)
outcomes_probabilities = [None] * max(dice)

while True:
    try:
        nb_of_casts = int(input('Enter the desired number of times '
                                'a randomly chosen die will be cast: '
                               )
                         )
        break
    except ValueError:
        pass
print('\nThis is a secret, but the chosen die is the one with',
      chosen_dice, 'faces.'
     )
for cast in range(nb_of_casts):
    for possible_outcome in range(max(dice)):
        outcomes_probabilities[possible_outcome] = 0
        # Let H_1, ..., H_5 be the hypotheses that the chosen die
        # has 4, 6, 8, 12, 20 sides, respectively.
        # Let D be the hypothesis that the last cast yields n for
        # a particular number n between 1 and the number of sides
        # of the chosen die. Then, denoting by p the probability
        # function,  p(D) = p(D/H_1)p(H_1) + ... + p(D/H_5)p(H_5)
        # where p(D/H_i) == 0 in case n is greater than the number
        # of sides of the die associated with H_i.
        outcomes_probabilities[possible_outcome] =\
                sum(hypotheses_probabilities[die] / die
                        for die in dice if possible_outcome < die
                   )
    number_cast = choice(range(chosen_dice))
    for die in dice:
        if number_cast >= die:           
            hypotheses_probabilities[die] = 0
        else:
            # The old value of hypotheses_probabilities[die] is
            # the prior -- p(H_i) --, and the new value of
            # hypotheses_probabilities[die] is the posterior,
            # namely, p(H_i/D). We apply Bayes rule:
            # p(H_i/D) = p(D/H_i) * p(H_i) / p(D)
            # with p(D/H_i) = 1 / dice[die]
            #      p(H_i) = hypotheses_probabilities[die]
            #      p(D) = outcomes_probabilities[number_cast]
            hypotheses_probabilities[die] =\
                    hypotheses_probabilities[die]\
                    / (die * outcomes_probabilities[number_cast])
    if cast < nb_of_simulations_to_display:
        print('\nCasting the chosen die... Outcome:', number_cast + 1)
        print('The updated dice probabilities are:')
        for die in dice:
            print(f'    {die:2}: {hypotheses_probabilities[die] * 100:.2f}%')
if nb_of_casts > nb_of_simulations_to_display:
    print('\nThe final probabilities are:')             
    for die in dice:
        print(f'    {die:2}: {hypotheses_probabilities[die] * 100:.2f}%')
