# Наследуется ли метод из другого класса, и если да, то из какого
def method_check(cl, met):
    if met in methods[cl]:
        return cl
    else:
        lookfor = inherit[cl]
        if lookfor == None:
            return None
        for name in lookfor:
            tmp = method_check(name, met)
            print(tmp, name)
            if tmp != None:
                return tmp
        return None

inherit = {}
n = int(input())
for i in range(n):
    rule = input().split(' ')
    if len(rule) == 1:
        inherit[rule[0]] = None
    else:
        rule1, shit, *rule2 = rule
        inherit[rule1] = rule2
print(inherit)
methods = dict.fromkeys(dict.keys(inherit))

m = int(input())
for j in range(m):
    key, *val = input().split(' ')
    if methods[key] != None:
        tmp = methods[key]
        tmp.append(val[0])
    else:
        methods[key] = val
print(methods)

cl, met = input().split(' ')
print(method_check(cl, met))


# 4
# D
# C : D
# B : C
# A : B
# 5
# D z
# D n
# C a
# B r
# A t
# A z