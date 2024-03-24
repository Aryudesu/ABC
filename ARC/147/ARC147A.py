N = int(input())
A = [int(l) for l in input().split()]

A.sort(reverse=True)
res = 0
i = 0
j = N - 1
while True:
    Ai = A[i]
    Aj = A[j]
    new_Ai = Ai % Aj
    if new_Ai:
        A.append(new_Ai)
        A[i] = 0
        N += 1
        i += 1
        j += 1
    else:
        A[i] = 0
        i += 1
    res += 1
    if i == j:
        break
print(res)
