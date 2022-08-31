num_lst = []
for _ in range(9):
    num_lst.append(int(input()))
s_lst = sorted(num_lst)
max_num = max(num_lst)
max_idx = 0
for i in range(9):
    if num_lst[i] == max_num:
        max_idx = i + 1
        break
print(max_num)
print(max_idx)
