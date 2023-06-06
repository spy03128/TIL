import sys
input = sys.stdin.readline

def binary_search(x, start, end):
	while start <= end:
		mid = (start + end) // 2
		if product[mid] == x:
			return True
		elif product[mid] < x:
			start = mid + 1
		else:
			end = mid - 1
	return False

n = int(input())
product = sorted(list(map(int, input().split())))
m = int(input())
customer = list(map(int, input().split()))
answer = []
for x in customer:
	if binary_search(x, 0, n-1):
		answer.append("yes")
	else:
		answer.append("no")

print(*answer)

# ==================
# 집합 이용하기

import sys
input = sys.stdin.readline

n = int(input())
product = set(map(int, input().split()))

m = int(input())
customer = list(map(int, input().split()))

for x in customer:
    if x in product:
        print("yes", end = " ")
    else:
        print("no", end = " ")