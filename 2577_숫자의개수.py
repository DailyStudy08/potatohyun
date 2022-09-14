'''방법1
num1 = int(input())
num2 = int(input())
num3 = int(input())
num_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cnt_lst = [0] * 10

ans = num1 * num2 * num3
sp_lst = list(str(ans))
for sp in sp_lst:
    idx = 0
    for nb in range(len(num_lst)):
        if sp == num_lst[nb]:
            idx = nb
            cnt_lst[idx] += 1

for i in cnt_lst:
    print(i)
'''

'''방법2
num1 = int(input())
num2 = int(input())
num3 = int(input())
cnt_lst = [0] * 10
ans = num1 * num2 * num3
ans_str = str(num1 * num2 * num3)

for i in range(len(ans_str)):
    cnt_lst[ans%10] += 1
    ans //= 10
for i in cnt_lst:
    print(i)
'''