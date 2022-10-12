'''
기초수학_1193.분수찾기
https://www.acmicpc.net/problem/1193
'''

X = int(input())

flag = 1    # 1 : 탑, 2: 바텀
turn = 1
top,bottom = 1, 1
while turn != X:
    if flag == 1:
        if top == 1:
            flag = 2
            # bottom += 1
        else:
            top -= 1
            # bottom += 1
        bottom += 1
    elif flag == 2:
        if bottom == 1:
            flag = 1
            # top += 1
        else:
            # top += 1
            bottom -= 1
        top += 1
    turn += 1
print(top,'/',bottom)

'''
시간초과
'''

input_num = int(input())

line = 0  # 사선 라인
max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자
while input_num > max_num:
    line += 1  
    max_num += line  

gap = max_num - input_num 
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  #분자
    under = gap + 1  #분모
else :  # 사선 라인이 홀수번째 일 때
    top = gap + 1  #분자
    under = line - gap  #분모
print(f'{top}/{under}')