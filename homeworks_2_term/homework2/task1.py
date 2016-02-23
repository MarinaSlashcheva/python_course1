def sum(a, b):
    if type(a) is not int or type(b) is not int:
        raise TypeError
    else:
        if a < 0 or b < 0:
            raise ValueError
        else:
            return int(a) + int(b)