def calc()->bool:
    G, M, D, K, V = map(int, input().split())
    TD = M - G
    if D * K < G:
        return (K + G - D * K) * V <= TD
    else:
        return TD * D >= G*V 

print("Yes" if calc() else "No")
