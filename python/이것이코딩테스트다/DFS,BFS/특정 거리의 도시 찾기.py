import sys
from collections import deque
input = sys.stdin.readline

def BFS(x):
    visited[x] = 0
    Q = deque()
    Q.append(x)
    while Q:
        cur = Q.popleft()
        for next in graph[cur]:
            if visited[next]==-1:
                Q.append(next)
                visited[next] = visited[cur]+1

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [-1]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

BFS(x)
if k not in visited:
    print(-1)
else:
    for i in range(n+1):
        if visited[i]==k:
            print(i)
