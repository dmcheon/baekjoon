# 모든 경우의 수를 체크
# def recur(idx, P):
#     global pay
    
#     if idx == N:
#         if pay < P:
#             pay = P
#         return
#     if idx > N:
#         return
    
#     #오늘 상담을 한다면
#     recur(idx + sche[idx][0], sche[idx][1] + P)
    
#     #오늘 상담을 하지 않았을때 
#     recur(idx + 1, P)

# DP로 값을 저장해서 구하기.
import sys
sys.setrecursionlimit(99999999)

def recur(idx):
    if idx == N :
        return 0
    if idx > N :
        return -999999999
    if dp[idx] != -1:
        return dp[idx]

    #상담을 받거나 안받거나 그 중에서 더 돈을 많이 벌때 내 DP 테이블에 저장하겠다
    dp[idx] = max(recur(idx + sche[idx][0]) + sche[idx][1], recur(idx + 1))
    return dp[idx]

N = int(input())
sche = [list(map(int, input().split())) for _ in range(N)]
dp = [-1 for _ in range(N)]
ans = recur(0)
print(ans)