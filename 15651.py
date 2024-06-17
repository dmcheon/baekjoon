N, M = map(int, input().split())

ans = []
def recur(num):
    #종료 조건: 수열의 개수가 M번째일때
    if num == M:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, N + 1):
        ans.append(i)
        recur(num + 1)
        ans.pop()
        
recur(0)