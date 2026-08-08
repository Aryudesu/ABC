N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
D = [b-a for a, b in zip(A, B)]
D.sort(reverse=True)
print(sum(A) + sum(D[:K]))
