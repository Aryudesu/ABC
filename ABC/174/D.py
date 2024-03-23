N = int(input())
C = input()
WC = 0
RC = 0
WTC = 0
RTC = 0
for c in C:
    if c == "R":
        RC += 1
    else:
        WC += 1
for i in range(N):
    if i + 1 <= RC and C[i] == "R":
        RTC += 1
    else:
        WTC += 1
print(abs(RC - RTC))
