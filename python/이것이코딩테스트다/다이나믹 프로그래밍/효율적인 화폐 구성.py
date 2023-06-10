import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [10001] * (m + 1)
dp[0] = 0

for _ in range(n):
    x = int(input())
    for y in range(x, m + 1):
        dp[y] = min(dp[y], dp[y - x] + 1)

print(dp[m] if dp[m]!=10001 else -1)