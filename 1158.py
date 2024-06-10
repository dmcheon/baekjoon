import sys

input = sys.stdin.readline().split()
N = int(input[0])
K = int(input[1])

origin = [i + 1 for i in range(N)]
result = []
index = 0
for i in range(N):
    pop_index = (index + (K - 1)) % len(origin)
    result.append(origin.pop(pop_index))
    index = pop_index
    
    
print(result)