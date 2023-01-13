# Say that two strings s_1 and s_2 can be merged into a third
# string s_3 if s_3 is obtained from s_1 by inserting
# arbitrarily in s_1 the characters in s_2, respecting their
# order. For instance, the two strings ab and cd can be merged
# into abcd, or cabd, or cdab, or acbd, or acdb..., but not into
# adbc nor into cbda.
#
# Prompts the user for 3 strings and displays the output as follows:
# - If no string can be obtained from the other two by merging,
# then the program outputs that there is no solution.
# - Otherwise, the program outputs which of the strings can be obtained
# from the other two by merging.


def can_merge(string_1, string_2, string_3):
    pass
    # Replace pass above with your code.
    # Think recursively


ranks = 'first', 'second', 'third'  
shortest, in_between, longest =\
    sorted(zip(ranks,
               (input(f'Please input the {rank} string: ') for rank in ranks),
              ), key=lambda x: len(x[1])
          )
if not longest[1]:
    print('Any string can be obtained from the other two.')
elif not shortest[1]:
    if in_between[1] == longest[1]:
        print(f'The {in_between[0]} and {longest[0]} strings can be obtained '
              'by merging the other two.'
             )
    else:
        report_failure()
elif len(longest[1]) != len(shortest[1]) + len(in_between[1])\
   or not can_merge(shortest[1], in_between[1], longest[1]):
    report_failure()
else:
    print(f'The {longest[0]} string can be obtained by merging the other two.')

    
