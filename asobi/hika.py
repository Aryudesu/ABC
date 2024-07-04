N = 302875106592253
for n in range(1, 100):
    tmp = n ** n
    if tmp == N:
        print(n)
        break
    elif tmp > N:
        break

