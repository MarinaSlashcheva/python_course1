def prime(num):
    if num == 3 or num == 2:
        return True
    elif num == 1:
        return False
    else:
        import math
        last_num = int(math.sqrt(num))
        while last_num > 1:
            j = num % last_num
            if j == 0:
                return False
                break
            else:
                last_num -= 1
                if last_num > 1:
                    continue
                else:
                    return True
amount = int(input())
for i in range(amount):
    print(prime(int(input())))

