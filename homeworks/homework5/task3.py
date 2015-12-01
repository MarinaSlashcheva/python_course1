import re
import sys

data = sys.stdin.read()
data = data.split('\n')
index = 0
for string in data:
    index += 1
    check = re.findall('([\w]+) = ', string)
    if len(check) != 0:
        print(index, check[0])

