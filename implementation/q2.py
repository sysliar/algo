# implementation-2 : 시각

n = int(input())
counter = 0

for hour in range(0, n+ 1):
    for min in range(0, 60):
        for sec in range(0, 60):
            if '3' in str(hour) + str(min) + str(sec):
                counter += 1

print(counter)
