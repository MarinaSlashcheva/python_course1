import sys
data = sys.stdin.read()
data = data.split('\n')

full_dic = dict.fromkeys(data[1].split(' '))
i = int(data[2])
ind = 3
while i > 0:
    dic = dict()
    string = data[ind].split(' ')
    if full_dic[string[0]] == None:
        dic = dict()
        dic[string[1]] = string[2]
        full_dic[string[0]] = dic
    else:
        var = full_dic[string[0]]
        var[string[1]] = string[2]
    ind += 1
    i -= 1
# print(full_dic)

stack = (data[1].split(' '))

ex = data[3 + int(data[2])]

for i in reversed(stack):
    left = stack
    curr_dic = full_dic[i]
    if ex not in curr_dic:
        # print('просто бросил')
        left.pop()
        continue
    if curr_dic[ex] != '_':
        ex = curr_dic[ex]
        # print("обработал и бросил")
        left.pop()
        continue
    else:
        for j in left:
            print(j, end=' ')
        break
