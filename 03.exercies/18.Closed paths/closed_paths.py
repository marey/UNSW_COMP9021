# Written by Eric Martin for COMP9021


def closed_path(*x_y_coordinates):
    black_points = set()
    for i in range(1, len(x_y_coordinates), 2):
        y = x_y_coordinates[i]
        x_1, x_2 = sorted((x_y_coordinates[i - 1],
                           x_y_coordinates[(i + 1) % len(x_y_coordinates)]
                          )
                         )
        for x in range(x_1, x_2):
            black_points.add((2 * y - 1, 2 * x - 1))
            black_points.add((2 * y - 1, 2 * x))
        black_points.add((2 * y - 1, 2 * x + 1))
    for i in range(0, len(x_y_coordinates), 2):
        x = x_y_coordinates[i]
        y_1, y_2 = sorted((x_y_coordinates[(i - 1) % len(x_y_coordinates)],
                           x_y_coordinates[i + 1]
                          )
                         )
        for y in range(y_1, y_2):
            black_points.add((2 * y - 1, 2 * x - 1))
            black_points.add((2 * y, 2 * x - 1))
        black_points.add((2 * y + 1, 2 * x - 1))
    for y in range(2 * len(x_y_coordinates) + 1):
        for x in range(2 * len(x_y_coordinates) + 1):
            print('\N{Black Large Square}', end='')\
                    if (y, x) in black_points\
                    else print('\N{White Large Square}', end='')
        print()
