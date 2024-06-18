import sys
input = sys.stdin.readline
# input을 readline으로 안받으니 시간초과 당함
# 입력이 많이 들어오는 문제는 input 대신 sys.stdin.readline을 써야 합니다.
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)    
    
visited = [0 for i in range(N + 1)]
count = 0

for i in range(1, N + 1):
    if visited[i] == 0:
        count += 1
        visited[i] = 1
        
        q = []
        q.append(i)
        
        while q:
            node = q.pop(0)
            for n in graph[node]:
                if visited[n] == 0:
                    visited[n] = 1
                    q.append(n) 

print(count)