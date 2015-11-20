import math
with open('dict.txt', 'r') as f:
    dict = f.read()
dict = dict.split('\n')
adj = 0
noun = 0
verb = 0
for w in dict:
    if w[-2:] == 'yo':
        adj += 1
    elif w[-2:] == 'ka':
        noun += 1
    else:
        verb += 1
combinations = 0
for num in range(0, adj):
    combinations += math.factorial(adj)//math.factorial(num)
all_comb = combinations * noun * verb
print(all_comb)

