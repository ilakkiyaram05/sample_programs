import math

n, a, b, c, d = map(int, input().split())
total_sum = 0
for i in range(1, n + 1):
    x = (a * i) + b
    y = (c * i) + d
    total_sum += math.gcd(x, y)

print(total_sum % 998244353)
