T = int(input())
for t in range(T):
    X, Y, K = map(int, input().split())
    graph = [[0 for _ in range(X)] for _ in range(Y)]
    visited = [[0 for _ in range(X)] for _ in range(Y)]
    count = 0
    
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for y in range(Y):
        for x in range(X):
            if graph[y][x] == 1 and visited[y][x] == 0: #BFS로 탐색.
                count += 1
                q = []
                q.append([y, x])
                
                while q:
                    ey, ex = q.pop(0)
                
                    for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                        ny, nx = ey + dy, ex + dx
                        
                        if 0 <= ny < Y and 0 <= nx < X:
                            if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                                visited[ny][nx] = 1 
                                q.append([ny, nx])
        
    print(count)