### 재귀함수를 이용한 이진수 출력

```python
def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end="")

n = int(input())
DFS(n)
```

### 이진트리순회

DFS: `재귀 , 트리 이용`

부모 노드의 위치에 따라

- 전위순회 : 부모 왼쪽노드 오른쪽노드 `대부분 DFS 문제`
- 중위순회 : 왼쪽노드 부모 오른쪽노드
- 후위순회 : 왼쪽노드 오른쪽노드 부모노드 `병합정렬`

```python
def DFS(v):
    if v>7:
        return
    else:
        print(v,end=" ")
        DFS(v*2)
        DFS(v*2+1)

DFS(1)
```

### 부분집합 구하기

```python
def DFS(v):
    if v == n+1:
        for i in range(n+1):
            if ch[i]==1:
                print(i,end=" ")
        print()
        return
    ch[v]=1
    DFS(v+1)
    ch[v]=0
    DFS(v+1)

n=int(input())
ch = [0]*(n+1)
DFS(1))
```

### 합이 같은 부분집합

```python
def DFS(idx=0, a=[], b=[]):
    global check
    if check:
        return
    if idx == n:
        if sum(a)==sum(b):
            check=True
        return
    a.append(arr[idx])
    DFS(idx+1,a,b)
    a.pop()
    b.append(arr[idx])
    DFS(idx+1,a,b)
    b.pop()

n=int(input())
arr=list(map(int,input().split()))
check=False
DFS()
if check:
    print("YES")
else:
    print("NO")
```

```python
import sys

def DFS(L, sum):
    if sum>total//2:
        return 
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1,sum+arr[L])
        DFS(L+1,sum)

n=int(input())
arr=list(map(int,input().split()))
total=sum(arr)
DFS(0,0)
print("NO")
```

### 바둑이 승차

```python
import sys
input = sys.stdin.readline

def DFS(v):
    global maxim
    if v==n:
        wt = 0
        for i in range(n):
            if check[i]==1:
                wt+=arr[i]
                if wt>c:
                    return
        maxim = max(maxim, wt)
        return 
    check[v] = 1
    DFS(v+1)
    check[v] = 0
    DFS(v+1)

c , n = map(int, input().split())
arr = [int(input()) for _ in range(n)]
check = [0]*n
maxim = 0
DFS(0)
print(maxim)
```

```python
def DFS(L, sum,tsum):
    global result
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L],tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

c,n = map(int,input().split())
a = [0]*n
result = -2147000000
for i in range(n):
    a[i] = int(input())
total = sum(a)
DFS(0,0,0)
print(result)
```

### 인접행렬(가중치 방향그래프)

```python
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for i in range(1,n+1):
    for j in range(1, n+1):
        print(graph[i][j], end=" ")
    print()
```

### 경로 탐색(그래프 DFS)

```python
import sys
input = sys.stdin.readline

def DFS(L):
    global cnt
    if L==n:
        cnt+=1
    for i in range(1, n + 1):
        if check[i]==0 and graph[L][i]==1:
            check[L]=1
            DFS(L+1)
            check[L] = 0

n,m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
check = [0]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
cnt=0
check[1] = 1
DFS(1)
print(cnt)
```