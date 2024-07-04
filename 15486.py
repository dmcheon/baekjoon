import sys
input = sys.stdin.readline

N = int(input())
sch = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N + 1)]
for i in range(N):
    time = sch[i][0]
    val = sch[i][1]
    dp[i + 1] = max(dp[i + 1], dp[i])
    if i + time < N + 1:
        dp[i + time] = max(dp[i + time], dp[i] + val)
        
print(dp[-1])


