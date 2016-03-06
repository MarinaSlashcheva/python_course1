#В вашей программе будут объявлены четыре класса – A, B, C, D.
#Выведите через пробел названия классов, наследником которых является класс D.

class A:
    pass

class B:
    pass

class C:
    pass

class D(A, C):
    pass

for i in (A, B, C):
    if issubclass(D, i) == True:
        print(i.__name__, end=' ')

print(issubclass(D, D)) # TRUE