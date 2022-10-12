'''
stack_4949.균형잡힌세상
https://www.acmicpc.net/problem/4949
'''


while True:
    sentence = list(input())
    if sentence[0] == '.':
        break
    stack = []
    for s in sentence:
        if s == '.':
            break
        
        elif (s == ')' or  s == ']') and stack :
            if s == ')' and stack[-1] =='(':
                stack.pop()
            elif s == ']' and stack[-1] =='[':
                stack.pop()
            else:           # s가 ')' or  ']'인데 stack[-1] 도 ')' or  ']'인 경우를 고려해줘야함.
                stack.append(s)
        elif s == '(' or s == '[':
            stack.append(s)
        elif s == ')' or  s == ']':
            stack.append(s)
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
'''
input받을때 문장제시해주고 싶으면 sentence = input('입력 : ') 이런식으로 input()안에 작성해주면됨(여기서쓰인건 아닌데 서치하다가 알게됨)
엔터해서 종료시킬때는 if 변수==''로 해주면 됨
21번째 줄인가? else구문 없어서 틀렸다.
->닫히는 괄호일때 stack의 마지막이마지막일수도 있으니까

'''

