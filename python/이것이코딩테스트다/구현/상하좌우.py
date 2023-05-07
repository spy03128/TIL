n = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
x, y = 1,1
direction_dict = {"U": 0, "R": 1, "D": 2, "L": 3}
move = input().split()
for m in move:
    d = direction_dict[m]
    nx = x + dx[d]
    ny = y + dy[d]
    
    if 0 < nx <= n and 0 < ny <= n:
        x, y = nx, ny

print(x,y)