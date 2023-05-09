st = input()
eng = []
num = []
for s in st:
    if s in "0123456789":
        num.append(int(s))
    else:
        eng.append(s)
eng.sort()
print("".join(eng)+str(sum(num)))