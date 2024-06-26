n = int(input())
L = list(map(int, input().split()))

max_L = max(L)
modif_L = [l + max_L for l in L] 

ans = sum(modif_L) - max_L*2
print(ans)

