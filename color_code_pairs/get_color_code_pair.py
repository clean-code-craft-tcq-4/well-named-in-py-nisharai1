MAJOR_COLORS = ['white', 'red', 'black', 'yellow', 'violet']
MINOR_COLORS = ["blue", "orange", "green", "brown", "slate"]
TOTAL_COLOR_CODE_PAIRS = 25


def get_color_from_pair_number(pair_number):
    if pair_number > TOTAL_COLOR_CODE_PAIRS:
        raise ValueError('Pair number out of range')
    major_index = (pair_number - 1) // len(MINOR_COLORS)
    minor_index = (pair_number - 1) % len(MINOR_COLORS)
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def get_pair_number(major_color, minor_color):
    major_index = MAJOR_COLORS.index(major_color.lower())
    minor_index = MINOR_COLORS.index(minor_color.lower())
    pair_number = major_index * len(MINOR_COLORS) + minor_index + 1
    return pair_number
