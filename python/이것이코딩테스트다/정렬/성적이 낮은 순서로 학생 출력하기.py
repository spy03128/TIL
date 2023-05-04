n = int(input())
arr = []
for i in range(n):
    name, score = input().split()
    arr.append((name, int(score)))
arr.sort(key=lambda x:x[1])
for name,score in arr:
    print(name,end=" ")