N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
# 종이 갯수
cnt = []

def divide(x, y, n):
    color = map[x][y]
    
    # 색이 같은지 판별
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != map[i][j]:
                for a in range(3):
                    for b in range(3):
                        divide(x + (n//3)*a, y + (n//3)*b, n//3)
                return
            
    
    #색에 따라 종이의 개수 삽입
    if color == 1:
        cnt.append(1)
    
    elif color == -1:
        cnt.append(-1)
    else:
        cnt.append(0)
        
divide(0, 0, N)
print(cnt.count(-1), cnt.count(0), cnt.count(1), sep='\n')
