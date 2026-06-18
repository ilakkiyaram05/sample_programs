import sys

def main():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # Map the remaining inputs into float values for probabilities
    p = [float(x) for x in input_data[1:]]
    
    # dp[j] stores the probability of getting exactly j heads
    dp = [0.0] * (n + 1)
    dp[0] = 1.0  # Base case: 0 heads with 0 coins has 100% probability
    
    # DP State transitions
    for i in range(n):
        coin_p = p[i]
        # Iterate backwards from i+1 down to 0 to update in-place safely
        for j in range(i + 1, -1, -1):
            head_prob = dp[j - 1] * coin_p if j > 0 else 0.0
            tail_prob = dp[j] * (1.0 - coin_p)
            dp[j] = head_prob + tail_prob
            
    # Calculate the minimum number of heads required to exceed tails
    minimum_heads_needed = (n // 2) + 1
    
    # Sum up all matching conditions
    total_probability = sum(dp[minimum_heads_needed:])
    
    # Print output matching the 10^-9 precision constraint
    print(f"{total_probability:.10f}")

if __name__ == '__main__':
    main()
