N = int(input())
graph = [list(map(int, input().rstrip())) for i in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
N_town = 0
N_houses = []
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1 and visited[y][x] == 0:
            N_town += 1

            q = []
            q.append([y, x])
            visited[y][x] = 1
            
            cnt = 1
            while q:
                ey, ex = q.pop(0)
                
                for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    ny, nx = ey + dy, ex + dx
                    if 0 <= ny < N and 0 <= nx < N:
                        if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                            visited[ny][nx] = 1
                            q.append([ny, nx])
                            cnt += 1
                            
            N_houses.append(cnt)
            
            
print(N_town)
N_houses.sort()
for h in N_houses:
    print(h)                   
            
