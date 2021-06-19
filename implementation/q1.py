# implementation-1 : 상하좌우


x, y = 1, 1
move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
n = int(input())
plans = input().split()

for com in plans:
    nx = x + move[com][0]
    ny = y + move[com][1]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x = nx
    y = ny

print(f'{x} {y}')