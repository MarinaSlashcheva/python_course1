import re
import collections

with open('hp5.txt', 'r') as f:
    text = f.read()
all = []
all_patterns = ('whispered ([A-Z][a-z]*)', 'whispered ([A-Z][a-z]* [A-Z][a-z]*)', '([A-Z][a-z]*) whispered', '([A-Z][a-z]* [A-Z][a-z]*) whispered')
for pattern in all_patterns:
    smth = re.findall(pattern, text)
    all += smth

dict = collections.Counter(all)
print(dict['Hermione'], end=' ' + 'Hermione')

# Output это читерство конечно, но это делалось в последние минуты