import sys
input = sys.stdin.readline

N = int(input())
sg = sorted(list(map(int, input().split())))
M = int(input())
cards = list(map(int, input().split()))

result = []

for i in range(M):
    s = 0
    e = N - 1
    r = 0
    
    while s <= e:
        mid = (s + e)//2
        
        if sg[mid] == cards[i]:
            r = 1
            break
        if sg[mid] < cards[i]:
            s = mid + 1
            
        else:
            e = mid - 1
    
    
    result.append(r)     

print(*result)
