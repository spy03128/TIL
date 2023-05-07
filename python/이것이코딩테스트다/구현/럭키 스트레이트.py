s = input()
point = (len(s)-1)//2 + 1
a = s[:point]
b = s[point:]
sum_a , sum_b = 0, 0
for x in a:
    sum_a += int(x)
for x in b:
    sum_b += int(x)
if sum_a==sum_b:
    print("LUCKY")
else:
    print("READY")