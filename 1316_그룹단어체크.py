N = int(input())
result = 0
for _ in range(N):
    lst = list(input())
    cnt = 0
    for i in range(1,len(lst)):
        if lst[i] in lst[0:i] and lst[i] != lst[i-1]:
            break
        else:
            cnt += 1
    if cnt == len(lst)-1:
        # print(lst)
        result += 1
print(result)