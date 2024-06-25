
N = int(input())
meetings = ([list(map(int, input().split())) for _ in range(N)])
meetings.sort(key=lambda x:(x[1], x[0]))

max_n = 0
end_point = 0

for n_start, n_end in meetings:
    if end_point <= n_start:
        end_point = n_end
        max_n += 1
    
print(max_n)
    