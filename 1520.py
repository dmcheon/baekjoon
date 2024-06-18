def recur(y, x):
    # 오른쪽 하단 끝에 도달하면 종료
    if y == Y - 1 and x == X - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    
    route = 0
    for dy, dx in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < Y and 0 <= nx < X:
            if graph[y][x] > graph[ny][nx]:
                route += recur(ny, nx)
            
    dp[y][x] = route
    return dp[y][x]


Y, X = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(Y)]
dp = [[-1 for _ in range(X)] for _ in range(Y)]

ans = recur(0, 0)
print(dp[0][0])