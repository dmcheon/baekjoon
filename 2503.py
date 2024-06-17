#답이 안맞음. 나중에 고치기. 

N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k :
                continue
            
            check = 0
            for score in scores:
                number = score[0]
                strike = score[1]
                ball = score[2]
                
                ball_count = 0
                strike_count = 0
                
                string = str(number)
                
                if str(i) == string[0] or str(j) == string[1] or str(k) == string[2]:
                    strike_count += 1
                
                elif str(i) == string[1] or str(i) == string[2]:
                    ball_count += 1
                elif str(j) == string[0] or str(i) == string[2]:
                    ball_count += 1
                elif str(k) == string[0] or str(i) == string[1]:
                    ball_count += 1
                    
                
                if strike == strike_count and ball == ball_count:
                    check += 1
                    
            if check == N:
                answer += 1

print(answer)
                     
                
                    
                
                