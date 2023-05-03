import sys
from itertools import permutations
input = sys.stdin.readline

def DFS(i, now):
    global res_max, res_min, num
    if i == n:
        res_max = max(res_max, now)
        res_min = min(res_min, now)
        return
    else:
        if num[0]>0:
            num[0] -=1
            DFS(i+1, now + num_arr[i])
            num[0] +=1
        if num[1]>0:
            num[1] -= 1
            DFS(i + 1, now - num_arr[i])
            num[1] += 1
        if num[2]>0:
            num[2] -= 1
            DFS(i + 1, now * num_arr[i])
            num[2] += 1
        if num[3]>0:
            num[3] -= 1
            if now < 0:
                tmp = -now // num_arr[i]
                DFS(i+1, -tmp)
            else:
                DFS(i+1, now//num_arr[i])
            num[3] += 1


n = int(input())
num_arr = list(map(int,input().split()))
num = list(map(int,input().split()))

res_max, res_min = float('-Inf'), float('Inf')
DFS(1, num_arr[0])


print(res_max)
print(res_min)