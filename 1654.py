#랜선 자르기
K, N = map(int, input().split())
lengths = [int(input()) for _ in range(K)]

#범위: 랜선의 길이
min_length = 1
max_length = sum(lengths)//N

#기준: 랜선의 개수
answer = 0

while min_length <= max_length:
    mid_length = (min_length + max_length) // 2
    n_lancable = sum([length // mid_length for length in lengths])
    
    if n_lancable >= N:
        answer = mid_length
        min_length = mid_length + 1
    else:
        max_length = mid_length - 1
        
print(answer)
