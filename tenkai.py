import sympy as sp

# 記号を定義
a1, a2, b1, b2, u = sp.symbols('a1 a2 b1 b2 u')

# 展開したい式
expr1 = (a1*b1) * (1-a2*b1*u) * (1-a1*b2*u) * (1-a2*b2*u)
expr2 = (a2*b1) * (1-a1*b1*u) * (1-a1*b2*u) * (1-a2*b2*u)
expr3 = (a1*b2) * (1-a1*b1*u) * (1-a2*b1*u) * (1-a2*b2*u)
expr4 = (a2*b2) * (1-a1*b1*u) * (1-a1*b2*u) * (1-a2*b1*u)

# 合計
total = (expr1 - expr2 - expr3 + expr4)

# 展開 & 整理
expanded_total = sp.expand(total)
collected_total = sp.collect(expanded_total, u)

print("展開した合計式:", expanded_total)
print("整理した合計式:", collected_total)