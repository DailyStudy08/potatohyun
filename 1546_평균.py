cnt = int(input())
score = list(map(int,input().split()))
score.sort()
max_score = score [-1]
ns_score = []
for i in range(cnt):
    ns_score.append(score[i]/score[-1]*100)
print(sum(ns_score)/cnt)