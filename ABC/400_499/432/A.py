ABC = list(map(int, input().split()))
ABC.sort(reverse=True)
A, B, C = ABC
print(A*100 + B*10 + C)
