n, k, r = map(int, input('Введите длину нити в первый день, процент и нужную длину: ').split())
days = 1

while r > n:
    days += 1
    n *= 1+k/100

print(days)
