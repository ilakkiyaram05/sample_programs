def min_operations(s: str, t: str) -> int:
    m, n = len(s), len(t)
    
    # Initialize the DP table with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the base cases
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters from s to match empty t
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters into empty s to match t
        
    # Fill the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],    # Insert
                    dp[i - 1][j],    # Remove
                    dp[i - 1][j - 1] # Replace
                )
                
    return dp[m][n]

# Driver code to test the examples
print(min_operations("geek", "gesek"))  # Output: 1
print(min_operations("gfg", "gfg"))      # Output: 0
