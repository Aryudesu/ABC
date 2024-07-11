N, X = [int(l) for l in input().split()]
A = [int(l) - 1 for l in input().split()]
node = X - 1
memo = set()
while not node in memo:
    memo.add(node)
    node = A[node]
print(len(memo))
