N = int(input())
student = []
for _ in range(N):
    name, kor, eng, math = input().split()
    student.append((-int(kor), int(eng), -int(math), name))
student.sort()
for st in student:
    print(st[3])