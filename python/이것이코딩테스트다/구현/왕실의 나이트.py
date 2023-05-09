xy = input()
x, y = ord(xy[0])-97, int(xy[1])-1
cnt = 0

# 내가 푼 방법
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for d1 in range(4):
    cx = x + dx[d1]*2
    cy = y + dy[d1]*2
    if 0<=cx<8 and 0<=cy<9:
        s,e = 0, 0
        if d1==0 or d1==1:
            s,e = 2, 4
        else:
            s,e = 0, 2
        for d2 in range(s,e):
            nx = cx + dx[d2]
            ny = cy + dy[d2]
            if 0<=nx<8 and 0<=ny<8:
                cnt+=1


# 한번에 이동할 수 있는 방향을 모두 정의해서 푸는 방법
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if 0<=nx<8 and 0<=ny<8:
        cnt+=1
        



print(cnt)

