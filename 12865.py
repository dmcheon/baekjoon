# 백트래킹으로 모든 경우의 수 찾아 업뎃.
# def recur(idx, W, V):
#     global max_V
#     #종료조건: 물건들을 다 탐색했다.
#     if W > K:
#         return
#     if idx == N:
#         if max_V < V:
#             max_V = V
#         return
#     #물건을 챙긴다
#     recur(idx + 1, stuffs[idx][0] + W, stuffs[idx][1] + V)
#     #물건을 챙기지 않는다
#     recur(idx + 1, W, V)
 
 # 메모이제이션 DP   
def recur(idx, W):
    if W > K:
        return -99999999
    if idx == N:
        return 0
    if dp[idx][W] != -1:
        return dp[idx][W]
    
    # 물건을 챙기든 안 챙기는 최댓값을 dp에 넣어서 저장
    dp[idx][W] = max(recur(idx + 1, stuffs[idx][0] + W) + stuffs[idx][1], recur(idx + 1, W))
    return dp[idx][W]
    


N, K = map(int, input().split())
stuffs = [list(map(int, input().split())) for _ in range(N)]
# max_V = 0

#배낭의 가치를 저장
dp = [[-1 for _ in range(100001)] for i in range(N)]
answer = recur(0, 0)
print(answer)
