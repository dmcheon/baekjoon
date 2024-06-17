N = int(input())
checkers = [list(map(int, input().split())) for _ in range(N)]
x_diff, y_diff = 9999999, 9999999

for x in range(1, 1000001):
    for y in range(1, 1000001):
        temp_x_diff, temp_y_diff = 0, 0
        for check in checkers:
            temp_x_diff += abs(x - check[0])
            temp_y_diff += abs(y - check[1])
        
        if temp_x_diff < x_diff:
            x_diff = temp_x_diff
        if temp_y_diff < y_diff:
            y_diff = temp_y_diff
            
for check in checkers:
    print(abs(x_diff - check[0]) + abs(y_diff - check[1]))