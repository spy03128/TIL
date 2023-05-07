import sys, heapq
input = sys.stdin.readline

n = int(input())
Q = []
total = 0
for _ in range(n):
    heapq.heappush(Q, int(input()))
while len(Q)>1:
    a = heapq.heappop(Q)
    b = heapq.heappop(Q)
    tmp = a+b
    heapq.heappush(Q, tmp)
    total+=tmp
print(total)