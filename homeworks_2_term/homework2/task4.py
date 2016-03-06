def foo():
    # raise AssertionError
    # raise ArithmeticError
    raise ZeroDivisionError

try:
    foo()
except AssertionError:
    print('AssertionError')
except ZeroDivisionError:
    print('ZeroDivisionError')
except ArithmeticError:
    print('ArithmeticError')
