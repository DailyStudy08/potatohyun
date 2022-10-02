'''
stack연습
'''
'''
push X: 정수 X를 스택에 넣는 연산.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
        만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 
    만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
N = int(input())
stack = []
answer = []
for _ in range(N):
    do_lst = input().split()
    if do_lst[0] == 'push':
        stack.append(int(do_lst[1]))
    elif do_lst[0] == 'pop':
        if len(stack) == 0:
            answer.append(-1)
        else:
            answer.append(stack.pop())
    elif do_lst[0] == 'size':
        answer.append(len(stack))
    elif do_lst[0] == 'empty':
        if stack:
            answer.append(0)
        else:
            answer.append(1)
    else:   #  do_lst[0] == 'top'
        if stack and stack[-1]:
            answer.append(stack[-1])
        else:
            answer.append(-1)
for i in answer:
    print(i)

'''
바로 print하니까 시간초과뜸
append로해서 출력하니까 통과... 왜...?
-> print하는게 생각보다 시간을 많이 잡아먹는대.
그래서 append로 답을 모아서 출력하는게 훨씬 빠른거고
'''