import sys
from collections import deque
input = sys.stdin.readline

def BFS():

    Q = deque()
    Q.append((0,0))
    visited[0][0] = 1
    while Q:
        cx,cy = Q.popleft()
        if cx == n-1 and cy == m-1:
            return
        for i in range(4):
            nx = cx +dx[i]
            ny = cy +dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and arr[nx][ny]==1:
                Q.append((nx,ny))
                visited[nx][ny] = visited[cx][cy]+1


n,m = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

BFS()
print(visited[n-1][m-1])

"""
5 6
101010
111111
000001
111111
111111
"""