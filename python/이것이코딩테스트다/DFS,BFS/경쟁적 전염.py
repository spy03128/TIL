import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    Q = deque()
    for q in Qarr:
        Q.append(q)
    while Q:
        cur_num, cur_x, cur_y = Q.popleft()
        if visited[cur_x][cur_y] == s:
            break
        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny]==0 and visited[nx][ny] ==-1:
                Q.append((cur_num,nx,ny))
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                arr[nx][ny] = cur_num

n,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
s,x,y, = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
Qarr = []
visited = [[-1]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
         if arr[i][j] != 0:
             Qarr.append((arr[i][j], i, j))
             visited[i][j]=0

Qarr.sort()

BFS()

print(arr[x-1][y-1])
