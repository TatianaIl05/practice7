n = int(input('Введите большее число: '))
questions = 0

while 2**questions < n:
    questions += 1

print(questions)
