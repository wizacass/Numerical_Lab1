def list_abs(list):
    result = []
    for x in list:
        result.append(abs(x))
    return result


def inverted(list):
    new_list = []
    for x in list:
        new_list.append(x * -1)
    return new_list


def max_negative_index(data):
    i_max, i = 0, 1
    while i < len(data):
        i_max = i if data[i] < 0 else i_max
        i = i + 1
    return i_max


def find_roots(x_min, x_max, step, accuracy, func):
    zeroes_x = []
    x = round(x_min, accuracy)
    while x < x_max:
        f1 = func(x)
        f2 = func(x + step)
        if f1 <= 0 and f2 > 0 or f1 >= 0 and f2 < 0:
            zeroes_x.append(x)

        x = round(x + step, accuracy)
    return zeroes_x
