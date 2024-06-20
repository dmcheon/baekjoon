N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for i in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]

q = []
q.append([0, 0])
visited[0][0] = 1
dp[0][0] = 1

while q:
    ey, ex = q.pop(0)
    if ey == N - 1 and ex == M - 1:
        break

    for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ny, nx = ey + dy, ex + dx
        if 0 <= ny < N and 0 <= nx < M:
            if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                q.append([ny, nx])
                visited[ny][nx] = 1
                dp[ny][nx] = dp[ey][ex] + 1
            
print(dp[N- 1][M - 1])                   
                