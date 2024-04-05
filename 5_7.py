volume = int(input('Введите объём: '))

i = 1
cube_volumes = []

while i**3 <= volume:
    cube_volumes.append(i**3)
    i += 1

for item in cube_volumes:
    print(item, end=' ')
