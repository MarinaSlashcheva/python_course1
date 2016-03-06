# Вывести имя ошибки, которую не нужно ловить
def inherit_check(child, parent):
    if child == parent:
        return 'No'
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
#print(inherit)

already_caught = []
query = int(input())
for i in range(query):
    child = input()
    already_caught.append(child)
    for parent in already_caught:
        answer = inherit_check(child, parent)
        if answer == 'No':
            continue
        else:
            print(child)
            break

# 4
# ArithmeticError
# ZeroDivisionError : ArithmeticError
# OSError
# FileNotFoundError : OSError
# 4
# FileNotFoundError
# ArithmeticError
# ZeroDivisionError
# OSError


# This one especially tricky
# 4
# BaseException
# ValueError : BaseException
# UnicodeError : ValueError
# UnicodeEncodeError : UnicodeError
# 4
# BaseException
# ValueError
# UnicodeEncodeError
# UnicodeError


