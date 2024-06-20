import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int, input().split())))
x = int(input())

count = 0
s = 0
e = n - 1
while s < e:
    # 각 포인터의 합이 x 값과 같을 때
    if A[s] + A[e] == x:
        count += 1
        e -= 1
    # 각 포인터의 합이 x 값 보다 작을 때
    elif A[s] + A[e] < x:
        s += 1
    else:
        e -= 1

print(count)