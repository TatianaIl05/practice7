num_1 = float(input())
num_2 = float(input())
times = 0

while num_1 != 0 and num_2 != 0:
    if num_1 > num_2:
        times += 1
    num_1 = num_2
    num_2 = float(input())

print(times)
