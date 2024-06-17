N, M = map(int, input().split())
answer = []

def recur(num):
    if num == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N + 1):
        if i in answer:
            continue
        answer.append(i)
        recur(num + 1)
        answer.pop()
        

recur(0)       

    