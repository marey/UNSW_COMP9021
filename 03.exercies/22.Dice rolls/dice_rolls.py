# Written by Eric Martin for COMP9021


from random import randint, seed

from pygal import Bar
from pygal.style import Style


input_values = input('Enter N strictly positive integers '
                     '(number of sides of N dice): '
                    ).split()
if input_values:
    dice = []
    incorrect_input = False
    for i in input_values:
        try:
            nb_of_sides = int(i)
            if nb_of_sides <= 0:
                raise ValueError
            dice.append(nb_of_sides)
        except ValueError:
            dice.append(6)
            incorrect_input = True
    if incorrect_input:
        print('Some of the values, incorrect, have been replaced '
              'with the default value of 6.'
             )
else:
    print('You did not enter any value, a single standard '
          'six-sided die will be cast.'
         )
    dice = [6]
try:
    nb_of_rolls = int(input('Enter the desired number of rolls: '))
    if nb_of_rolls < 1:
        raise ValueError
except ValueError:
    print('No valid input was provided, so the default value of '
          '1,000 will be used.'
         )
    nb_of_rolls = 1_000
try:
    for_seed = int(input('Feed the seed if desired: '))
except ValueError:
    for_seed = 0
seed(for_seed)
rolls = [sum(randint(1, nb_of_sides) for nb_of_sides in dice)
             for _ in range(nb_of_rolls)
        ]
range_of_sums = range(len(dice), sum(dice) + 1)
counts = [{'value': count, 'label': f'Frequency: {count / nb_of_rolls:.2f}'}
              for count in (rolls.count(i) for i in range_of_sums)
         ]
histogram = Bar(style=Style(colors=('#228B22',), major_label_font_size=12),
                show_legend=False
               )
histogram.title = f'Simulation for {nb_of_rolls} rolls of the dice: '\
                  f'{sorted(dice)}'
histogram.x_labels = [str(i) for i in range_of_sums]
histogram.x_title = 'Possible sums'
histogram.y_title = 'Counts'
histogram.add('', counts)
histogram.render_to_file('dice_rolls__' + '_'.join(str(die) for die in dice)
                         + f'__{nb_of_rolls}.svg'
                        )
