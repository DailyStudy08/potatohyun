N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

# 시작점 찾고 하기보다는 다 바꿔두고 그걸 바꿨으면 1, 아니면 0 으로 해서 
# 최소점 찾는거로 하면 합은 바로 구할 수 있을듯
# 근데 시작점이 검정색, 흰색 경우를 다 해봐야 할듯

min_cnt = 50*50
b_or_w = ['B','W']
for chance in range(len(b_or_w)):
    w_arr=[[0]*M for _ in range(N)]

    target = b_or_w[chance]
    ano_target = b_or_w[abs(chance-1)]
    for i in range(N):
        if i % 2:
            for j in range(0,M,2):
                if arr[i][j] != target:
                    w_arr[i][j] = 1
            for j in range(1,M,2):
                if arr[i][j] != ano_target:
                    w_arr[i][j] = 1
        else:
            for j in range(0,M,2):
                if arr[i][j] != ano_target:
                    w_arr[i][j] = 1
            for j in range(1,M,2):
                if arr[i][j] != target:
                    w_arr[i][j] = 1

    for x in range(N-7):
        for y in range(M-7):
            tmp_cnt = 0
            for t in range(8):
                tmp_cnt += sum(w_arr[x+t][y:y+9])
            if tmp_cnt < min_cnt:
                min_cnt = tmp_cnt
print(min_cnt)



'''
9 23
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBW
'''
'''
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
'''