#나무자르기4
N, M = map(int, input().split())
trees = list(map(int, input().split()))

min_cut = 0
max_cut = max(trees)
answer = 0

while min_cut <= max_cut:
    cut = (min_cut + max_cut)//2
    cut_tree = sum([tree - cut for tree in trees if tree > cut])
    if cut_tree >= M:
        min_cut = cut + 1
        answer = cut
    else:
        max_cut = cut - 1 
        
print(answer)