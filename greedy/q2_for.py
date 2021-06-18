# greedy-2 : 숫자 카드 게임 (이중 for문 이용)

n, m = map(int, input().split())
result = 0


for i in range(n):
    data = list(map(int, input().split()))
    min = data[0]
    for j in range(1, m):
        if data[j] < min: min = data[j]
    if min > result: result = min

print(result)