N = int(input())
P = sorted(list(map(int, input().split())))

times = []*1111
times.append(P[0])
for i in range(1, len(P)):
    times.append(times[i - 1] + P[i]) 
    
print(sum(times))
    

