N, X = map(int, input().split())
essenses = sorted(list(map(int, input().split())))

s = 0
e = N - 1

bottle = 0
remain = 0
while s <= e:
    if essenses[e] >= X:
        bottle += 1
        e -= 1
        continue
    
    if s == e:
        remain += 1
        break
        
    if essenses[s] + essenses[e] >= X/2:
        bottle += 1
        s += 1
        e -= 1
    else:
        s += 1
        remain += 1

        
print(bottle + remain//3)