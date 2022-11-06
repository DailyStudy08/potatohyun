N = int(input())
lst = [list(map(int,input().split())) for n in range(N)]
for n in range(N):
    cnt = 1
    for m in range(N):
        if lst[n][0] < lst[m][0]:
            if lst[n][1] < lst[m][1]:
                cnt += 1
    lst[n].append(cnt)
for i in range(N):
    print(lst[i][2],end=' ')

