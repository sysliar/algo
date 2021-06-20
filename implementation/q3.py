# implementation-3 : 왕실의 나이트

data = input()

# 1 <= col, row <= 8
x = ord(data[0]) - ord('a') + 1 # x좌표
y = int(data[1]) # y좌표

move = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
counter = 0

for command in move:
    nx = x + command[0]
    ny = y + command[1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    counter += 1

print(counter)