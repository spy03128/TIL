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
