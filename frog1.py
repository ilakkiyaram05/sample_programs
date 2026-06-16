n = int(input())
# This reads the entire line of heights and converts them into a list of integers
h = list(map(int, input().split()))

dp = [0] * n

# Base cases
dp[0] = 0
if n > 1:
    dp[1] = abs(h[1] - h[0])

for i in range(2, n):
    c1 = abs(h[i-1] - h[i])
    c2 = abs(h[i-2] - h[i])
    dp[i] = min(dp[i-1] + c1, dp[i-2] + c2)

print(dp[n-1])
