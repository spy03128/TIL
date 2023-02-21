### 송아지 찾기

```python
from collections import deque

s,e=map(int,input().split())
MAX = 10000
ch = [0]*(MAX+1)
d = [0]*(MAX+1)
ch[s] = 1
d[s] = 0
dq = deque()
dq.append(s)
while dq:
    now = dq.popleft()
    if now==e:
        break
    for next in(now-1, now+1, now+5):
        if 0<next<=MAX and ch[next]==0:
            ch[next]=1
            dq.append(next)
            d[next] = d[now]+1

print(d[e])
```

### 사과나무

```python
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
check = [[0]*n for _ in range(n)]
sum = 0
Q = deque()
Q.append((n//2,n//2))
sum+=arr[n//2][n//2]
check[n//2][n//2] = 1
L=0
while True:
    if L==n//2:
        break
    size = len(Q)
    for i in range(size):
        now = Q.popleft()
        for j in range(4):
            x = now[0] + dx[j]
            y = now[1] + dy[j]
            if check[x][y]==0:
                check[x][y] =1
                sum+=arr[x][y]
                Q.append((x,y))
    L+=1
print(sum)
```

### 미로의 최단거리 통로

```python
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

arr = [list(map(int,input().split())) for _ in range(7)]
check = [[0]*7 for _ in range(7)]
Q = deque()
Q.append((0,0))
check[0][0] = 1

while Q:
    now = Q.popleft()
    for i in range(4):
        x = now[0] + dx[i]
        y = now[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and check[x][y]==0 and arr[x][y]==0:
            Q.append((x,y))
            check[x][y]=check[now[0]][now[1]]+1
if check[6][6]==0:
    print(-1)
else:
    print(check[6][6]-1)
```

```python
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int,input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]
Q = deque()
Q.append((0,0))
board[0][0]=1
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            board[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x,y))
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])
```

### 섬나라 아일랜드

```python
from collections import deque

def BFS(i,j):
    while Q:
        now = Q.popleft()
        for i in range(8):
            x = now[0]+dx[i]
            y = now[1]+dy[i]
            if 0<=x<n and 0<=y<n and check[x][y]==0 and arr[x][y]==1:
                Q.append((x,y))
                check[x][y]=1

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1,0]
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
check = [[0]*n for _ in range(n)]
Q = deque()
cnt=0
for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and check[i][j]==0:
            Q.append((i,j))
            check[i][j]==1
            BFS(i,j)
            cnt+=1

print(cnt)
```

### 토마토

```python
from collections import deque

def BFS():
    while Q:
        now = Q.popleft()
        for i in range(4):
            x = now[0]+dx[i]
            y = now[1]+dy[i]
            if 0<=x<n and 0<=y<m and arr[x][y]==0:
                check[x][y]=check[now[0]][now[1]]+1
                arr[x][y]=1
                Q.append((x,y))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]
Q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            Q.append((i,j))
BFS()
ch = False
for i in range(n):
    if ch:
        break
    for j in range(m):
        if arr[i][j]==0:
          ch = True
          break

if ch:
    print(-1)
else:
    print(max([max(x) for x in check]))
```

---

### 최대점수 구하기

```python
def DFS(L, t, s):
    global result
    if t > m:
        return
    if L==n:
        result=max(result,s)
    else:
        DFS(L+1, t+time[L], s+score[L])
        DFS(L+1, t,s)

n,m = map(int,input().split())
score = list()
time= list()

for _ in range(n):
    x,y = map(int,input().split())
    score.append(x)
    time.append(y)
result = 0
DFS(0,0,0)
print(result)
```

### 휴가 (삼성 SW역량평가 기출문제)

```python
def DFS(L,sum):
    global result
    if L==n+1:
        result = max(result, sum)
    else:
        if L+time[L] <= n+1:
            DFS(L + time[L], sum + point[L])
        DFS(L + 1, sum)

n = int(input())
time = list()
point = list()
result = -100
for _ in range(n):
    x,y = map(int,input().split())
    time.append(x)
    point.append(y)
time.insert(0,0)
point.insert(0,0)

DFS(1, 0)
print(result)
```

### 양팔저울

`set` : 중복을 제거하면서 값을 추가할 수 있음

```python
def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)

n=int(input())
G = list(map(int,input().split()))
s=sum(G)
res = set()
DFS(0,0)
print(s-len(res))
```

### 동전 바꿔주기

```python
def DFS(L, sum):
    global res
    if sum>t:
        return
    if L==k:
        if sum==t:
            res+=1

    else:
        for i in range(n[L]+1):
            DFS(L+1, sum+money[L]*i)

t = int(input())
k = int(input())
money = []
n = []
for i in range(k):
    x,y = map(int,input().split())
    money.append(x)
    n.append(y)
res = 0
DFS(0,0)

print(res)
```

### 동전 분배하기

```python
def DFS(L):
    global res
    if L == n:
        ch = max(person) - min(person)
        if ch<res:
            tmp = set()
            for x in person:
                tmp.add(x)
            if len(tmp)==3:
                res = min(res,ch)

        return
    for i in range(3):
        person[i] += money[L]
        DFS(L+1)
        person[i] -= money[L]

n = int(input())
money = []
for i in range(n):
    money.append(int(input()))
person = [0]*3
res = float('inf')
DFS(0)
print(res)
```

### 알파코드

```python
def DFS(L, P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(res[j], end=" ")
        print()
    else:
        for i in range(1,27):
            if code[L]==i:
                res[P]=i
                DFS(L+1, P+1)
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                res[P]=i
                DFS(L+2, P+1)

code = list(map(int,input()))
n=len(code)
res=[0]*(n+3)
cnt=0
DFS(0,0)
print(cnt)
```
