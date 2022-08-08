tc = int(input())

for i in range(tc):
    lst = []
    lst.append(list(range(1,16)))

    k = int(input())    #층
    n = int(input())    #호수
    for j in range(1,k+1):
        tmp = [1]
        for m in range(1,n+1):
            tmp.append(lst[j-1][m]+tmp[m-1])
        lst.append(tmp)

    print(lst[k][n-1])
        