def plural(n, subject):
    n = n % 100
    n1 = n % 10
    if 10 < n < 20:
        return(subject[2])
    elif 1 < n1 < 5:
        return(subject[1])
    elif n1 == 1:
        return(subject[0])
    else:
        return(subject[2])
word = input()
number = int(input())
if word == 'утюг':
    word = ['утюг', 'утюга', 'утюгов']
elif word == 'чайник':
    word = ['чайник', 'чайника', 'чайников']
elif word == 'ложка':
    word = ['ложка', 'ложки', 'ложек']
else:
    word = ['гармошка', 'гармошки', 'гармошек']
x = plural(number, word)
print('%d %s' % (number, x))
