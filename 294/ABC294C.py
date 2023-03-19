N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
C = A + B
C.sort()
c_data = dict()
for idx in range(N + M):
    c_data[C[idx]] = idx + 1
a_result = [c_data[a] for a in A]
b_result = [c_data[b] for b in B]
print(*a_result)
print(*b_result)
