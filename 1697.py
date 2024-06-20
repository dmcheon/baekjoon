N, K = map(int, input().split())
dp = [0]*100001

q = []
q.append(N)

while q:
    node = q.pop(0)
    if node == K:
            break
    
    for dist in [1, -1, node]:
        nxt_node = node + dist
        if 0 <= nxt_node < 100001 and dp[nxt_node] == 0:
            dp[nxt_node] = dp[node] + 1
            q.append(nxt_node)
            
print(dp[K])
        
        

