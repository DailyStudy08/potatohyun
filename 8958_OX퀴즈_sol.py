# from collections import deque
# deque.appendleft()

import sys
sys.stdin=open('input', 'r')   #입력값 파일로 해주면 한번에 뽑는거

tc = int(input())
for n in range(tc):
    answer = input()
    v_list = list(answer)
    score = 0
    nu_sum = 0
    for i in range(len(v_list)):
        if v_list[i] == 'O':
            nu_sum += 1
            score += nu_sum
        else :
            nu_sum = 0
    print(score)

