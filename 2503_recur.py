
# 100~999 까지 모든 경우의 수를 순회.
# 재귀
import sys
# 파이썬 천번정도 반복하면 멈추기 때문에, 더 돌리기
sys.setrecursionlimit(9999999) 

def checker(hint_idx, number):
    
    curr_hint = hint[hint_idx]
    str_hint = str(curr_hint[0])
    str_number = str(number)
    
    if str_number[0] == '0' or str_number[1] == '0' or str_number[2] == '0':
        return False
    if str_number[0] == str_number[1] or \
        str_number[0] == str_number[2] or \
            str_number[1] == str_number[2]:
                return False   
            
    #스트라이크인 경우
    strike_cnt = 0
    if str_number[0] == str_hint[0]:
        strike_cnt += 1
    if str_number[1] == str_hint[1]:
        strike_cnt += 1
    if str_number[2] == str_hint[2]:
        strike_cnt += 1
        
    #볼인 경우
    ball_cnt = 0
    if str_number[0] == str_hint[1] or str_number[0] == str_hint[2]:
        ball_cnt += 1
    if str_number[1] == str_hint[0] or str_number[1] == str_hint[2]:
        ball_cnt += 1
    if str_number[2] == str_hint[0] or str_number[2] == str_hint[1]:
        ball_cnt += 1
        
    if strike_cnt == curr_hint[1] and ball_cnt == curr_hint[2]:
        return True
    return False
    
def recur(hint_idx, number):
    global answer
# 파라미터로 몇번째 힌트인지, 그리고 숫자 몇번째인지 넣어준다.
# 종료 조건: 마지막 힌트까지 다 통과하면 종료.
    if hint_idx == N:
        answer += 1
        recur(0, number +1)
        return
    if number > 999:
        return
    
    # 볼이랑 스트라이크 개수가 맞으면 다음 힌트도 맞는지 체크
    if checker(hint_idx, number):
        recur(hint_idx + 1, number)
    
    # 볼이랑 스트라이크 개수가 안맞으면 다음 숫자가 힌트에 맞는지 확인
    else:
        recur(0, number + 1)

N = int(input())
hint = [list(map(int, input().split())) for _ in range(N)]
answer = 0
recur(0, 100)
print(answer)