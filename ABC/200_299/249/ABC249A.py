A, B, C, D, E, F, X = [int(l) for l in input().split()]

Taka_time, Taka_nokori = divmod(X, A + C)
Taka = (A * Taka_time * B) + B * (Taka_nokori if Taka_nokori < A else A)

Aoki_time, Aoki_nokori = divmod(X, D + F)
Aoki = (D * Aoki_time * E) + E * (Aoki_nokori if Aoki_nokori < D else D)

if Taka > Aoki:
    print("Takahashi")
elif Taka < Aoki:
    print("Aoki")
else:
    print("Draw")
