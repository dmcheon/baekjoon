N = int(input())
keys = [int(input()) for _ in range(N)]
answer = ["YES" for _ in range(N)]

for i, key in enumerate(keys):
    for n in range(2, 1000001):
        if key % n == 0:
            answer[i] = "NO"
            break
        
for a in answer:
    print(a)