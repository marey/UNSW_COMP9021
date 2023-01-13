# Written by Eric Martin for COMP9021


from itertools import chain


def look_and_say(d, n):
    digits = [d]
    for i in range(n):
        boundaries = list(chain((0,), (i for i in range(1, len(digits))
                                             if digits[i] != digits[i - 1]
                                      ), (len(digits),)
                               )
                         )
        digits = list(chain(*zip((boundaries[i + 1] - boundaries[i]
                                      for i in range(len(boundaries) - 1)
                                 ), (digits[boundaries[i]]
                                         for i in range(len(boundaries) - 1)
                                    )
                                )   
                           )
                     )
    return int(''.join(str(d) for d in digits))
