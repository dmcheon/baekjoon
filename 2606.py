N = int(input())
link_N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0 for i in range(N + 1)]

for i in range(link_N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# DFS
# def recur(node):
#     visited[node] = 1
#     for nxt in graph[node]:
#         if visited[nxt] == 1:
#             continue
#         recur(nxt)

# BFS
q = []
q.append(1)

while len(q):
    node = q.pop(0)
    visited[node] = 1
    
    for nxt in graph[node]:
        if visited[node] == 1:
            continue
        q.append(nxt) 


# recur(1)
print(sum(visited) - 1)