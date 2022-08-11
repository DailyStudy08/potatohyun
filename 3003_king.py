kqlbn = [1,1,2,2,2,8]
lst = list(map(int,input().split()))
result = []
for i in range(6):
    result.append(kqlbn[i]-lst[i])
print(*result)