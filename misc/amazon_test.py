matrix = [[1,0,0],
          [1,0,0],
          [1,9,1]]
# matrix = [[1,0,0],
#           [1,0,0],
#           [1,1,9]]
m = len(matrix)
n = len(matrix[0])
visited = []
for i in range(m):
    vis = []
    for j in range(n):
        vis.append(False)
    visited.append(vis)
visited[0][0] = True
dx = [1,-1,0,0]
dy = [0,0,1,-1]

r,c,d=0,0,0 # start, source

Q = [(r,c,d)]

while Q:
    r_,c_,d_ = Q.pop(0)
    d1 = d_ + 1
    for i in range(4):
        r1 = r_ + dy[i]
        c1 = c_ + dx[i]
        if r1 >= 0 and r1 < m and c1 >= 0 and c1 < n:
            if matrix[r1][c1] == 0:
                continue
            elif matrix[r1][c1] == 1 and not visited[r1][c1]:
                Q.append((r1, c1, d1))
                visited[r1][c1] = True
            elif matrix[r1][c1] == 9:
                print("Reached in",d1)
                import sys
                sys.exit(0)
            else:
                continue
        else:
            continue
