A, B = map(int, input().split())
data = set()
data.add(A + B)
data.add(A - B)
data.add(A * B)
if A%B == 0:
    data.add(A//B)
print("Nine" if 9 in data else "Nein")
