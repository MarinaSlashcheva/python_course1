import sys
import re
data = sys.stdin.read()
data = data.split('\n')

cool_list = []
for number in data:
    check = re.findall('(1{3}|2{3}|3{3}|4{3}|5{3}|6{3}|7{3}|8{3}|9{3}|0{3})', number)
    if len(check) == 1:
        cool_list.append(number)
print('\n'.join(cool_list))

