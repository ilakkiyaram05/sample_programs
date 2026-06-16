import sys

def solve():
    # Read N
    n = int(sys.stdin.readline())
    # Read heights
    h = list(map(int, sys.stdin.readline().split()))
   
    # dp[i] will store the minimum cost to reach stone i
    dp = [0] * n
   
    # Base Case: Stone 1 (index 0) is 0
    dp[0] = 0
   
    # Base Case: Stone 2 (index 1)
    if n > 1:
        dp[1] = abs(h[1] - h[0])
       
    # Fill the table for the rest of the stones
    for i in range(2, n):
        # Option 1: Jump from the previous stone
        opt1 = dp[i-1] + abs(h[i] - h[i-1])
        # Option 2: Jump from two stones back
        opt2 = dp[i-2] + abs(h[i] - h[i-2])
       
        # Take the minimum of the two
        dp[i] = min(opt1, opt2)
       
    # The answer is the cost to reach the last stone
    print(dp[n-1])

solve()
