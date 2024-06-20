N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))

cut_tree = 0

# 기준: 자른 나무의 합이 M 보다 크거나 같을때
# 범위: 절단기의 높이. 1~max(trees)

s = 1
e = max(trees)

h = 0

while s <= e:
    mid = (s + e)//2
    cut_tree = sum([t - mid for t in trees if t - mid > 0])

    if cut_tree >= M:
        s = mid + 1
        if h < mid:
            h = mid
        
    else:
        e = mid - 1
        
print(h)       