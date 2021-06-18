# greedy-2 : 큰 수의 법칙

#n, m, k = map(int, input().split()) # 공백으로 구분하여 입력
#data = list(map(int, input().split())) # 공백으로 구분하여 리스트 입력

n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]

data.sort()
first = data[-1]
second = data[-2]
result = 0

a = m // (k + 1)
b = m % (k + 1)

result = a * ((first * k) + second) + (b * first)

print(f'result = {result}')
    
