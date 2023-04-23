import sys, copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def calc_row(num):
    return num//m

def calc_col(num):
    return num%m

def BFS(narr):
    global cnt
    tmp = 0
    Q = deque()
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if narr[i][j]==2:
                Q.append((i,j))
    while Q:
        x,y = Q.popleft()
        visited[x][y] = 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m and narr[nx][ny]==0 and visited[nx][ny]==0:
                Q.append((nx,ny))
                visited[nx][ny]=1
                narr[nx][ny]=2
    for i in range(n):
        for j in range(m):
            if narr[i][j]==0:
                tmp+=1
    cnt = max(cnt,tmp)

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
for combi in combinations(range(n*m),3):
    narr = copy.deepcopy(arr)
    flag = False
    for i in combi:
        x = calc_row(i)
        y = calc_col(i)

        if narr[x][y] != 0:
            flag = True
            break
        narr[x][y] = 1
    if flag:
        continue

    BFS(narr)



print(cnt)