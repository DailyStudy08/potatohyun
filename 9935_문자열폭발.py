'''
stack2_9935.문자열 폭발
https://www.acmicpc.net/problem/9935
'''


sentence = input()
bomb = input()
stack = []
for s in range(len(sentence)):  # 뒤에서부터 비교해야함.top으로 해서 하는 방향으로 해야할듯
    stack.append(sentence[s])
    if stack[-len(bomb):] == list(bomb):
        for _ in range(len(bomb)):
            stack.pop()
sentence = ''.join(stack)       # 리스트를 문자열로 합치는 방법

if sentence:
    print(sentence)
else:
    print('FRULA')
