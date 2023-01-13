# Written by Eric Martin for COMP9021


def month_representation_lines(starting_day, nb_of_days):
    lines = [' Mo Tu We Th Fr Sa Su ']
    line = ' ' * 3 * starting_day
    for i in range(1, nb_of_days + 1):
        line += f'{i:3}'
        starting_day = (starting_day + 1) % 7
        if starting_day == 0:
            lines.append(line + ' ')
            line = ''
    if line != '':
        line += ' ' * 3 * (7 - starting_day)
        lines.append(line + ' ')
    return lines

def reject_input():
    print('Wrong input.', end=' ')


field_width = 22
month_names = 'January', 'February', 'March', 'April','May', 'June', 'July',\
              'August', 'September', 'October', 'November', 'December'
month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print('I will display a calendar, for a year or a month in a year.\n'
      'The year should be no earlier than 1753.\n'
      "Input at least the first three letters of the month's name, if any.\n"
     )
while True:
    month = 0
    date = input('Input year, or year and month, or month and year: ')
    date = date.split()
    if not (0 < len(date) < 3):
        reject_input()
        continue
    if len(date) == 1:
        year = date[0]
    else:
        # Digits appear before letters in ascii character set.
        year, month = sorted(date)
        if len(month) < 3:
            reject_input()
            continue
        month = month.title()
        for i in range(12):
            if month_names[i].startswith(month):
                month = i
                break
        else:
            reject_input()
            continue
    try:
        year = int(year)
        if year <= 1752:
            raise ValueError
        break
    except ValueError:
        reject_input()
# Number of days between 1 January 2000 and the requested date,
# being 1 January of the requested year if no month has been
# input, positive for a date after 1 January 2000, negative for
# a date before 1 January 2000. If a month of March or later has
# been input and the input year is a leap year before 2000, then
# the assignment is incorrect by one day, which is fixed in the
# following if statement.
offset = (year - 2000) * 365\
         + (year - 1997) // 4 - (year - 1901) // 100 + (year - 1601) // 400\
         + sum(month_lengths[: month])
if month > 2 and (year % 4 == 0 and year % 100 or year % 400 == 0):
    offset += 1
# 1 January 2000 is a Saturday
starting_day = (offset + 5) % 7
if len(date) == 2:
    date = month_names[month] + ' ' + str(year)
    print()
    print(date.center(field_width))
    nb_of_days = 29 if month == 1\
                       and (year % 4 == 0 and year % 100 or year % 400 == 0)\
                    else month_lengths[month]
    for line in month_representation_lines(starting_day, nb_of_days):
        print(line)
else:
    print()
    print(str(year).center(field_width * 3 + 2))
    if year % 4 == 0 and year % 100 or year % 400 == 0:
        month_lengths[1] += 1
    months = [[month.center(field_width)] for month in month_names]
    for i in range(12):
        months[i].extend(month_representation_lines(starting_day,
                                                    month_lengths[i]
                                                   )
                        )
        starting_day = (starting_day + month_lengths[i]) % 7
    groups_of_three_months = [months[3 * i : 3 * (i + 1)] for i in range(4)]
    for group_of_three_months in groups_of_three_months:
        for month in group_of_three_months:
            month.extend([' ' * field_width]\
                                  * (max(len(g) for g in group_of_three_months)
                                     - len(month)
                                    )
                        )
        for line in zip(*group_of_three_months):
            print(' '.join(line))
