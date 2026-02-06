N = int(input())
A = list(map(int, input().split()))
rl = [0]
p = -1
for a in A:
    if a > p:
        rl[-1] += 1
    else:
        rl.append(1)
    p = a
result = 0
for n in rl:
    result += (n * (n + 1))//2
print(result)
