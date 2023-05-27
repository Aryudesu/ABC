N = int(input())
A = [int(l) for l in input().split()]
B = [a for a in A]
B.sort()
graph = dict()
data = []
for n in range(N):
    if A[n] != B[n]:
        graph.get(A[n], [])
