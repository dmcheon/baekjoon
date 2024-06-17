N, M = map(int, input().split())

#자연수 중에서 중복 없이 M개를 고른 수열.

answer = []
def recur(num):
    #종료 조건: 수열의 개수가 M개일 때.
    if num == M:
        print(' '.join(map(str, answer)))
    
    for i in range(1, N + 1):
        if len(answer) > 0 and i <= answer[-1]:
            continue
        answer.append(i)
        recur(num + 1)
        answer.pop()  
        
recur(0)  