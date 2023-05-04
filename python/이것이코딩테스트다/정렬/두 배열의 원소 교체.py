n, k = map(int, input().split())
Aarr = list(map(int,input().split()))
Barr = list(map(int,input().split()))

Aarr.sort()
Barr.sort(reverse=True)
for i in range(k):
    if Aarr[i] < Barr[i]:
        Aarr[i], Barr[i] = Barr[i], Aarr[i]
    else:
        break

print(sum(Aarr))