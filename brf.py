from collections import Counter

# HIT&BLOW
def hb(g, a):
    hit = 0
    blow = 0
    for i in range(4):
        if g[i] == a[i]:
            hit += 1
    for i in range(4):
        for j in range(4):
            if g[j] == a[i] and g[i] != a[i] and g[j] != a[j]:
                blow += 1
    return hit,blow

# define representative patterns with letters; map letters to digits 0,1,2...
patterns = {
"ABCD":"0123",
"AABC":"0012",
"ABAC":"0102",
"ABCA":"0120",
"BAAC":"1002",
"BACA":"1020",
"BCAA":"1200",
"AAAB":"0001",
"AABA":"0010",
"ABAA":"0100",
"BAAA":"1000",
"AAAA":"0000"
}

def count_for_guess(g):
    cnt=0
    for x in range(10000):
        a=f"{x:04d}"
        h,b=hb(g,a)
        if h==1 and b==1:
            cnt+=1
    return cnt

results={}
for name,g in patterns.items():
    results[name]=count_for_guess(g)

print(results)
