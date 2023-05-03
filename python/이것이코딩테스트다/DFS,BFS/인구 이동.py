import sys
from collections import deque
input = sys.stdin.readline

def BFS(i, j):
    global arr
    Q = deque()
    Q.append((i,j))
    visited[i][j]=1
    cnt, total = 1,arr[i][j]
    vis = []
    vis.append((i,j))
    while Q:
        x,y = Q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and L<=abs(arr[nx][ny]-arr[x][y])<=R:
                Q.append((nx,ny))
                visited[nx][ny]=1
                cnt+=1
                total+=arr[nx][ny]
                vis.append((nx,ny))
    tmp = int(total/cnt)
    for x,y in vis:
        arr[x][y] = tmp


N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
res = 0
while True:
    check = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                BFS(i,j)
                check+=1
    if check==N*N:
        break
    res +=1
print(res)