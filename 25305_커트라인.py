N, K = map(int, input().split())
score_lst = list(map(int, input().split())) 
score_lst.sort(reverse=True)
print(score_lst)

print(score_lst[K-1])