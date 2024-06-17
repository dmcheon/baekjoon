N, M = map(int, input().split())

answer = []

def recur(num):
    #종료 조건: 수열 개수가 M개면 종료
    if num == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N + 1):
        if len(answer) > 0 and answer[-1] > i:
            continue
        answer.append(i)
        recur(num + 1)
        answer.pop()

recur(0)