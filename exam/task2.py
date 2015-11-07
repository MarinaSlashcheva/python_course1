with open('dict.txt', 'r') as f:
    dict = f.read()
dict = dict.split('\n')
adj = []
noun = []
verb = []
for w in dict:
    if w[-2:] == 'yo':
        adj.append(w)
    elif w[-2:] == 'ka':
        noun.append(w)
    else:
        verb.append(w)

# TIME IS GOOONEEEE