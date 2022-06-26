from get_color_code_pair import (
    get_color_from_pair_number,
    get_pair_number
)
from reference_manual import print_user_reference_manual


def get_color_pair(pair_number):
    major, minor = get_color_from_pair_number(pair_number)
    print(f'Color coding for {pair_number} '
          f'is {major} and {minor}')


def get_color_code(major_color, minor_color):
    pair_number = get_pair_number(major_color, minor_color)
    print(f'Color Code for {major_color} and {minor_color} '
          f'is {pair_number}')


if __name__ == '__main__':
    print_user_reference_manual()
    get_color_pair(22)
    get_color_code(
        major_color='Red',
        minor_color='Orange'
    )
