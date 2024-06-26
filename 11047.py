N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]


coins = [a for a in A if a <= K]
coins.sort(reverse=True)

ans = 0
val = K

for coin in coins:
    if val == 0:
        break
    ans += val // coin
    val = val % coin
    
print(ans)