
N, M, K = map(int, input().split())

team = 0
leftover = 0
while(1):
    if N >= 2 and M >= 1:
        team += 1
        N -= 2
        M -= 1
        
    else:
        leftover += N + M
        break
        
if leftover >= K:
    print(team)
    
else:
    interns = K - leftover
    team = team - interns//3
    if interns % 3 > 0:
        team -= 1
    
    print(team)
    