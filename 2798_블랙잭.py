def ssum(N, M):
    lst =  sorted(list(map(int,input().split())))
    sum_lst=[]
    for i in range(N-2):
        for j in range(i+1,N-1):
            for l in range(j+1,N):
                if lst[i]+lst[j]+lst[l] == M:
                    return M
                if lst[i]+lst[j]+lst[l] > M:
                    break
                sum_lst.append(lst[i]+lst[j]+lst[l])
    return max(sum_lst)
N,M = map(int, input().split())
print(ssum(N, M))