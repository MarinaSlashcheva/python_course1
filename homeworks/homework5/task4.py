import re
import sys

data = sys.stdin.read()
data = data.split('\n')
index = 0
for string in data:
    index += 1
    check = re.match(' *([\w,. ]+) = ', string)
    if check != None:
        match = list(check.groups())
        for i in match:
            exit = ' '.join(i.split(', '))
            print(index, exit)

