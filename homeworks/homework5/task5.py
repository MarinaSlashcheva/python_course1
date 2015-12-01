import re
import sys

str_input = sys.stdin.read()
pattern = '([\W]+|_)'
result = re.sub(pattern, ' ', str_input)
print(result)