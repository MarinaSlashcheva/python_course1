numbers = [int(i) for i in input().split()]
num1 = (sorted(numbers[0:len(numbers):2]))
num2 = (sorted(numbers[1:len(numbers):2], reverse=True))

both = []
i = 0
while i < len(num1):
    both += [num1[i], num2[i]]
    i += 1

for i in both:
    print(i, end = ' ')