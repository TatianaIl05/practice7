your_line = input()
final_line = ''

for index, value in enumerate(your_line, start=1):
    if index % 3 == 0:
        final_line += value

print(final_line)
