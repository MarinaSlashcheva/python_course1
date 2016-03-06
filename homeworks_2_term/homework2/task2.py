# Наследуется ли один класс от другого - yes/no
# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A

def inherit_check(child, parent):
    if child == parent:
        return 'Yes'
    elif inherit[child] == None:
        return 'No'
    elif parent in inherit[child]:
        return 'Yes'
    else:
        for classes in inherit[child]:
            smth = inherit_check(classes, parent)
            if smth == 'Yes':
                return smth
        return smth


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

query = int(input())
for i in range(query):
    parent, child = input().split(' ')
    answer = inherit_check(child, parent)
    print(answer)
