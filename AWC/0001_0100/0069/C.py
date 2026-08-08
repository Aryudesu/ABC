N, K = map(int, input().split())
S = input()
result = 0
c = 0
d = 0
data = [0] * (N + 1)
for idx in range(N):
    d = (d + data[idx]) % 2
    s = (int(S[idx]) + d) % 2
    if s == 1:
        pass
    elif s == 0:
        if idx <= N - K:
            d = (d + 1) % 2
            data[min(idx + K, N)] += -1
            result += 1
        else:
            result = -1
            break
    else:
        raise ValueError()
print(result)
