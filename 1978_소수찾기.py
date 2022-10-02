'''
baekjoon 1978_소수찾기
기본수학2
'''
'''
N = int(input())
# lst = set(map(int, input().split()))
lst = list(range(1,1001))
# cnt = 0
set_lst = set()
lstlst = []
for i in lst:
    # if i == 1:
    #     set_lst.add(i)
    #     # cnt += 1
    # if i == 2 or i == 3 or i == 5 or i == 7:
    #     continue
    # elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
    #     set_lst.add(i)
    #     # cnt += 1
    if i == 2 or i == 3 or i == 5 or i == 7:
        lstlst.append(i)
    elif i !=1 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:

        lstlst.append(i)
# print(len(lst-set_lst))
print(lstlst)
print(len(lstlst))
'''
N = int(input())
arr = list(map(int,input().split()))
sosu_lst = list(map(str,range(4,1001)))
sosu_copy = []
cnt = 0
for i in range(len(sosu_lst)):
    sosu_copy.append(sosu_lst[i])

for i in sosu_lst:
    for j in range(2,int(i)):
        pass
        if int(i)%j == 0:
            temp = str(i)
            sosu_copy.remove(temp)
            break

sosu_copy.append('2')
sosu_copy.append('3')

for i in arr:
    if str(i) in sosu_copy:
        cnt+=1

print(cnt)
