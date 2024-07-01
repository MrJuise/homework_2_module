n = int(input())
print(f'{n}:', end='')
for x1 in range(1, n):
    for x2 in range(x1 + 1, n):
        if n % (x1 + x2) == 0:
            print(f'{x1}{x2}', end='')
print()