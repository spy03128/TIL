# 단순하게 푸는 방법
n, m ,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
total = 0
cnt = 0
for _ in range(m):
    if cnt == k:
        cnt = 0
        total+=arr[1]
    else:
        total+=arr[0]
        cnt+=1
print(total)

#수학적 연산을 사용해 푸는 방법
first = arr[0]
second = arr[1]
count = int(m/(k+1)) * k
count+=m%(k+1)
res = 0
res += (count) * first
res += (m - count) * second
print(res)