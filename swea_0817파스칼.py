T = int(input())
for tc in range(1,T+1):
    print(f'#{tc}')
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if j == 0:
                arr[i][j] = 1
            elif i != 0:  
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        for a in range(N):
            if arr[i][a] != 0:
                print(arr[i][a],end=' ')
        print()
