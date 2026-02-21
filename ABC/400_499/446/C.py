from collections import deque

T = int(input())
result = []
for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    data = deque()
    for n in range(N):
        a = A[n]
        b = B[n]
        data.append((a, n))
        while b > 0:
            # print(b, data)
            num, day = data.popleft()
            if num < b:
                b -= num
            else:
                num -= b
                b = 0
                # print("debug", num, day)
                if num > 0:
                    data.appendleft((num, day))
        while True:
            if len(data) == 0:
                break
            num, day = data.popleft()
            if day < (n + 1) - D:
                continue
            data.appendleft((num, day))
            break
    res = 0
    for n, d in data:
        res += n
    result.append(res)
for r in result:
    print(r)
