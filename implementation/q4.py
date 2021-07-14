# implementation-4 : 게임 개발

data = []
n, m = map(int, input().split()) # map  size
a, b, d = map(int, input().split()) # (a, b): position, d: direction
for i in range(m):
    data.append(list(map(int, input().split()))) # 0: ground, 1: sea


