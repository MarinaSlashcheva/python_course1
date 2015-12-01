import sys
import re
data = sys.stdin.read()
you = re.findall('you', data)
print(len(you))