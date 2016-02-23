import re
def foo():
    raise AssertionError

# Version 1, not really intellectual
try:
    foo()
except AssertionError:
    print('Caught AssertionError')
except MemoryError:
    print('Caught MemoryError')
except RuntimeError:
    print('Caught RuntimeError')

# Version 2, a bit better
try:
    foo()
except (AssertionError, MemoryError, RuntimeError) as error:
    x = re.findall('\w+', str(type(error)))
    print('Caught', x[1])
