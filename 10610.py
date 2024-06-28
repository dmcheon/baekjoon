N = list(map(int, input().rstrip()))

if 0 not in N or sum(N) % 3 != 0:
    print(-1)
    
else:
    N.sort(reverse=True)
    ans = ""
    for n in N:
        ans += str(n)
        
    print(ans)