def calc(A):
    count = 0
    for i in range(5):
        if A[i] == i:
            count += 1
        elif i < 5 and A[i] == i + 1 and A[i + 1] == i:
            count += 1
    return count == 4


A = [int(l)-1 for l in input().split()]
print("Yes" if calc(A) else "No")
