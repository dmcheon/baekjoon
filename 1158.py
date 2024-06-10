N, K = map(int, input().split())

origin = [i + 1 for i in range(N)]
result = []
index = 0
for i in range(N):
    pop_index = (pop_index + (K - 1)) % len(origin)
    result.append(origin.pop(pop_index))
 
        
print(str(result).replace('[', '<').replace(']', '>'))