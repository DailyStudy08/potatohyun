'''
stack_10773.제로
'''

K = int(input())
stack = []
for k in range(K):
    money = int(input())
    if money == 0:
        stack.pop()
    else:
        stack.append(money)
sum = 0
for s in stack:
    sum+=s
print(sum)

'''
sum(stack)으로 프린트하면 런타임 에러 발생! 왜?
보통 런타임에러가 발생하는 이유는 다음과 같다.
1. 배열의 범위가 너무 적거나 많을 때
2. 0으로 무언가를 나눴을 때
3. 메모리를 과다하게 사용했을 떄
'''

