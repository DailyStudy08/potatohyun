'''
stack_9012.괄호
https://www.acmicpc.net/problem/9012
'''
T = int(input())
for _ in range(T):
    stack = []
    arr = list(input())
    for i in arr:
        if i == ')' and stack and stack[-1] =='(':
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
'''
수업에서 했던 문제.
처음엔 if에서 '('들어가는거도 다 고려해줬는데 
생각해보니까 ')'가 들어갈때 pop하는 조건만 잘 생각해주면 나머지 경우는 전부append니까
else로 묶어줄수 있었다.
'''
