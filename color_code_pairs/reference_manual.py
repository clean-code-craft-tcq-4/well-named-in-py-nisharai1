MAJOR_COLORS = ['white', 'red', 'black', 'yellow', 'violet']
MINOR_COLORS = ["blue", "orange", "green", "brown", "slate"]

from get_color_code_pair import (
    get_pair_number
)


def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'


def color_number_to_string(number):
    return f'{number}'


def print_user_reference_manual():
    print("USER REFERENCE MANUAL FOR COLOR CODE\n")
    print("{:<15} {:<15} {:<5}".format('MAJOR_COLOR',
                                       'MINOR_COLOR',
                                       'NUMBER'))

    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            number = get_pair_number(major_color, minor_color)
            number = color_number_to_string(number)
            print("{:<15} {:<15} {:<5}".
                  format(major_color, minor_color, number))
