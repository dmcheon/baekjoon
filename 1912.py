N = int(input())
arr = list(map(int, input().split()))

sum_arr = [0 for _ in range(N + 1)]

for i in range(N):
    if sum_arr[i] + arr[i] < arr[i]:
        sum_arr[i + 1] = arr[i]
    else:
        sum_arr[i + 1] = sum_arr[i] + arr[i]

sum_arr.pop(0)       
print(max(sum_arr))
    
    