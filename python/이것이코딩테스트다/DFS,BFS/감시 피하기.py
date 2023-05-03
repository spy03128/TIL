import sys
input = sys.stdin.readline

def check(x,y):
    for d in range(4):
        cx,cy = x,y
        while True:
            cx += dx[d]
            cy += dy[d]
            if not (0<=cx<n and 0<=cy<n):
                break
            if arr[cx][cy] == 'O':
                break
            if arr[cx][cy] == 'S':
                return True

    return False

def DFS(count):

    if count == 3:
        for i,j in teacher:
            if check(i,j):
                break
        else:
            print("YES")
            exit()
    else:
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'X':
                    arr[i][j] = 'O'
                    DFS(count + 1)
                    arr[i][j] = 'X'



n = int(input())
arr = [input().split() for _ in range(n)]
teacher = []
for i in range(n):
    for j in range(n):
        if arr[i][j]=='T':
            teacher.append((i,j))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
DFS(0)
print("NO")