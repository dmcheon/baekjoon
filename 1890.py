N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)]for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
        
        jump = game[i][j]
        
        if j + jump < N:
            dp[i][j + jump] += dp[i][j]
           
        if i + jump < N:
            dp[i + jump][j] += dp[i][j]
          
                
print(dp[N-1][N-1])