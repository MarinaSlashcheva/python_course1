
import collections
string = input()
dict = collections.Counter(string)
l = list(dict.keys())
l = sorted(l)
for i in l:
    print(i, dict[i])