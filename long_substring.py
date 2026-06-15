def longestUniqueSubstr(S: str) -> int:
    last_seen = {}
    max_len = 0
    start = 0
    for end, char in enumerate(S):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = end
        max_len = max(max_len, end - start + 1)
    return max_len
def main():
    s1 = "geeksforgeeks"
    print(f"Input:  S = '{s1}'")
    print(f"Output: {longestUniqueSubstr(s1)}")
    print("-" * 30)
if __name__ == "__main__":
    main()
