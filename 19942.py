#식재료의 최소 영양 성분을 넣고 가격을 최소화
def recur(idx, p, f, s, v, c):
    global price
    global used
    global answer
   
   
    # 최소 영양성분이 다 들어갔는지 체크 후 가격 업뎃
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if price > c:
            price = c
            answer = []
            for i in used:
                answer.append(i)
      
    #종료조건: 마지막 재료까지 다 골랐을때               
    if idx == N:
        return
    
    # 영양 성분을 사용하는 케이스
    used.append(idx + 1)
    recur(idx + 1, nutri[idx][0] + p, nutri[idx][1] + f, nutri[idx][2] + s, \
        nutri[idx][3] + v, nutri[idx][4] + c)
    used.pop()
    # 영양 성분을 사용하지 않는 케이스
    recur(idx + 1, p, f, s, v, c)
    
    
    
#식재료 개수
N = int(input())
mp, mf, ms, mv = map(int, input().split())
nutri = [list(map(int, input().split())) for _ in range(N)]
used = []
answer = []
price = 9999999999
  
recur(0, 0, 0, 0, 0, 0)
answer.sort()

if answer:
    print(price)
    print(*answer)
else:
    print(-1)