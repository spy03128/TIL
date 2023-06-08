import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()
s, e = 0, house[n-1]-house[0]
answer = 0

while s <= e:
    mid = (s + e) // 2
    spot, cnt = 0, 1
    for x in range(1, n):
        if house[x] - house[spot] >= mid:
            cnt += 1
            spot = x
    if cnt >= c:
        answer = mid
        s = mid + 1
    else:
        e = mid - 1

print(answer)
