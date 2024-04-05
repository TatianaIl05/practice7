from math import sqrt

num = int(input('Введите число: '))

while int(sqrt(num)) - sqrt(num) != 0:
    print('Число не является полным квадратом')
    num = int(input('Введите другое число: '))

print(f'Число {num} является полным квадратом')
