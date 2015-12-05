import re
import collections

def invert_my_dict(dict):
    inv_dict = {}
    for key in dict:
        val = dict[key]
        if val not in inv_dict:
            inv_dict[val] = [key]
        else:
            inv_dict[val].append(key)
    return inv_dict

with open('hp5.txt', 'r') as f:
    text = f.read()
all = []
all_patterns = ('whispered ([A-Z][a-z]*)', 'whispered ([A-Z][a-z]* [A-Z][a-z]*)', '([A-Z][a-z]*) whispered', '([A-Z][a-z]* [A-Z][a-z]*) whispered')
for pattern in all_patterns:
    smth = re.findall(pattern, text)
    all += smth

dict = collections.Counter(all)

inv_dict = invert_my_dict(dict)
for i in inv_dict[max(inv_dict.keys())]:
    print(dict[i], i)