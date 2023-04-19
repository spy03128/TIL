import sys
from collections import deque
input = sys.stdin.readline

def BFS(x,y):
    Q = deque()
    Q.append((x,y))
    visited[x][y]=1
    while Q:
        cx,cy = Q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0 and visited[nx][ny]==0:
                visited[nx][ny]=1
                Q.append((nx,ny))

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
visited = [[0]*m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and visited[i][j]==0:
            BFS(i,j)
            cnt+=1

print(cnt)

"""
4 5
0 0 1 1 0
0 0 0 1 1
1 1 1 1 1
0 0 0 0 0
"""