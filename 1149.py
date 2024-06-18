N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for i in range(3)]for _ in range(N)]
dp[0] = graph[0]

for i in range(1, N):
    for RGB in range(3):
        if RGB == 0:
            #RED
            dp[i][RGB] = min(dp[i - 1][1], dp[i - 1][2]) + graph[i][RGB]
        if RGB == 1:
            #GREEN
            dp[i][RGB] = min(dp[i - 1][0], dp[i - 1][2]) + graph[i][RGB]
        if RGB == 2:
            #BLUE
            dp[i][RGB] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][RGB]
            
print(min(dp[-1]))