N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
A.sort()
All = sum(A)
NumLis = dict()
prev = A[0]
NumLis[A[0]] = 0
key = A[0]
is_connect = True
for a in A:
    if a != prev and a != prev + 1:
        is_connect = False
        key = a
        NumLis[key] = 0
    NumLis[key] += a
    prev = a
m = 0
for k, v in NumLis.items():
    if v > m:
        m = v
    key = k
if not is_connect:
    if A[-1] == M - 1:
        if A[0] == 0:
            tmp = NumLis[0] + NumLis[key]
            if m < tmp:
                m = tmp
print(All - m)
