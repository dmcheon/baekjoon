import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def recur(y, x):
    if dp[y][x] != 0:
        return dp[y][x]
    
    # 네 방향 탐색
    for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N:
            if graph[y][x] < graph[ny][nx]:
                dp[y][x] = max(recur(ny, nx) + 1, dp[y][x])
                
    
    return dp[y][x]
    

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

#입력받은 그래프 순서대로 순회
for y in range(N):
    for x in range(N):
        recur(y, x)

print(max(map(max, dp)) + 1)