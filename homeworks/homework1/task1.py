word = input()
number = int(input())

if number%10 == 0 or 5<=number%100<=19 or 5<=number%10<=9 or number%100 == 0:
    if word == 'утюг':
        print(number, 'утюгов')
    else:
        print(number, 'ложек')
elif number % 10 == 1 or number % 100 == 1:
    if word == 'утюг':
        print(number, 'утюг')
    else:
        print(number, 'ложка')
elif 2<=number%10<=4 or 2<=number%100<=4:
    if word == 'утюг':
        print(number, 'утюга')
    else:
        print(number, 'ложки')

