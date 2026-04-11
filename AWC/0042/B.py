N, S, T = map(int, input().split())
D = list(map(int, input().split()))
D.sort()
skill = S
for d in D:
    if skill >= d:
        skill += d
print("Yes" if T <= skill else "No")
