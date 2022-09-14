answer = input()
# print(len(answer))
score = 0
v_list = list(answer)
# print(v_list)
for i in range(len(v_list)):
    if v_list[i] == 'O':
        if i == 1:
            score += 1
        else:
            pass