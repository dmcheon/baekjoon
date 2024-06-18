
# 신맛과 쓴맛의 차이가 가장 작은 요리. 신맛은 사용한 신맛의 곱. 쓴맛은 사용한 재료의 합. 
# 완전 탐색으로 모든 경우의 수를 할 수도 있지만 재귀로도 할 수 있을듯. 


def recur(ingre_idx, S, B, use):
    global answer
    # 종료조건: 마지막 재료까지 탐색이 끝났으면 종료
    if ingre_idx == N:
        if use > 0:
            answer = min(abs(S - B), answer)
        return
    
    # 호출 로직: 다음 재료를 사용할때
    recur(ingre_idx + 1, S*ingre[ingre_idx][0], B + ingre[ingre_idx][1], use+1)
    # 다음 재료를 사용하지 않을때
    recur(ingre_idx + 1, S, B, use)
    
    
N = int(input())
ingre = [list(map(int, input().split())) for _ in range(N)]
answer = 999999999999
recur(0, 1, 0, 0)
print(answer)