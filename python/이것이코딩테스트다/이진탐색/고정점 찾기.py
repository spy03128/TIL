import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
s, e = 0, n-1

while s <= e:
    mid = (s + e) // 2
    if mid == array[mid]:
        print(mid)
        exit()
    elif mid < array[mid]:
        e = mid - 1
    else:
        s = mid + 1

print(-1)