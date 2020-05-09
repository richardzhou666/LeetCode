def reverse(x):
    if x == 0 or x > (2**31) - 1 or x < -2**31:
        return 0
    absnum = abs(x)
    str_num = str(absnum)
    new = 0
    digits = []
    for i in range(len(str_num)):
        digits.append(int(str_num[i]))
    n = 0
    while n < len(str_num):
        new += 10**n * digits[n]
        n += 1
    if x < 0:
        new *= -1
    if new > 2**31 - 1 or new < -2 ** 31:
        return 0
    return new
