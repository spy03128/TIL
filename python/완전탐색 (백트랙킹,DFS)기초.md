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