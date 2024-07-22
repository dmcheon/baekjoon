
def recur(depth, idx):
    if depth == 6:
        print(*out)
        return 

    for i in range(idx, k):
        out.append(S[i])
        recur(depth + 1, i + 1)
        out.pop()


while True:
    array = list(map(int, input().split()))
    k = array[0]
    if k == 0:
        break
    S = array[1:]
    out = []
    recur(0, 0)

    print()


