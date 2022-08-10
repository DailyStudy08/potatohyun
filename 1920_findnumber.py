N = int(input())
NA = sorted(list(map(int,input().split())))
M = int(input())
MA = list(map(int,input().split()))
def bin(a,n,key):
    st = 0
    end = n-1
    while st <= end:
        mm = (st+end)//2
        if a[mm] == key:
            return 1
        elif a[mm] > key:
            end = mm -1
        else:
            st = mm +1
    return 0
for i in MA:
    print(bin(NA,N,i))