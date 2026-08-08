N = int(input())
l = 0
r = 0
result = 0
while l < N:
    if l >= r:
        r = l + 1
    while r < N:
        print(f"? {l + 1} {r + 1}")
        s = input()
        if s == "No":
            break
        r += 1
    if r > l:
        result += r - l - 1
    l += 1
print(f"! {result}")
