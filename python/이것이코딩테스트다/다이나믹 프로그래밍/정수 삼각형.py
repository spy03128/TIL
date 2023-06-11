import sys
input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = array[0][0]

for x in range(1, n):
    for y in range(x + 1):
        if y == 0:
            dp[x][y] = dp[x - 1][y] + array[x][y]
        elif y == x:
            dp[x][y] = dp[x - 1][y - 1] + array[x][y]
        else:
            dp[x][y] = max(dp[x - 1][y - 1] + array[x][y], dp[x - 1][y] + array[x][y])

print(max(dp[n-1]))