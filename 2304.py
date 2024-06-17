N = int(input())

columns = [list(map(int, input().split())) for _ in range(N)]
columns.sort()

tall_idx = 0
tall_height = 0
for i, col in enumerate(columns):
    if col[1] > tall_height:
        tall_height = col[1]
        tall_idx = i
        

height = columns[0][1]
result = tall_height

for i in range(tall_idx):
    if height < columns[i + 1][1]:
        result += height*(columns[i + 1][0] - columns[i][0])
        height = columns[i + 1][1]
    else:
        result += height*(columns[i + 1][0] - columns[i][0])
        

height = columns[-1][1]

for i in range(N - 1, tall_idx, -1):
    if height < columns[i - 1][1]:
        result += height*(columns[i][0] - columns[i - 1][0])
        height = columns[i - 1][1]
    else:
        result += height*(columns[i][0] - columns[i-1][0])
        
print(result)

    

