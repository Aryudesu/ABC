import heapq

N, K = [int(l) for l in input().split()]
A = [-int(l) for l in input().split()]
heapq.heapify(A)
result = 0
for k in range(K):
    dat = -heapq.heappop(A)
    if dat > 0:
        result += dat
        dat -= 1
        heapq.heappush(A, -dat)
    else:
        break
print(result)
