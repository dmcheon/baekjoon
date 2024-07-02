N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]

dp[0][S] = 1

for i in range(1, N + 1):
    for j in range(M + 1):
        if dp[i - 1][j] == 1:
            plus_vol = j + V[i - 1]
            minus_vol = j - V[i - 1]
            if 0 <= plus_vol <= M:
                dp[i][plus_vol] = 1
            if 0 <= minus_vol <= M:
                dp[i][minus_vol] = 1
                
ans = -1

for i in range(M, -1, -1):
    if dp[N][i] == 1:
        ans = i
        break
            
print(ans)