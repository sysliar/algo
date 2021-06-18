# greedy-3 : 1이 될 때 까지

n, k = map(int, input().split())
counter = 0

while n >= k:
    a = n % k
    
    counter = counter + a # 1씩 빼는 부분
    n = n - a

    counter = counter + 1 # 나누어 떨어지는 부분
    n = n // k            # n / k 시 float 으로 변함

counter = counter + n - 1

print(f'n = {n}, counter = {counter}')
