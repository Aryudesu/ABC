def calc(H, W, A):
    return False

def inputField():
    H, W = [int(l) for l in input().split()]
    A = []
    for h in range(H):
        A.append(input())
    return H, W, A

H, W, A = inputField()
print("Yes" if calc(H, W, A) else "No")

