import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
start, end = 0, max(array)
answer = 0
while start <= end:
	mid = (start + end) // 2
	total = 0
	for a in array:
		total += max(a - mid, 0)
	if total < m:
		end = mid - 1
	else:
		answer = mid
		start = mid + 1

print(answer)