spisok = [int(i) for i in input().split()]
sp1 = []
sp2 = []
for i in spisok:
    sp1 = (sorted(spisok[0:len(spisok):2]))
for j in spisok:
    sp2 = (sorted(spisok[1:len(spisok):2], reverse=True))

both = []
i = 0
while i < len(sp1):
    both += [sp1[i], sp2[i]]
    i += 1

for i in both:
    print(i, end = ' ')