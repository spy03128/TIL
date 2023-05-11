n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
min_row = []
for i in range(n):
    min_r = min(arr[i])
    min_row.append(min_r)

print(max(min_row))