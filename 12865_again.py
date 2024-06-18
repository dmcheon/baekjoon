def recur(idx, w):
    if w > K:
        return -999999999
    
    if idx == N:
        return 0
    
    if dp[idx][w] != -1:
        return dp[idx][w]
    
    #물건을 챙긴다/ 챙기지 않는다 중 큰 수
    dp[idx][w] = max(recur(idx + 1, w + stuffs[idx][0]) + stuffs[idx][1], recur(idx + 1, w))

    return dp[idx][w]



N, K = map(int, input().split())
stuffs = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(100001)] for _ in range(N)]

ans = recur(0, 0)
print(ans)