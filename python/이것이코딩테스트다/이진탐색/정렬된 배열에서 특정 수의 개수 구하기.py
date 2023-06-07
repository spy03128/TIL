import sys
input = sys.stdin.readline

def search_first(s, e, x):
	while s <= e:
		mid = (s + e) // 2
		if array[mid] == x:
			if mid == 0:
				return 0
			if array[mid - 1] == array[mid]:
				e = mid - 1
			else:
				return mid
		elif array[mid] < x:
			s = mid + 1
		else:
			e = mid - 1
	return -1

def search_finish(s, e, x):
	while s <= e:
		mid = (s + e) // 2
		if array[mid] == x:
			if mid == e:
				return e
			if array[mid + 1] == array[mid]:
				s = mid + 1
			else:
				return mid
		elif array[mid] < x:
			s = mid + 1
		else:
			e = mid - 1
	return -1

n, x = map(int, input().split())
array = list(map(int, input().split()))
first = search_first(0, n - 1, x)
finish = search_finish(0, n - 1, x)
if first == -1 and finish == -1:
	print(-1)
else:
	print(finish - first + 1)